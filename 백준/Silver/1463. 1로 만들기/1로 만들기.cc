#include<iostream>
#define MAX 1000000

int arr[MAX] = { 0 };

void makeOne(int n)
{
	int a, b, c;
	arr[1] = 0;
	arr[2] = 1;
	arr[3] = 1;
	for (int i = 4; i <= n; i++)
	{
		a = MAX, b = MAX, c = MAX;
		if (i % 2 == 0)
			a = arr[i / 2];
		if (i % 3 == 0)
			b = arr[i / 3];
		c = arr[i - 1];
		if (a > b)
		{
			if (b > c)
				arr[i] = c;
			else
				arr[i] = b;
		}
		else
		{
			if (a > c)
				arr[i] = c;
			else
				arr[i] = a;
		}
		arr[i] += 1;
	}
}

int main()
{
	int n;
	std:: cin >> n;

	makeOne(n);
	printf("%d", arr[n]);

}