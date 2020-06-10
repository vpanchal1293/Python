from ctypes import *

dll_path = r'..\Dll_learn\c_dll\Debug\c_dll.dll'
dll=cdll.LoadLibrary(dll_path)
from __builtin__ import int
from _ctypes import Structure

'''
res = void
arg = void 
'''
dll.void_void()

'''
res = int
arg = void 
'''
dll.int_void.restype = c_int
ret_int = dll.int_void()
print("Hello",ret_int)

'''
res = void 
arg = int
'''
dll.void_int.argtypes = [c_int]
dll.void_int(10)

'''
Same for all 
c_bool    _Bool    bool (1)
c_char    char    1-character bytes object
c_wchar    wchar_t    1-character string
c_byte    char    int
c_ubyte    unsigned char    int
c_short    short    int
c_ushort    unsigned short    int
c_int    int    int
c_uint    unsigned int    int
c_long    long    int
c_ulong    unsigned long    int
c_longlong    __int64 or long long    int
c_ulonglong    unsigned __int64 or unsigned long long    int
c_size_t    size_t    int
c_ssize_t    ssize_t or Py_ssize_t    int
c_float    float    float
c_double    double    float
c_longdouble    long double    float
'''

'''
Access Print variable
'''
int_var = c_int.in_dll(dll,'int_val')
print(int_var.value)
int_var.value = 20
print(int_var.value)

'''
res = void 
arg = int *
'''
dll.void_intptr.argtypes = [POINTER(c_int)]
int_location = pointer(c_int())
print('content of pointed val',int_location.contents)
dll.void_intptr(int_location)
print(int_location.contents.value)

'''
other mathod
res = void 
arg = int *
'''
int_location = c_int(10)
dll.void_intptr(byref(int_location))
print(int_location.value)

'''
arg = array of any datatype(int array[10],)
res = void
'''
int_array_declar = c_int * 10
print(int_array_declar)
int_array_def = int_array_declar(00,10,20,30,40,50,60,70,80,90)
print(int_array_def)
print("Print in python")
for i in int_array_def:
    print(i)
print("End of Print in python")

dll.void_intarray.argtypes = [int_array_declar]
#dll.void_intarray.argtypes = [POINTER(c_int)]
dll.void_intarray(int_array_def)

'''
arg = array of any datatype(int array[10],) modified in c
res = void
'''
int_array_declar = c_int * 10
print(int_array_declar)
int_array_def = int_array_declar(00,10,20,30,40,50,60,70,80,90)
print(int_array_def)
print("Print in python")
for i in int_array_def:
    print(i)
print("End of Print in python")

dll.void_intarray_modification.argtypes = [int_array_declar]
dll.void_intarray_modification(int_array_def)
print("Modified in c")
for i in int_array_def:
    print(i)
print("End of Modified in c")

'''
arg = char pointer (constant)
res = void
'''
str_python = "Hello String"
str_ctype = c_char_p(str_python)
dll.void_charptr.argtypes = [c_char_p]
dll.void_charptr(str_ctype)

'''
arg = char pointer modified
res = void
'''
char_array_declar = c_char * 10
print(char_array_declar)
char_array_def = char_array_declar('H','e','l','l','o')
print(char_array_def)
dll.void_chararray.argtypes = [c_char_p]
dll.void_chararray(char_array_def)
print("In Python",char_array_def.value)

'''
arg = char pointer modified
res = void
other mathod
'''
char_array_def = create_string_buffer("hello")
print(char_array_def)
dll.void_chararray.argtypes = [c_char_p]
dll.void_chararray(char_array_def)
print("In Python using create_string_buffer",char_array_def.value)

'''
Structure
typedef struct point
{
    int x;
    int y;
}Point;
'''
class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]

print(POINT)
point = POINT(10,20)
print(point)
dll.void_struc.argtypes = [POINT]
dll.void_struc(point)

'''
arg = void
res = char pointer
char *
'''

dll.charptr_void.restype = c_char_p
ret_str = dll.charptr_void()
print(ret_str)

