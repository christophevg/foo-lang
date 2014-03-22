// nodes
// nodes related functions
// author: Christophe VG

#include <stdio.h>

#include <stdlib.h>
#include <string.h>

#include "stdarg-collect.h"
#include "nodes.h"
#include "bool.h"

// based on memory analysis, the maximum number of nodes can be roughly 
// determined. a low value for testing and demo purposes is used here.
// could be extended to a dynamic memory allocation system with memory
// constraint checking. but that is not really the goal here ;-)
#define MAX_NODES 5

// the internal list of nodes
node_t  nodes[MAX_NODES];
uint8_t next_node = 0;

// forward declarations of private functions
node_t* _add_node(uint64_t address);
void    _add_node_handler(time_t interval, node_handler_t handler, bool all);

// initializes the nodes information with an entry for our own node
void nodes_init(void) {
  _add_node(0);
}

// we can only handle the generic attributes
node_t* _add_node(uint64_t address) {
  nodes[next_node].id      = next_node;
  nodes[next_node].address = address;
  next_node++;
  return &nodes[next_node-1];
}

// looks up a node based on its address. if not found, the node is created.
node_t* nodes_lookup(uint64_t address) {
  for(uint8_t n=0; n<next_node; n++) {
    if(nodes[n].address == address) {
      return &nodes[n];
    }
  }
  // unknown nodes are created on the fly
  return _add_node(address);
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

