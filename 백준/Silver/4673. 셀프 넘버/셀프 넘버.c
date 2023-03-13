#include<stdio.h>
#pragma warning(disable:4996)
#define SIZE 10000

int returnsum(int x)
{
	if (x < 10)
		return x;
	return (x%10) + returnsum((x/10));
}

int main()
{
	short arr[SIZE] = { 0 };
	int num = 0;
	for (int i = 1; i < SIZE; i++)
	{
		num = returnsum(i) + i;
		//printf("%d:%d\n", i, num);
		if(num<10000)
			arr[num] = 1;
	}

	for (int i = 1; i < SIZE; i++)
	{
		if (arr[i] == 0)
			printf("%d\n", i);
	}
	return 0;
}
