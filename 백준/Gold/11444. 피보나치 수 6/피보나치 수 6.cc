#include<iostream>
#define DIV 1000000007
using namespace std;

long long** arr;

long long** matrix_mul(int n, long long** m, long long** y)
{
	int temp[5][5] = { 0 };

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				temp[i][j] = ((temp[i][j] % DIV)+ ((m[i][k] * y[k][j]) % DIV)) %DIV;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			m[i][j] = temp[i][j] % DIV;
		}
	}
	return m;
}

long long** matrix_power(long long* a[5], long long b, int n) {
	if (b == 1)
		return a;
	else {
		long long** temp = matrix_power(a, b / 2, n);
		if (b % 2 == 0)
			return matrix_mul(n, temp, temp);
		else
			return matrix_mul(n, matrix_mul(n, temp, temp), arr);
	}
}


int main()
{
	long long b;
	int n = 2;
	long long** mp;
	long long** result;

	cin >> b;
	mp = (long long**)calloc(sizeof(long long*), n);
	for (int i = 0; i < n; i++)
		mp[i] = (long long*)calloc(sizeof(long long), n);
	arr = (long long**)calloc(sizeof(long long*), n);
	for (int i = 0; i < n; i++)
		arr[i] = (long long*)calloc(sizeof(long long), n);
	
	mp[0][0] = 0;
	mp[0][1] = 1;
	mp[1][0] = 1;
	mp[1][1] = 1;
	arr[0][0] = 0;
	arr[0][1] = 1;
	arr[1][0] = 1;
	arr[1][1] = 1;


	result = matrix_power(mp, b, n);


	cout << (result[0][1] % DIV) << ' ';
	return 0;
}