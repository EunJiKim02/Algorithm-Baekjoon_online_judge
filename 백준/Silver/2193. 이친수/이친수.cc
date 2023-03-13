#include<iostream>
#define MAX 91

using namespace std;

long long pinaryNumber[MAX][2] = { 0 };

int main()
{
	int n; 
	cin >> n;

	pinaryNumber[0][0] = 0; pinaryNumber[0][1] = 1;

	for (int i = 1; i < n; i++)
	{
		pinaryNumber[i][0] = pinaryNumber[i - 1][0] + pinaryNumber[i - 1][1];
		pinaryNumber[i][1] = pinaryNumber[i - 1][0];
	}

	cout << pinaryNumber[n-1][0] + pinaryNumber[n-1][1] << '\n';

}