#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	int* arr = (int*)calloc(sizeof(int), (n + 1));

	arr[1] = 1;
	for (int i = 2; i <= n; i++)
	{
		arr[i] = i;
		for (int j = 1; j * j <= i; j++)
		{
			if (arr[i] > arr[i - (j * j)])
				arr[i] = arr[i - (j * j)] + 1;
		}
	}

	cout << arr[n] << '\n';

}