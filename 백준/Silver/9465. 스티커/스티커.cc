#include<iostream>
#define MOD 9901
using namespace std;

int arr[3][100001] = { 0 };
int cost[2][100001] = { 0 };

int main()
{
	int n;
	cin >> n;
	for (int m = 0; m < n; m++)
	{
		int r;
		cin >> r; //2 by r
		
		//input
		for (int i = 0; i < 2; i++)
		{
			for (int j = 1; j <= r; j++)
				cin >> cost[i][j];
		}
		arr[0][1] = 0; arr[1][1] = cost[0][1]; arr[2][1] = cost[1][1];
		//calculate
		for (int i = 2; i <= r; i++)
		{
			arr[0][i] = max(arr[0][i - 1], max( arr[1][i - 1] , arr[2][i - 1])) + 0;
			arr[1][i] = max(arr[0][i - 1] ,arr[2][i - 1]) + cost[0][i] ;
			arr[2][i] = max(arr[0][i - 1], arr[1][i - 1]) + cost[1][i];
		}
		cout << max(arr[0][n] ,max( arr[1][r] , arr[2][r]))  << '\n';
	}
}