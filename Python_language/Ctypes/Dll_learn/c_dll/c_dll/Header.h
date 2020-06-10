#ifndef HEADER_H
#define HEADER_H

#include<stdio.h>
#include<string.h>
#define DLLEXPORT __declspec(dllexport)
#define ENTER_FUN printf("\nEntering in c Function = %s\n", __func__);
#define EXIT_FUN printf("Exiting in c Function = %s\n\n", __func__);

typedef struct point
{
	int x;
	int y;
}Point;
//Only value
DLLEXPORT extern int int_val;

//res = void
//arg = void
DLLEXPORT void void_void(void);

//res = int
//arg = void
DLLEXPORT int int_void(void);

//res = void
//arg = int
DLLEXPORT void void_int(int);

//res = void
//arg = int pointer
DLLEXPORT void void_intptr(int *val);

//res = void
// arg = array of int
DLLEXPORT void void_intarray(int *val);

//res = void
//arg = array of int(modify in c)
DLLEXPORT void void_intarray_modification(int *val);

//res = void
//arg = char string(constant)
DLLEXPORT void void_charptr(char *ptr);

//res = void
//arg = char array(modify)
DLLEXPORT void void_chararray(char *ptr);

//res = void
//arg = strucutre
DLLEXPORT void void_struc(Point p);

//res = char pointer
//arg = void
DLLEXPORT char * charptr_void(void);

#endif
