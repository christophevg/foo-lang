// test
// tests all foo-lib/C modules
// author: Christophe VG

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <unistd.h>

#include "crypto.h"
#include "time.h"
#include "nodes.h"

void test_crypto(void) {
  printf("--- testing crypto\n");
  uint8_t expected[20] = { 0x2a, 0xae, 0x6c, 0x35, 0xc9, 0x4f, 0xcf, 0xb4, 0x15, 
                           0xdb, 0xe9, 0x5f, 0x40, 0x8b, 0x9c, 0xe9, 0x1e, 0xe8,
                           0x46, 0xed };
  // sha1
  uint8_t* hash = sha1(11, 'h', 'e', 'l', 'l', 'o', ' ', 
                           'w', 'o', 'r', 'l', 'd');
  assert(memcmp(hash, expected, 20) == 0);

  // sha1_compare
  assert(sha1_compare(expected, 11, 'h', 'e', 'l', 'l', 'o', ' ',
                                    'w', 'o', 'r', 'l', 'd'));
  assert(sha1_compare(expected, 11, 'H', 'E', 'L', 'L', 'O', ' ',
                                    'W', 'O', 'R', 'L', 'D') == FALSE);
}

void test_time(void) {
  printf("--- testing time\n");
  time_t prev = now();
  usleep(100*1000);
  for(int i=0; i<10; i++) {
    time_t current = now();
    if( current >= prev + 10) {
      prev = current;
    } else {
      printf("FAIL: time did not advance in between cycles: %lu < %lu\n",
             prev, current);
    }
    usleep(10*1000);
  }
}

uint8_t handled = 0;

void handler0(node_t* node) {
  handled++;
  node->address += 10;
}

void handler1(node_t* node) {
  if(handled > 2 && node->id != 1) {
    handled++;
    assert(node->address - ((node->id-1)*100) == 30);
  }
}

void test_nodes_scheduling(void) {
  printf("    - scheduling\n");

  // introduce some nodes through the lookup function
  nodes_lookup(100);
  nodes_lookup(200);

  nodes_schedule_all(100, handler0);
  nodes_schedule_own(100, handler0);
  nodes_schedule_all(300, handler1);

  // time ~= 0
  usleep(100*1000);
  // time ~= 100
  nodes_process();  // triggers handler0 4x

  usleep(100*1000);
  // time ~= 200
  nodes_process();  // triggers handler0 4x

  usleep(100*1000);
  // time ~= 300
  nodes_process();  // triggers handler0 4x and handler1 2x

  node_t* self = nodes_self();
  assert(self->address == 30);

  assert( handled == 14 );
}

void test_payload_basics(void) {
  printf("    - payload\n");

  uint8_t data[11] = { 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd' };

  payload_t* payload = make_payload((uint8_t*)&data, 11);

  assert(memcmp(data, payload->bytes, 11) == 0);
  assert(payload->size == 11);

  assert(payload_contains(payload, 2, 'l', 'l'));
  assert(payload_contains(payload, 2, 'l', 'a') == FALSE);
  assert(payload_contains(payload, 5, 'l', 'a', 't', 'e', 'r') == FALSE);

  payload_t* payload2 = copy_payload(payload);

  assert(memcmp(payload2->bytes, payload->bytes, 11) == 0);
  assert(payload2->size == 11);
}

bool    found_first  = FALSE;
bool    found_second = FALSE;
uint8_t hits         = 0;

void payload_handler0(node_t* from, node_t* hop, node_t* to) {
  assert(found_second == FALSE);
  found_first = TRUE;
  hits++;
  // consume 3 bytes
  assert(payload_parser_consume_byte() == 0x10);
  assert(payload_parser_consume_byte() == 0x30);
  assert(payload_parser_consume_byte() == 0x40);
}

void payload_handler1(node_t* from, node_t* hop, node_t* to) {
  assert(found_first);
  found_second = TRUE;
  hits++;
  // consume 3 bytes
  assert(payload_parser_consume_byte() == 0x60);
  assert(payload_parser_consume_byte() == 0x10);
}

void test_payload_parser(void) {
  printf("    - payload parser\n");

  uint8_t data[9] = { 0x10, 0x20, 0x10, 0x30, 0x40, 0x10, 0x50, 0x60, 0x10 };
  payload_t* payload = make_payload((uint8_t*)&data, 9);

  // configure parser actions
  payload_parser_register(payload_handler0, 2, 0x10, 0x20);
  payload_parser_register(payload_handler1, 2, 0x10, 0x50);

  // introduce some nodes through the lookup function
  node_t* node1 = nodes_lookup(100);
  node_t* node2 = nodes_lookup(200);
  node_t* node3 = nodes_lookup(300);

  payload_parser_parse(node1, node2, node3, payload);

  assert(found_first && found_second && (hits==2));
}

time_t ts;
bool   found_ts = FALSE;

void timestamp_consumer(node_t* from, node_t* hop, node_t* to) {
  assert(payload_parser_consume_timestamp() == ts);
  found_ts = TRUE;
}

void test_payload_timestamp_consumer(void) {
  ts = now();
  union {
    time_t  ts;
    uint8_t b[sizeof(time_t)];
  } conv = { .ts = ts };
  uint8_t* ts_data = malloc(2*sizeof(uint8_t)+sizeof(time_t));
  ts_data[0] = 0x00;
  ts_data[1] = 0x10;
  memcpy(&ts_data[2], conv.b, sizeof(time_t));
  payload_t* payload = make_payload(ts_data, 2+sizeof(time_t));

  payload_parser_register(timestamp_consumer, 2, 0x00, 0x10);

  // introduce some nodes through the lookup function
  node_t* node1 = nodes_lookup(100);
  node_t* node2 = nodes_lookup(200);
  node_t* node3 = nodes_lookup(300);

  payload_parser_parse(node1, node2, node3, payload);

  assert(found_ts);
}

void test_nodes(void) {
  printf("--- testing nodes\n");

  nodes_init();

  test_nodes_scheduling();
  test_payload_basics();
  test_payload_parser();
  test_payload_timestamp_consumer();
}

int main(void) {

  printf("*** performing all tests for foo-lib...\n");

  test_crypto();
  test_time();
  test_nodes();

  printf("*** SUCCESS\n");
  
  exit(EXIT_SUCCESS);
}
