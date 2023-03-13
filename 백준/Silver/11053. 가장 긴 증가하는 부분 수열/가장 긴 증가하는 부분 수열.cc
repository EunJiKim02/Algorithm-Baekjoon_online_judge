#include<iostream>

using namespace std;

int* length;
int* arr;

int main()
{
	int n;
	cin >> n;
	length = (int*)calloc(sizeof(int), (n + 1));

	arr = (int*)calloc(sizeof(int), (n + 1));

	for (int i = 1; i <= n; i++)
		cin >> arr[i];


	for (int i = 1; i <= n; i++)
	{
		int maxlen = 0;
		for (int j = 1; j < n; j++)
		{
			if (arr[i] > arr[j] && maxlen < length[j])
				maxlen = length[j];
		}
		length[i] = maxlen + 1;
	}

	int longest = 1;
	for (int i = 1; i <= n; i++)
	{
		if (length[i] > longest)
			longest = length[i];
	}

	cout << longest << '\n';

}