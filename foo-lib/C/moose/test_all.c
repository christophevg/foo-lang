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

#define STATUS_LED_PORT    PORTB  // PB0
#define STATUS_LED_PIN     0


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
    }
    _delay_ms(10L);
  }
}

void init(void);
void deinit(void);

int main(void) {
  
  init();
  
  printf("\n*** performing all tests for moose implementation of foo-lib...\n");

  test_time();

  printf("*** SUCCESS\n");

  deinit();
  
  while(TRUE);
  
  return 0;
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
