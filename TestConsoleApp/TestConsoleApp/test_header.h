#pragma once

#define UNUSED(v)			(v) = (v)
#define UNUSED_CONST(t, c)	(t) new_v = (c)

typedef unsigned long uint32_t;

extern uint32_t do_something(uint32_t const val);
