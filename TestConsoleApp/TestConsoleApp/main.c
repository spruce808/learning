#include <stdio.h>

#include "test_header.h"

int main(int argc, char * argv[])
{
	uint32_t val = 42;
	uint32_t val_squared;

	UNUSED(argc);
	UNUSED(argv);
	
	printf("In main\n");


	val_squared = do_something(val);
	printf("Square of %u is %u\n", val, val_squared);
}