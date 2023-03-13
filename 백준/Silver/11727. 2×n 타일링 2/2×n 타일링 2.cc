#include<iostream>
#define MAX 1001

using namespace std;

int fibo[MAX] = { 0 };

int main()
{
	int n;
	cin >> n;
	
	fibo[0] = 1;
	fibo[1] = 1;

	for (int i = 2; i <= n; i++)
	{
		fibo[i] = (fibo[i - 1] + 2 *fibo[i - 2]) %10007;
	}
	cout << fibo[n] << '\n';

	return 0;
}