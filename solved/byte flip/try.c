#include<stdio.h>
#include<stdlib.h>

int main(){
    char a;
    char* b;
    b= &a;
    printf("indirizzo di a: %p", b);
    printf("indirizzo di a: %p", *b);
    return 0;
}

