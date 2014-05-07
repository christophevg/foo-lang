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

// based on memory analysis, the maximum number of nodes can be roughly 
// determined. a low value for testing and demo purposes is used here.
// could be extended to a dynamic memory allocation system with memory
// constraint checking. but that is not really the goal here ;-)

#define MAX_NODES 5

// initializes the internal working of the nodes module
void nodes_init(void);

void nodes_process(void);

node_t* nodes_lookup(uint16_t address);

uint8_t nodes_count(void);
node_t* nodes_get(uint8_t id);

node_t* nodes_self(void);

// SCHEDULING

typedef void (*node_handler_t)(node_t* node);

void nodes_schedule_all(time_t interval, node_handler_t handler);

void nodes_schedule_own(time_t interval, node_handler_t handler);

#include "payload.h"

// PAYLOAD PARSER

typedef void (*payload_handler_t)(node_t* me, node_t* sender,
                                  node_t* from, node_t* hop, node_t* to,
                                  payload_t* payload);

void payload_parser_dump_rules(void);

void payload_parser_reset(void);

void payload_parser_register(payload_handler_t handler, int num, ...);

void payload_parser_register_else(payload_handler_t handler);

void payload_parser_register_all(payload_handler_t handler);

void payload_parser_parse(uint16_t source_addr,
                          uint16_t from_addr, uint16_t hop_addr, uint16_t to_addr,
                          uint8_t size, uint8_t* payload_bytes);

time_t payload_parser_consume_timestamp(void);

uint8_t payload_parser_consume_byte(void);

uint8_t* payload_parser_consume_bytes(int amount);

node_t* payload_parser_consume_node(void);

float payload_parser_consume_float(void);

/*
 * Network related functions are platform specific. A platform implementation
 * needs to provide the implementation for the signature defined above.
 * e.g. see moose/nodes.c
 */

void     nodes_io_init(void);
uint16_t nodes_get_nw_address(void);
void     nodes_broadcast(uint16_t num, ...);
void     nodes_send(node_t* node, uint16_t num, ...);
void     nodes_io_process(void);

#endif
