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
  handled++;
  if(handled > 2) { assert(node->address - (node->id*100) == 30); }
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
  nodes_process();  // triggers handler0 3x

  usleep(100*1000);
  // time ~= 200
  nodes_process();  // triggers handler0 3x

  usleep(100*1000);
  // time ~= 300
  nodes_process();  // triggers handler0 3x and handler1 2x

  node_t* self = nodes_self();
  assert(self->address == 30);

  assert( handled == 11 );
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

void test_nodes(void) {
  printf("--- testing nodes\n");

  nodes_init();

  test_nodes_scheduling();
  test_payload_basics();
}

int main(void) {

  printf("*** performing all tests for foo-lib...\n");

  test_crypto();
  test_time();
  test_nodes();

  printf("*** SUCCESS\n");
  
  exit(EXIT_SUCCESS);
}
