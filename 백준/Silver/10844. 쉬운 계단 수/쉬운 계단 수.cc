#include<iostream>
#define MAX 101
#define MOD 1000000000
using namespace std;

int stairnumber[MAX][10] = { 0 };

int main()
{
	int n;
	int ans = 0;
	cin >> n;

	stairnumber[1][1] = 1; stairnumber[1][2] = 1; stairnumber[1][3] = 1;
	stairnumber[1][4] = 1; stairnumber[1][5] = 1; stairnumber[1][6] = 1;
	stairnumber[1][7] = 1; stairnumber[1][8] = 1; stairnumber[1][9] = 1;

	for (int i = 2; i < MAX; i++)
	{
		stairnumber[i][0] = stairnumber[i - 1][1] % MOD;
		stairnumber[i][9] = stairnumber[i - 1][8] % MOD;
		for (int j = 1; j <= 8; j++)
			stairnumber[i][j] = stairnumber[i - 1][j - 1] % MOD + stairnumber[i - 1][j + 1] % MOD;
	}

	for (int i = 0; i < 10; i++)
	{
		ans  = (ans += (stairnumber[n][i] % MOD)) % MOD;
	}
	cout << ans << '\n';
	return 0;
}