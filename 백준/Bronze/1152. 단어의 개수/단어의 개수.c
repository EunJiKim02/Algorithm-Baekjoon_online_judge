#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
#define SIZE 1000000

int main()
{
	int i;
	int cnt = 1;
	char str[SIZE] = { 0 };
	gets(str);
	int len = strlen(str);
	if ((len == 1) && (str[0] == ' '))
		cnt--;

	for (i = 0; i < len; i++)
	{
		if (str[i] == ' ' && (i != 0 && i != len - 1))
			cnt++;
	}

	printf("%d", cnt);

}