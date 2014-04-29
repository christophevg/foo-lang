// crypto
// cryptography related function calls
// author: Christophe VG

#ifndef _FOO_CRYPTO
#define _FOO_CRYPTO

#include <stdarg.h>
#include <stdint.h>

#include "bool.h"

// reusing the very nice implementation by Matt Mahoney
#include "sha1.h"

uint8_t* sha1(int, ...);
bool sha1_compare(uint8_t[20], int, ...);

#endif
