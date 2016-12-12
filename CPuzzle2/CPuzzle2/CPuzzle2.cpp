/* A program to accept a C char* string (or a ulong), that will print
   the offsets of runs of 0's and 1's, where the runs are longer than 1.
   For example, if given "0010011" it will print "0, 3, 5".
*/

#include <stdio.h>
#include <string.h>

// Prints the offsets of runs of the same character in the supplied string.
void print_offsets(char * const string_to_test)
{
	int end = strlen(string_to_test);
	int pos;

	bool found_match = false;

	for (pos = 1; pos < end; pos++)
	{
		bool match = (string_to_test[pos] == string_to_test[pos - 1]);

		if (!found_match && match)
		{
			// The character at pos matches the previous character, but 
			// not the one before that
			printf("%u, ", pos - 1);
		}

		found_match = match;
	}

	printf("\n");
}

int main(int const argc, char * const argv[])
{
	if (argc > 1)
	{
		printf("String to test is %s\n", argv[1]);
		print_offsets(argv[1]);
	}

	return 0;
}

