#include<iostream>
#define MAX 1000001
#define MOD 1000000009

using namespace std;

long long arr[MAX] = { 0 };

int main()
{
	int n;
	int t;
	cin >> t;

	arr[1] = 1;
	arr[2] = 2;
	arr[3] = arr[1] + arr[2] + 1;

	for (int i = 4; i < MAX; i++)
		arr[i] = arr[i - 1]%MOD + arr[i - 2]%MOD + arr[i - 3]%MOD;

	for (int i = 0; i < t; i++)
	{
		cin >> n;
		cout << arr[n]%MOD << '\n';
	}

}