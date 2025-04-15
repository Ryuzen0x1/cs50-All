# Learning Language C

The initial code block a `hello` program in C looks like this:

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n")
}
```

Then compile the source code using `make hello` command. The extension is automatically detected in C. Run the code with this `./hello`, just like running a `bash` script

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

It's a scary looking error. If you dont include a header file your source code doesn't get access to libraries, some codes that someone else wrote for you to use as base. CS50 has a user-friendly version of the [man-pages](https://manual.cs50.io/) for ***C*** header files to learn accordingly. As it is slightly complicated to get user inputs in ***C*** we will use `cs50.h` header file also to get basic inputs.

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("Hello, %s\n", answer);
}
```

- As ***C*** is a fairly low level programming language we have to specify the type (`string`, `int`, etc) of variable we are going to use.
- The `%s` is a placeholder to be replaced by the value of the variable, which is the input from user.