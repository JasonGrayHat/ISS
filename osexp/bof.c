#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int copybuffer(char* input)
{
	char buffer[256];
	strcpy (buffer, input);
	return 0;
}

void main (int argc, char *argv[])
{
	int localvar=1;
	copybuffer(argv[1]);
	exit(0);
}
