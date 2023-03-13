#include<iostream>

using namespace std;

int main(void)
{
	int n, k, tmp;
	int* arr;
	int* sum;
	cin >> n;
	arr = (int*)calloc(sizeof(int), (n+1));
	sum = (int*)calloc(sizeof(int), (n + 1));
	cin >> sum[0];
	arr[0] = sum[0];
	for (int i = 1; i < n; i++)
	{
		for (int j = 0; j <= i; j++)
			cin >> arr[j];		

		sum[i] = sum[i - 1] + arr[i];
		for (int j = i-1; j > 0; j--)
			sum[j] = max(sum[j - 1], sum[j]) + arr[j];
		sum[0] = sum[0] + arr[0];
	}
	int max = sum[0];
	for (int i = 1; i < n; i++)
	{
		if (max < sum[i])
			max = sum[i];
	}
	cout << max << '\n';
}