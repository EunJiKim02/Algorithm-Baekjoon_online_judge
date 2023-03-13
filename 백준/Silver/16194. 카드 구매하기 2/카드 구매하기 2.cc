#include<iostream>

using namespace std;

int main()
{
	int N;
	int* arr;
	int* ans;
	int min;
	cin >> N;
	arr = (int*)malloc(sizeof(int) * (N+1));

	for (int i = 1; i <= N; i++)
		cin >> arr[i];

	for (int i = 1; i <= N; i++)
	{
		min = 999999999;
		for (int j = 1; j <= i / 2; j++)
		{
			if ((arr[j] + arr[i - j]) < min)
				min = arr[j] + arr[i - j];
		}
		if (min < arr[i])
			arr[i] = min;
	}
	cout << arr[N] << '\n';

}