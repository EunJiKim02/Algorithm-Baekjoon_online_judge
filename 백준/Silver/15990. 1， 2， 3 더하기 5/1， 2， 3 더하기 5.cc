#include<iostream>
#define MAX 100002
#define MOD 1000000009

using namespace std;

int arr[MAX][4] = { 0 };

int main()
{
	int n;
	int t;
	cin >> t;

	//initialize
	arr[1][1] = 1; arr[1][2] = 0; arr[1][3] = 0; // 1
	arr[2][1] = 0; arr[2][2] = 1; arr[2][3] = 0; // 2
	arr[3][1] = 1; arr[3][2] = 1; arr[3][3] = 1; // 21 12 3

	for (int i = 4; i < MAX; i++)
	{
		arr[i][1] = (arr[i - 1][2] + arr[i - 1][3])%MOD;
		arr[i][2] = (arr[i - 2][1] + arr[i - 2][3])%MOD;
		arr[i][3] = (arr[i - 3][1] + arr[i - 3][2])%MOD;
	}

	for (int i = 0; i < t; i++)
	{
		cin >> n;
		//n = i;
		//cout << "n : " << n << '\n';
		//cout << arr[n][1] << ' ' << arr[n][2] << ' ' << arr[n][3] << '\n';
		cout << ((arr[n][1] % MOD + arr[n][2] % MOD) % MOD + arr[n][3]) % MOD << "\n";
	}

}