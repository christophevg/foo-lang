// nodes
// nodes related functions
// author: Christophe VG

#ifndef _FOO_NODES
#define _FOO_NODES

#include <stdarg.h>
#include <stdint.h>

#include "bool.h"
#include "time.h"

// NODES

// nodes_t is generated and should already be known before this header file
// is included. To allow compilation without specific extended functionality,
// the default/minimal node struct is added here conditionally.

#ifndef _NODES_STRUCT
#define _NODES_STRUCT

typedef struct {
  // domain properties
  uint8_t  id;
  uint16_t address;
} node_t;

#endif

// initializes the internal working of the nodes module
void nodes_init(void);

void nodes_process(void);

node_t* nodes_lookup(uint64_t address);

node_t* nodes_self();

// SCHEDULING

typedef void (*node_handler_t)(node_t* node);

void nodes_schedule_all(time_t interval, node_handler_t handler);

void nodes_schedule_own(time_t interval, node_handler_t handler);


// PAYLOAD

typedef struct payload_t {
  uint8_t* bytes;
  uint16_t size;
} payload_t;

payload_t* make_payload(uint8_t* bytes, int size);

payload_t* copy_payload(payload_t* source);

void free_payload(payload_t* payload);

bool payload_contains(payload_t* payload, int num, ...);

// PAYLOAD PARSER

typedef void (*payload_handler_t)(node_t* from, node_t* to);

void payload_parser_dump_rules(void);

void payload_parser_register(payload_handler_t handler, int num, ...);

void payload_parser_parse(node_t* sender, node_t* receiver, payload_t* payload);

time_t payload_parser_consume_timestamp(void);

uint8_t payload_parser_consume_byte(void);

uint8_t* payload_parser_consume_bytes(int amount);

/*
 * Network related functions are platform specific. A platform implementation
 * needs to provide the implementation for the signature defined above.
 * e.g. see moose/nodes.c
 */

void nodes_broadcast(int num, ...);
void nodes_send(node_t* node, int num, ...);

#endif
