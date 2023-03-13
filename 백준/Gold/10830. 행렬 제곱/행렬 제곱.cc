#include<iostream>
#define DIV 1000
using namespace std;

int ** arr;

int ** matrix_mul(int n, int **m, int **y)
{
	int temp[5][5] = { 0 };

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				temp[i][j] += ((m[i][k] * y[k][j]) % DIV);
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

int** matrix_power(int *a[5], long long b, int n){
	if (b == 1)
		return a;
	else {
		int** temp = matrix_power(a, b / 2, n);
		if (b % 2 == 0)
			return matrix_mul(n, temp ,temp);
		else
			return matrix_mul(n, matrix_mul(n, temp, temp), arr);
	}
}


int main()
{
	long long b;
	int n;
	int** mp;
	int** result;

	cin >> n >> b;
	mp = (int**)calloc(sizeof(int*), n);
	for (int i = 0; i < n; i++)
		mp[i] = (int*)calloc(sizeof(int), n);
	arr = (int**)calloc(sizeof(int*), n);
	for (int i = 0; i < n; i++)
		arr[i] = (int*)calloc(sizeof(int), n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> mp[i][j];
			arr[i][j] = mp[i][j]%DIV;
			mp[i][j] %= DIV;
		}
	}
	result = matrix_power(mp, b, n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << mp[i][j] % DIV << ' ';
		}
		cout << '\n';
	}
	return 0;
}