// CppCollectionsTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <array>
#include <list>
#include <deque>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

namespace petetest {

	int do_something(int const val)
	{
		return val * 2;
	}

	void dump_container(std::_Container_base& container)
	{
		printf("Container is \n");
	}
}



int main()
{
	std::array<int, 10> my_array;

	my_array[0] = 32;
	printf("array size is %u\n", my_array.size());

	std::list<int> my_list;
	std::list<int>::iterator my_iter = my_list.begin();
	
	my_list.insert(my_iter, 2);
	my_list.push_back(82);
	printf("list size is %u\n", my_list.size());

	std::queue<int> my_queue;
	std::vector<int> my_vector;
	stack<int> my_stack;

	my_queue.push(42);
	my_queue.push(55);
	//petetest::dump_container(my_queue);

	my_vector.push_back(100);
	my_vector.push_back(200);

	my_stack.push(petetest::do_something(1234));
	my_stack.push(petetest::do_something(5678));
	my_stack.pop();

	int* ptr = nullptr;

    return 0;
}

