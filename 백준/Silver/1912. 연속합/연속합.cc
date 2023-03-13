#include<iostream>

using namespace std;

int main()
{
	int n;
	int max = -20000;
	int* arr;
	int* sum;
	cin >> n;
	arr = (int*)calloc(sizeof(int), n);
	sum = (int*)calloc(sizeof(int), n);
	cin >> arr[0];
	for (int i = 1; i < n; i++) {
		cin >> arr[i];
		if (arr[i - 1] > 0)
			arr[i] = arr[i] + arr[i - 1];
	}
	
	for (int i = 0; i < n; i++)
	{
		if (arr[i] > max)
			max = arr[i];
	}
	cout << max << '\n';

}