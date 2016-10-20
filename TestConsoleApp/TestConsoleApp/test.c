#include "test_header.h"

/* Returns the summed-square of the supplied data values
*/
uint32_t do_something(TEST_DATA_T * const p_this)
{
	return (p_this->val1 * p_this->val1) + (p_this->val2 * p_this->val2);
}
