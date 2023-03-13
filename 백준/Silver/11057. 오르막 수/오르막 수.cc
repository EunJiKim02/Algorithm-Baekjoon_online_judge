#include<iostream>
#define MOD 10007

using namespace std;

int main()
{
	int* arr[10];
	int n;
	cin >> n;
	for (int i = 0; i < 10; i++)
		arr[i] = (int*)calloc(sizeof(int), n);
	for (int i = 0; i < 10; i++)
		arr[i][0] = 1;

	for (int i = 1; i < n; i++)
	{
		arr[0][i] = arr[0][i - 1] % MOD;
		arr[1][i] = arr[1][i - 1] % MOD + arr[0][i] % MOD;
		arr[2][i] = arr[2][i - 1] % MOD + arr[1][i] % MOD;
		arr[3][i] = arr[3][i - 1] % MOD + arr[2][i] % MOD;
		arr[4][i] = arr[4][i - 1] % MOD + arr[3][i] % MOD;
		arr[5][i] = arr[5][i - 1] % MOD + arr[4][i] % MOD;
		arr[6][i] = arr[6][i - 1] % MOD + arr[5][i] % MOD;
		arr[7][i] = arr[7][i - 1] % MOD + arr[6][i] % MOD;
		arr[8][i] = arr[8][i - 1] % MOD + arr[7][i] % MOD;
		arr[9][i] = arr[9][i - 1] % MOD + arr[8][i] % MOD;
	}

	int ans = 0;
	for (int i = 0; i < 10; i++)
		ans += arr[i][n - 1];
	cout << ans%MOD << '\n';

}