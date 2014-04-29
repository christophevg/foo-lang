// nodes
// nodes related functions
// author: Christophe VG

#include <stdio.h>

#include <stdlib.h>
#include <string.h>

#include "stdarg-collect.h"
#include "nodes.h"
#include "bool.h"

// the internal list of nodes
node_t  nodes[MAX_NODES];
uint8_t next_node = 0;

// forward declarations of private functions
node_t* _add_node(uint16_t address);
void    _add_node_handler(time_t interval, node_handler_t handler, bool all);

#define MOCK_NETWORK_NAME STR(MOCK_NETWORK)
#ifdef MOCK_NETWORK
void nodes_io_init(void) {
  // nothing todo
}
void nodes_io_process(void) {
  // nothing todo
}
uint16_t nodes_get_nw_address(void) {
  return 0; // default for local testing
}
#endif

// initializes the nodes information with an entry for our own node
void nodes_init(void) {
  nodes_io_init();
}

// we can only handle the generic attributes
node_t* _add_node(uint16_t address) {
  nodes[next_node].id      = next_node;
  nodes[next_node].address = address;
  next_node++;
  return &nodes[next_node-1];
}

// looks up a node based on its address. if not found, the node is created.
node_t* nodes_lookup(uint16_t address) {
  for(uint8_t n=0; n<next_node; n++) {
    if(nodes[n].address == address) {
      return &nodes[n];
    }
  }
  // unknown nodes are created on the fly
  return _add_node(address);
}

uint8_t nodes_count(void) {
  return next_node;
}

node_t* nodes_get(uint8_t id) {
  return &nodes[id];
}

node_t* nodes_self(void) {
  return &nodes[0];
}

// SCHEDULING

// TODO: replace this by dynamic memory allocation, based on compilation unit
//       information
#define MAX_HANDLERS  5
#define MAX_INTERVALS 5

typedef struct {
  time_t           interval;
  time_t           next;
  uint8_t          next_handler;
  struct {
    node_handler_t handler;
    bool           all;
  } handlers[MAX_HANDLERS];
} nodes_schedule_t;

nodes_schedule_t schedule[MAX_INTERVALS];
uint8_t          next_schedule;

void nodes_schedule_all(time_t interval, node_handler_t handler) {
  _add_node_handler(interval, handler, TRUE);
}

void nodes_schedule_own(time_t interval, node_handler_t handler) {
  _add_node_handler(interval, handler, FALSE);
}

void _add_node_handler(time_t interval, node_handler_t handler, bool all) {
  // look up the interval
  for(uint8_t i=0; i<next_schedule; i++) {
    if( schedule[i].interval == interval) {
      // add a handler to this interval
      schedule[i].handlers[schedule[i].next_handler].handler = handler;
      schedule[i].handlers[schedule[i].next_handler].all     = all;
      schedule[i].next_handler++;
      return;
    }
  }
  // didn't find an previous defined interval, create a new one and add the
  // handler to it
  schedule[next_schedule].interval            = interval;
  schedule[next_schedule].next                = now() + interval;
  schedule[next_schedule].handlers[0].handler = handler;
  schedule[next_schedule].handlers[0].all     = all;
  schedule[next_schedule].next_handler        = 1;
  next_schedule++;
}

// check if any of the intervals are met, if so, loop all nodes and call handler
// do this for both all_nodes and own_node.
void nodes_process(void) {
  nodes_io_process();
  
  time_t current = now();
  for(uint8_t s=0; s<next_schedule; s++) {
    if(current >= schedule[s].next) {
      // execute handlers for this interval
      for(uint8_t h=0; h<schedule[s].next_handler; h++) {
        if(schedule[s].handlers[h].all) {
          // for all nodes, excluding ourselves (aka node 0)
          for(uint8_t n=1; n<next_node; n++) {
            schedule[s].handlers[h].handler(&nodes[n]);
          }
        } else {
          // only for our node
          schedule[s].handlers[h].handler(nodes_self());
        }
      }
      // and schedule next execution
      schedule[s].next = current + schedule[s].interval;
    }
  }
}

// PAYLOAD

payload_t* make_payload(uint8_t* bytes, int size) {
  payload_t* payload = malloc(sizeof(payload_t));
  payload->size = size;
  payload->bytes = malloc(size * sizeof(uint8_t));
  memcpy(payload->bytes, bytes, size);
  return payload;
}

payload_t* copy_payload(payload_t* source) {
  payload_t* copy = malloc(sizeof(payload_t));
  copy->size = source->size;
  copy->bytes = malloc(source->size * sizeof(uint8_t));
  memcpy(copy->bytes, source->bytes, source->size);
  return copy;
}

void free_payload(payload_t* payload) {
  free(payload->bytes);
  free(payload);
}

bool payload_contains(payload_t* payload, int size, ...) {
  uint8_t* needle = malloc(size * sizeof(uint8_t));
  va_collect(needle, size, uint8_t);

  for(uint16_t h=0; h < payload->size - size; h++) {
    uint16_t n=0;
    while(n<size && payload->bytes[h+n] == needle[n]) { n++; }
    if(n==size) {
      free(needle);
      return TRUE;
    }
  }
  free(needle);
  return FALSE;
}

// PAYLOAD PARSER

typedef struct parser_node_t {
  uint8_t               byte;     // the byte that matches this node/step
  payload_handler_t     handler;  // if we reach this step, execute this handler
  struct parser_node_t* alt;      // possible alternative at this step
  struct parser_node_t* next;     // possible next steps
} parser_node_t;

parser_node_t* parser = NULL;

parser_node_t* _create_node(uint8_t byte, payload_handler_t handler) {
  parser_node_t* node = malloc(sizeof(parser_node_t));
  node->byte    = byte;
  node->handler = handler;
  node->next    = NULL;
  node->alt     = NULL;
  return node;
}

parser_node_t* _add_alt(parser_node_t* sibbling, uint8_t byte,
                        payload_handler_t handler)
{
  parser_node_t* node = _create_node(byte, handler);
  sibbling->alt = node;
  return node;
}

parser_node_t* _add_next(parser_node_t* parent, uint8_t byte,
                         payload_handler_t handler)
{
  parser_node_t* node = _create_node(byte, handler);
  parent->next = node;
  return node;
}

parser_node_t* _find_alt(parser_node_t* node, uint8_t byte) {
  while(node->byte != byte && node->alt != NULL) {
    node = node->alt;
  }
  return node;
}

void _append_step(parser_node_t** start, uint8_t byte, payload_handler_t handler) {
  parser_node_t* node = *start;

  // do we have the next byte already as a node ?
  if(node->byte != byte) { // we didn't find a previous entry at level
    node = _add_alt(node, byte, handler);
  }
}

// adds a parser rule:
// a rule consists of a sequences of bytes  B1 B2 B3 ...
// each byte is matched at a level of the parser L1 L2 L3 ...
// each level of the parser consists of multiple alternatives LxA1 LxA2 LxA3 ...
// from each alternative a next alternative level can be constructed.
// the result is a tree with handlers at the leafs == fully matched rules
// adding a parser rule requires looping over all bytes and inserting them into
// the parser at each level. this can require creation of a new alternative 
// level with a first alternative or adding an alternative.
void _add_parser_rule(uint8_t* rule, uint16_t size, payload_handler_t handler) {
  if(size == 0) { return; } // nothing to add ;-)

  parser_node_t* node   = parser;  // points to the current level
  parser_node_t* parent = NULL;    // points to the previous level
                                   // e.g. node = parent->next

  // we step through the rule but hold off the last step == execution step
  // at the start of each iteration, node points to the first alternative for 
  // the "next" step of its parent.
  // at the end of the loop, node points to a previously created and found node
  // or a newly added one for this step. node and parent are updated.
  for(uint16_t step=0; step<size-1; step++) {
    // if the current level doesn't contain a list of alternatives yet, we 
    // create the first and link it from the parent (level)
    if(node == NULL) {
      if(parent == NULL) {
        // we're creating the very first node
        parser = _create_node(rule[step], NULL);
        node   = parser;
      } else {
        parent = _create_node(rule[step], NULL);
        node   = parent;
      }
    } else {
      // find an existing alternative for this byte
      node = _find_alt(node, rule[step]);
      if(node->byte == rule[step]) {
        // found a previous alternative, we're good
      } else {
        // we're at the end and need to add an alternative
        node = _add_alt(node, rule[step], NULL);
      }
    }
    // move node and parent
    parent = node;
    node   = node->next;
  }

  // add the last step with its handler
  if(node == NULL) {
    if(parent == NULL) {
      parser = _create_node(rule[size-1], handler);
    } else {
      parent->next = _create_node(rule[size-1], handler);
    }
  } else {
    node = _find_alt(node, rule[size-1]);
    if(node->byte == rule[size-1]) {
      node->handler = handler;
    } else {
      _add_alt(node, rule[size-1], handler);
    }
  }
}

void payload_parser_register(payload_handler_t handler, int size, ...) {
  uint8_t* rule = malloc(size * sizeof(uint8_t));
  va_collect(rule, size, uint8_t);
  _add_parser_rule(rule, size, handler);
}

void _dump(parser_node_t* node, int prefix) {
  parser_node_t* local = node;
  while(local != NULL) {
    for(int i=0; i<prefix; i++) { printf(" "); }
    printf("0x%02X\n", local->byte);
    _dump(local->next, prefix + 2);
    local = local->alt;
  }
}

void payload_parser_dump_rules(void) {
  _dump(parser, 0);
}

void payload_parser_reset(void) {
  // TODO: clean up used memory
  parser = NULL;
}

payload_t* parsed;
uint16_t   cursor;

payload_handler_t _parse(void) {
  parser_node_t* node = parser;
  while(node != NULL && cursor < parsed->size) {
    // find alternative at this level/step
    while(node->byte != parsed->bytes[cursor] && node->alt != NULL) {
      node = node->alt;
    }
    // we found a match, or we're at the last alternative
    if(node->byte != parsed->bytes[cursor]) {
      // no match ... bail out
      if(node == parser) {
        // this was first step in parser, and we couldn't parse the current 
        // byte, so this byte is unparsable... skip it
        cursor++;
      }
      return NULL;
    }
    // match, move cursor
    cursor++;
    // check if we have a handler
    if(node->handler != NULL) {
      return node->handler;
    }
    // continue to next level
    node = node->next;
  }
  return NULL;
}

void payload_parser_parse(node_t* sender, node_t* hop, node_t* receiver, 
                          payload_t* payload)
{
  parsed = payload;
  cursor = 0;

  // loop to restart parsing until all bytes have been parsed
  while(parser != NULL && cursor < parsed->size) {
    payload_handler_t handler = _parse();
    if( handler != NULL && cursor < parsed->size) {
      handler(sender, hop, receiver);
    }
  }
}

time_t payload_parser_consume_timestamp(void) {
  uint8_t* bytes = payload_parser_consume_bytes(sizeof(time_t));
  union { 
    time_t ts;
    uint8_t  b[sizeof(time_t)];
  } conv;
  memcpy(&conv.b, bytes, sizeof(time_t));
  free(bytes);
  return conv.ts;
}

uint8_t payload_parser_consume_byte(void) {
  uint8_t byte = parsed->bytes[cursor];
  cursor++;
  return byte;
}

uint8_t* payload_parser_consume_bytes(int amount) {
  uint8_t* bytes = malloc(amount*sizeof(uint8_t));
  for(uint16_t i=0; i<amount && cursor < parsed->size; i++, cursor++) {
    bytes[i] = parsed->bytes[cursor];
  }
  return bytes;
}
