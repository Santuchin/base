#include "types.h"

#define BINARY "01"
#define OCTAL "01234567"
#define DECIMAL "0123456789"
#define HEXADECIMAL "0123456789abcdef"
#define BASE64 "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

bytes encode(natural number, bytes digits);
natural decode(bytes number, bytes digits);

bool valid(bytes number, bytes digits);
natural length(natural number, natural base);

bytes encode_limited(natural number, bytes digits, natural length);

