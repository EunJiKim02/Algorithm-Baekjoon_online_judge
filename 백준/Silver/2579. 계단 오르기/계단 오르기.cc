#include<iostream>
#define MAX 301

int arr[MAX][2] = { 0 };
// arr[x][0] : 한 칸 올라옴
// arr[x][1] : 두 칸 올라옴

using namespace std;

int main()
{
	int n;
	cin >> n;
	
	cin >> arr[1][0];
	if (n >= 2) {
		cin >> arr[2][0];
		arr[2][1] = arr[2][0];
		arr[2][0] += arr[1][0];
	}
	for (int i = 3; i <= n; i++)
	{
		cin >> arr[i][0];
		arr[i][1] = arr[i][0] + max(arr[i-2][0], arr[i-2][1]);
		arr[i][0] += arr[i - 1][1];
	}
	cout << max(arr[n][0], arr[n][1]);

}
