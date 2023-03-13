#include<iostream>
#define MAX 10001

int arr[MAX][3] = { 0 };

using namespace std;

int main()
{
	int n,k;
	cin >> n;

	cin >> arr[1][0];
	arr[1][1] = arr[1][0];
	if (n >= 2) {
		cin >> arr[2][0];
		arr[2][1] = arr[2][0];
		arr[2][0] += arr[1][0];
	}
	for (int i = 3; i <= n; i++)
	{
		cin >> k;
		arr[i][0] += k + max(arr[i - 1][1], arr[i - 1][2]);
		arr[i][1] = k + max(arr[i - 2][2], max(arr[i - 2][0], arr[i - 2][1]));
		arr[i][2] = k + max(arr[i - 3][2], max(arr[i - 3][0], arr[i - 3][1]));
	}
	cout << max(max(arr[n][0], arr[n][1]), max(arr[n][2], arr[n-1][0]));

}
