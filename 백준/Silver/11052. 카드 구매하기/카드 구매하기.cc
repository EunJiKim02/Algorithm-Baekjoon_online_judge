#include<iostream>

using namespace std;

int main()
{
	int N;
	int* arr;
	int* ans;
	int max;
	cin >> N;
	arr = (int*)malloc(sizeof(int) * (N+1));

	for (int i = 1; i <= N; i++)
		cin >> arr[i];

	for (int i = 1; i <= N; i++)
	{
		max = 0;
		for (int j = 1; j <= i / 2; j++)
		{
			if ((arr[j] + arr[i - j]) > max)
				max = arr[j] + arr[i - j];
		}
		if (max > arr[i])
			arr[i] = max;
	}
	cout << arr[N] << '\n';

}