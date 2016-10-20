#pragma once

#define UNUSED(v)			(v) = (v)
#define UNUSED_CONST(t, c)	{ t new_##c = c; new_##c = new_##c; }

typedef unsigned long uint32_t;

typedef struct
{
	uint32_t val1;
	uint32_t val2;

} TEST_DATA_T;

// Returns the summed square of both numbers
extern uint32_t do_something(TEST_DATA_T * const data);
