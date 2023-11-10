#include<stdio.h>
#include <string.h>

int main(void) {

    char sss[101];
    scanf("%s", sss);

    int alpha[26] = { 0 };

    for (int i = 0; i < strlen(sss); i++) {
        int index = sss[i] - 'a';
        if (alpha[index] != 0)
            continue;
        alpha[index] = i + 1;
    }

    for (int i = 0; i < 26; i++)
        printf("%d ", alpha[i] - 1);

    return 0;
}