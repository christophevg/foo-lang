// time.h
// time related functions
// author: Christophe VG

#ifndef _FOO_TIME
#define _FOO_TIME

#ifndef time_t
#define time_t unsigned long
#endif

time_t now(void);

/*
 * Time related functions are platform specific. A platform implementation needs
 * to provide the implementation for the signature defined above.
 * e.g. see moose/time.c
 */

#endif
