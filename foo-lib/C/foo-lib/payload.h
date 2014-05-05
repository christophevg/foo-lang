// payload
// payload related functions
// author: Christophe VG

#ifndef _FOO_PAYLOAD
#define _FOO_PAYLOAD

#include <stdarg.h>
#include <stdint.h>

#include "bool.h"

// PAYLOAD

typedef struct payload_t {
  uint8_t* bytes;
  uint16_t size;
} payload_t;

payload_t* make_payload(uint8_t* bytes, int size);

payload_t* copy_payload(payload_t* source);

void free_payload(payload_t* payload);

bool equal_payload(payload_t* pl1, payload_t* pl2);

bool payload_contains(payload_t* payload, int num, ...);

#endif
