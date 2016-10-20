#include <stdio.h>

#include "test_header.h"

int main(int const argc, char * argv[])
{
	TEST_DATA_T data;
	uint32_t result;

	UNUSED_CONST(int, argc);
	UNUSED(argv);
	
	printf("In main\n");

	data.val1 = 32;
	data.val2 = 104;

	result = do_something(&data);
	printf("Square of %u is %u\n", data.val1, result);
}