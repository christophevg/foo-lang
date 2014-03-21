// crypto
// cryptography related function calls
// author: Christophe VG

#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#include "bool.h"
#include "stdarg-collect.h"

#include "crypto.h"
#include "sha1.h"

// Private non-vararg version of sha1
// Accepts size and an array of bytes.
// Returns a pointer to a 20-byte hash.
uint8_t* _sha1(int size, uint8_t* buffer) {
  SHA1Context context;
  SHA1Reset(&context);
  SHA1Input(&context, buffer, size);

  uint8_t* hash = malloc(20 * sizeof(uint8_t));
  if( SHA1Result(&context, hash) != shaSuccess ) { return NULL; }

  return hash;
}

// Computes the SHA-1 hash for a variable amount of bytes. 
// Accepts a single mandatory argument, representing the number of bytes that
// will follow it.
// Returns a pointer to 20 bytes, representing the hash.
uint8_t* sha1(int size, ...) {
  uint8_t* buffer = malloc(size * sizeof(uint8_t));
  va_collect(buffer, size, uint8_t);
  return _sha1(size, buffer);
}

// Compares a given hash of 20 bytes to a freshly computed SHA-1 hash for
// a given number of bytes.
// Accepts a hash of 20 bytes and a second mandatory argument, representing
// the number of bytes that will follow it.
// Returns a boolen indication if the hash matches
bool sha1_compare(uint8_t expected[20], int size, ...) {
  uint8_t* buffer = malloc(size * sizeof(uint8_t));
  va_collect(buffer, size, uint8_t);
  return (memcmp(_sha1(size, buffer), expected, 20) == 0);
}
