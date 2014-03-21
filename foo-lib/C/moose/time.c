// time
// time related functions, specific for the moose platform
// author: Christophe VG

#include "../time.h"

#include "moose/clock.h"

// a simple redirection to the underlying moose clock function
time_t now(void) {
  return clock_get_millis();
}

/*
 * WARNING: use of this function requires initialization using clock_init !!!
 */
