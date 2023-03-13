#include <iostream>
#include <vector>
#define INF 9999999
#define SIZE 101

using namespace std;

int arr[SIZE][SIZE] = { 0 };

int main(void)
{
	cin.tie(NULL);

	int n, m;
	cin >> n;
	cin >> m;
	int i, j, c;
	for (int k = 0; k < m; k++)
	{
		cin >> i >> j >> c;
		if (arr[i][j] != 0)
			arr[i][j] = min(arr[i][j], c);
		else
			arr[i][j] = c;
	}

	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			if (arr[i][j] == 0 && i != j)
				arr[i][j] = INF;
		}
	}

	for (int k = 1; k <= n; k++){
		for (int i = 1; i <= n; i++){
			for (int j = 1; j <= n; j++)
				arr[i][j] = min(arr[i][j], (arr[i][k] + arr[k][j]));
		}
	}
	for (int i = 1; i <= n; i++){
		for (int j = 1; j <= n; j++){
			if (arr[i][j] == INF)
				cout << 0 << ' ';
			else
				cout << arr[i][j] << ' ';
		}
		cout << '\n';
	}

}