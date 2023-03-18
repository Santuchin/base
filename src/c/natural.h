
char* encode(unsigned long long int number, char* digits)
unsigned long long int decode(char* number, char* digits);
size_t length(unsigned long long int, size_t base);
size_t valid(char* digits, char* digits, bool leading);

char* encode_limited(unsigned long long int number, char* digits, size_t len)
{
	char* resp = malloc(len);

	for (size_t index = 0; index < len; len++)
	{
		resp[index] = digits[number % base];
		number /= base;
	}

	return resp;
}

