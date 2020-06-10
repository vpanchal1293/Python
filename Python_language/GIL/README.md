What is GIL?
-It is Global Interpreter lock.
-Allows only one thread run at a time
-So in python we cannot achieve multithreading because of GIL

What problem GIL solve?
-Understanding of Garbage Collection
-When reference count reaches to zero it will memory will be released.
-If in multithreaded condition multiple thread will access same object.
-So reference count variable needs to be protected otherwise memory leak will occur.
-If every object will have separate lock then deadlock may occur and overhead on performance.
-So in python only one lock Global lock will used which lock the interpreter 
-Due to this one lock mechanism increase the performance of single threaded application.
-Because of only one lock handling is better than multiple lock.

Why was the GIL chosen as the solution?
-lot of extensions were being written for the existing C libraries 
-These C extensions required a thread-safe memory management which the GIL provided

Impact on Multi-threaded Applications
-There are two types of Applications I/O bound , CPU bound
-In CPU bound Applications multithreaded app will take more time than single thread
-Because of pre-emptive scheduling(thread is forced to leave CPU)
-In I/O bound Applications GIL will not affect much.
-Because of cooperative scheduling(thread will leave CPU for waiting I/O event)
