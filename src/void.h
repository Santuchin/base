#include "types.h"

// #define BYTES bytes(range(2 ** 8))
// #define ASCII bytes(range(2 ** 7))

bytes encode(natural number, bytes digits);
natural decode(bytes number, bytes digits);

bool valid(bytes number, bytes digits);
natural length(natural number, natural base);

