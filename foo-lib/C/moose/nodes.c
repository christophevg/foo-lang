// nodes
// nodes related functions, specific for the moose platform
// author: Christophe VG

#include <string.h> // for memcpy: can be avoided

#include "../stdarg-collect.h"
#include "../nodes.h"

#include "moose/xbee.h"

/*
 * This implementation adds a bit of additional functionality to simulate
 * multi-hop messaging. Routing is made explicit by a statically configured
 * next hop. If a destination is NOT the next hop, the message is send to the
 * next hop. This next hop is also explicitly added as the first 64 bits of the
 * payload and the final destination is added as the second 64 bits of the
 * payload. All messaging is done through broadcasting, which allows us to
 * identify if a packet was meant for us, or if we overheart communication
 * between two other nodes. If a real broadcast is send, the final destination
 * and the hop are set to the default broadcast node.
 */

// forward declarations of private helper functions
void _accept_frame(xbee_rx_t* frame);
void _broadcast(void);
void _send(void);
void _xbee_send(uint16_t hop, uint16_t to, uint8_t size, uint8_t* payload);

// our fixed next hop
node_t* next_hop;

// broadcasted messages are collected into a buffer  

// because we add 2*2 bytes for internal hop and destination mgmt, the maximum
// amount of bytes that can be send/collected is 104-4 = 100

#define MAX_SIZE 100

uint8_t broadcast_buffer[MAX_SIZE];
uint8_t broadcast_size = 0;

// we keep a buffer for each possible node. this implementation should be more
// dynamic, to accomodate for large numbers of nodes. here we can simply
uint8_t send_buffer[MAX_NODES][MAX_SIZE];
uint8_t send_size[MAX_NODES];

// register our own incoming frame handler
void nodes_io_init(void) {
  xbee_init();                    // initialize use of XBee module
  xbee_wait_for_association();    // wait until the network is available
  xbee_on_receive(_accept_frame);
  // add our own node and a broadcast node
  nodes_lookup(xbee_get_nw_address());
  nodes_lookup(0xFFFE);
  // prepare node for parent
  next_hop = nodes_lookup(xbee_get_parent_address());
  // init buffers
  broadcast_size = 0;
  for(uint8_t i=0; i<nodes_count(); i++) { send_size[i] = 0; }
}

void nodes_broadcast(uint16_t size, ...) {
  if(size > MAX_SIZE-broadcast_size) { return; } // TODO: dont' drop silently
  uint8_t* buffer = &(broadcast_buffer[broadcast_size]);
  va_collect(buffer, size, uint8_t);
  broadcast_size += size;
}

void nodes_send(node_t* node, uint16_t size, ...) {
  if(size > MAX_SIZE-send_size[node->id]) { return; }//TODO: dont' drop silently
  uint8_t* buffer = &(send_buffer[node->id][broadcast_size]);
  va_collect(buffer, size, uint8_t);
  send_size[node->id] += size;
}

void nodes_io_process(void) {
  _broadcast();
  _send();
  xbee_receive();
}

uint16_t nodes_get_nw_address(void) {
  return xbee_get_nw_address();
}

// private helper functions

void _accept_frame(xbee_rx_t* frame) {
  node_t* from = nodes_lookup(frame->nw_address);
  node_t* hop  = nodes_lookup(frame->data[1] | frame->data[0] << 8);
  node_t* to   = nodes_lookup(frame->data[3] | frame->data[2] << 8);
  payload_parser_parse(from, hop, to,
                       make_payload(&(frame->data[4]), frame->size-4));
}

void _broadcast(void) {
  if(broadcast_size > 0) {
    _xbee_send(XB_NW_BROADCAST, XB_NW_BROADCAST, broadcast_size, 
               broadcast_buffer);
    broadcast_size = 0;
  }
}

void _send(void) {
  for(uint8_t i=0; i<nodes_count(); i++) {
    if(send_size[i] > 0) {
      _xbee_send(next_hop->address, nodes_get(i)->address, send_size[i],
                 send_buffer[i]);
      send_size[i] = 0;
    }
  }
}

void _xbee_send(uint16_t hop, uint16_t to, uint8_t size, uint8_t* payload) {
  uint8_t* bytes = malloc(2*2+size);
  // add broadcast hop and destination
  bytes[0] = (uint8_t)(hop >> 8);
  bytes[1] = (uint8_t)(hop);
  bytes[2] = (uint8_t)(to >> 8);
  bytes[3] = (uint8_t)(to);
  // copy in the actual payload (TODO: can be avoided by preloading them)
  memcpy(&(bytes[4]), payload, size);

  xbee_tx_t frame;
  frame.size        = size + 2*2;
  frame.id          = XB_TX_NO_RESPONSE;
  frame.address     = XB_BROADCAST;
  frame.nw_address  = XB_NW_BROADCAST;
  frame.radius      = XB_MAX_RADIUS;
  frame.options     = XB_OPT_NONE;
  frame.data        = bytes;
  xbee_send(&frame);
}
