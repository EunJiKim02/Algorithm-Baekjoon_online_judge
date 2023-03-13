#include<iostream>

using namespace std;

int main()
{
	// arr[0][k] : R, arr[1][k] : G, arr[2][k] : B
	int* arr[3];
	int* cost[3];
	int n;

	cin >> n;
	for (int i = 0; i < 3; i++) {
		arr[i] = (int*)calloc(sizeof(int), n);
		cost[i] = (int*)calloc(sizeof(int), n);
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < 3; j++)
			cin >> arr[j][i];

	cost[0][0] = arr[0][0];
	cost[1][0] = arr[1][0];
	cost[2][0] = arr[2][0];

	for (int i = 1; i < n; i++)
	{
		cost[0][i] = min(cost[1][i - 1], cost[2][i - 1]) + arr[0][i];
		cost[1][i] = min(cost[0][i - 1], cost[2][i - 1]) + arr[1][i];
		cost[2][i] = min(cost[0][i - 1], cost[1][i - 1]) + arr[2][i];
	}

	cout << min(min(cost[0][n-1], cost[1][n-1]), cost[2][n-1]);

	
}