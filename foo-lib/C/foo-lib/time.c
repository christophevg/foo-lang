// time
// time related functions, implementation for testing purposes
// author: Christophe VG

#include <sys/time.h>

#include "time.h"

// a simple redirection to the underlying standard gettimeofday functionality
time_t now(void) {
  struct timeval  tp;
  struct timezone tzp = { .tz_minuteswest = 0, .tz_dsttime     = 0 };
  gettimeofday(&tp, &tzp);
  return tp.tv_sec * 1000 + (tp.tv_usec/1000);
}
