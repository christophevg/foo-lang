// test_all
// tests all foo-lib/C/moose modules
// author: Christophe VG

#include <avr/io.h>
#include <util/delay.h>

#include "moose/avr.h"
#include "moose/bool.h"
#include "moose/serial.h"
#include "moose/clock.h"

#include "../time.h"

#include "../external.h"
#define NODES_T_H_name STR(NODES_T_H)
#include STR(NODES_T_H)
#include "../nodes.h"

#define STATUS_LED_PORT    PORTB  // PB0
#define STATUS_LED_PIN     0

bool result = TRUE; // global indicator for test result

void test_time(void) {
  printf("--- testing time\n");
  _delay_ms(100L);
  time_t prev = 100;
  for(int i=0; i<10; i++) {
    time_t current = now();
    if( current >= prev + 10) {
      prev = current;
    } else {
      printf("FAIL: time did not advance in between cycles: %lu < %lu\n",
             prev, current);
      result = FALSE;
    }
    _delay_ms(10L);
  }
}

// nodes network access

bool handler0 = FALSE,
     handler1 = FALSE;

void handle_incoming_payload0(node_t* from, node_t* hop, node_t* to, payload_t* payload) {
  if( payload_parser_consume_byte() != 0x02 ) {
    printf("FAIL: first byte of echo != 0x02\n");
    return;
  }
  if( payload_parser_consume_byte() != 0x03 ) {
    printf("FAIL: second byte of echo != 0x03\n");
    return;
  }
  if( from->address != 0x0000 ) {
    printf("FAIL: from address doesn't match 0x0000\n");
    return;
  }
  if( hop->address != 0xFFFE ) {
    printf("FAIL: hop address doesn't match 0xFFFE\n");
    return;
  }
  if( to->address != 0xFFFE ) {
    printf("FAIL: to address doesn't match 0xFFFE\n");
    return;
  }
  handler0 = TRUE;
}

void handle_incoming_payload1(node_t* from, node_t* hop, node_t* to, payload_t* payload) {
  if( payload_parser_consume_byte() != 0x20 ) {
    printf("FAIL: first byte of echo != 0x20\n");
    return;
  }
  if( payload_parser_consume_byte() != 0x30 ) {
    printf("FAIL: second byte of echo != 0x30\n");
    return;
  }
  if( from->address != 0x0000 ) {
    printf("FAIL: from address doesn't match 0x0000\n");
    return;
  }
  if( hop->address != 0x0000 ) {
    printf("FAIL: hop address doesn't match 0x0000\n");
    return;
  }
  if( to->address != 0x0000 ) {
    printf("FAIL: to address doesn't match 0x0000\n");
    return;
  }
  handler1 = TRUE;
}

void test_nodes(void) {
  printf("--- testing nodes\n");
  
  nodes_init();

  // register a payload handler
  payload_parser_register(handle_incoming_payload0, 1, 0x01);
  payload_parser_register(handle_incoming_payload1, 1, 0x10);

  // broadcasting
  nodes_broadcast(3, 0x01, 0x02, 0x03);
  nodes_process();  // this broadcasts the message
  _delay_ms(200L);  // the echo server will re-broadcast it back, add some delay
  nodes_process();  // process the returned broadcast
  
  // sending to coordinator = 0x0000
  nodes_send(nodes_lookup(0x0000), 3, 0x10, 0x20, 0x30);
  nodes_process();
  _delay_ms(200L);
  nodes_process();
  
  if( ! handler0 || ! handler1 ) {
    printf("FAIL: one or more payload handler was not executed as expected.\n");
    result = FALSE;
  }
}

void init(void);
void deinit(void);

int main(void) {
  
  init();
  
  printf("\n*** performing all tests for moose implementation of foo-lib...\n");

  test_time();
  test_nodes();

  if(result) {
    printf("*** SUCCESS\n");
  } else {
    printf("*** FAILURE\n");
  }

  deinit();
  
  while(TRUE);  // loop until eternity
  return 0;     // not gonna happen ;-)
}

void init(void) {
  avr_init();                     // initialise MCU
  avr_set_bit(STATUS_LED_PORT,    // turn on the green status led
              STATUS_LED_PIN);

  clock_init();                   // init/start the millis clock

  serial_init();                  // initialize use of serial port(s)
}

void deinit(void) {
  avr_clear_bit(STATUS_LED_PORT,  // turn off the green status led
                STATUS_LED_PIN);
}
