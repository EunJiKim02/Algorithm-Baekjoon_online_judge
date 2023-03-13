#include<iostream>
#define MOD 1000000000
#define MAX 401

using namespace std;

int main()
{
	int m, k;
	cin >> m >> k;

	int n, r;
	int arr[401] = { 0 };

	n = (m + k) - 1;
	r = k - 1;

	if (r > (n / 2))
		r = (n - r);

	arr[0] = 1; arr[1] = 1;
	for (int i = 2; i <= n; i++)
	{
		for (int j = i; j >= 0; j--)
		{
			if (j == i)
				arr[j] = 1;
			else if (j == 0)
				arr[j] = 1;
			else
				arr[j] = arr[j] % MOD + arr[j - 1] % MOD;
		}

	}
	cout << arr[r] % MOD << '\n';


}
