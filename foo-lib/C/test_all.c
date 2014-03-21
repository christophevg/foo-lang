// test
// tests all foo-lib/C modules
// author: Christophe VG

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#include "crypto.h"
#include "time.h"

void test_crypto(void) {
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

int main(void) {

  printf("*** performing all tests for foo-lib...\n");
  test_crypto();
  printf("*** SUCCESS\n");
  
  exit(EXIT_SUCCESS);
}
