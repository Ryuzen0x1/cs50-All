#include <cs50.h>
#include <stdio.h>

// Is this how you write a comment?

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("Hello, %s\n", answer);
}
