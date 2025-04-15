# Learning Language C

The initial code block a `hello` program in C looks like this:

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n")
}
```

Then build the source code using `make hello` command. The extension is automatically detected in C.

## Header files

Any file that end with `.h` extension. It mainly gives the functionality that came with the language or system itself. Removing the `#include <stdio.h>` file will result in an error like this:

```c
hello.c:3:5: error: call to undeclared library function 'printf' with type 'int (const char *, ...)'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
    3 |     printf("Hello, World!\n");
      |     ^
hello.c:3:5: note: include the header <stdio.h> or explicitly provide a declaration for 'printf'
1 error generated.
make: *** [<builtin>: hello] Error 1
```

It's a scary looking error.