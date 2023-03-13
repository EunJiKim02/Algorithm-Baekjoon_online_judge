#include<iostream>
#define MOD 9901
using namespace std;

int main()
{
	int n;
	cin >> n;
	long long* arr[3];
	for (int i = 0; i < 3; i++)
		arr[i] = (long long*)calloc(sizeof(long long), n+1);

	arr[0][1] = 1; arr[1][1] = 1; arr[2][1] = 1;

	for (int i = 2; i <= n; i++)
	{
		arr[0][i] = arr[0][i - 1] % MOD + arr[1][i - 1] % MOD + arr[2][i - 1] % MOD;
		arr[1][i] = arr[0][i - 1] % MOD + arr[2][i - 1] % MOD;
		arr[2][i] = arr[0][i - 1] % MOD + arr[1][i - 1] % MOD;
	}
	cout << (arr[0][n] + arr[1][n] + arr[2][n]) % MOD;

}