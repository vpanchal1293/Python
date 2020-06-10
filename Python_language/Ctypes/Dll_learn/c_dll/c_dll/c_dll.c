#include"Header.h"

DLLEXPORT int int_val = 50;

void void_void(void)
{
	ENTER_FUN;
	printf("res_type = void\n");
	printf("arg_type = void\n");
	EXIT_FUN;
}

int int_void(void)
{
	ENTER_FUN;
	printf("res_type = int\n");
	printf("arg_type = void\n");
	EXIT_FUN;
	return 5;
}

void void_int(int i)
{
	ENTER_FUN;
	printf("res_type = int\n");
	printf("arg_type = void\n");
	printf("arg = %d\n", i);
	EXIT_FUN;
}

void void_intptr(int *val)
{
	ENTER_FUN;
	printf("res_type = void\n");
	*val = 20;
	printf("arg_type = int pointer\n");
	EXIT_FUN;
}

void void_intarray(int *val)
{
	ENTER_FUN;
	printf("res_type = void\n");
	int loop_cnt = 0;
	for (loop_cnt = 0; loop_cnt < 9; loop_cnt++)
	
		printf("%d\n",val[loop_cnt]);
	printf("arg_type = array of int\n");
	EXIT_FUN;
}

void void_intarray_modification(int *val)
{
	ENTER_FUN;
	printf("res_type = void\n");
	int loop_cnt = 0;
	for (loop_cnt = 0; loop_cnt < 9; loop_cnt++)
		val[loop_cnt] = (loop_cnt * 5 );
	printf("arg_type = array of int modified\n");
	EXIT_FUN;
}

void void_charptr(char *ptr)
{
	ENTER_FUN;
	printf("res_type = void\n");
	printf("%s\n", ptr);
	printf("arg_type = char pointer(not modified)\n");
	EXIT_FUN;
}

void void_chararray(char *ptr)
{
	ENTER_FUN;
	printf("res_type = void\n");
	printf("Before modification = %s\n", ptr);
	strcpy(ptr, "_HELLO_");
	printf("After modification = %s\n", ptr);
	printf("arg_type = char pointer(not modified)\n");
	EXIT_FUN;
}

void void_struc(Point p)
{
	ENTER_FUN;
	printf("res_type = void\n");
	printf("x = %d, y = %d\n", p.x, p.y);
	printf("arg_type = Point stuct\n");
	EXIT_FUN;
}

char * charptr_void(void)
{
	ENTER_FUN;
	char *p = "Return Char ptr from c";
	printf("res_type = char *\n");
	printf("arg_type = void\n");
	EXIT_FUN;
	return p;
}