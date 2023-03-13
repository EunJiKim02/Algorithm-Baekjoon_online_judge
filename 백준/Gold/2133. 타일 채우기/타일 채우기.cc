#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	long long arr[31] = { 0 };
	arr[2] = 3;
	for (int i = 3; i <= n; i++)
	{
		if (i % 2 != 0)
			continue;
		for (int j = i - 2; j >= 2; j -= 2)
		{
			if (j == i - 2)
				arr[i] += arr[j] * 3;
			else
				arr[i] += arr[j] * 2;
		}
		arr[i] += 2;
	}
	
	cout << arr[n] << '\n';
}