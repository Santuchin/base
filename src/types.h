#include <stdbool.h>

typedef struct
{
	void* ptr; // pointer to the start of the array
	size_t len; // count of items
	size_t size; // size in bytes of every item in the array
	// you can get the size in memory of array with array.size * array.len
}
array;

typedef struct
{
}
natural;


