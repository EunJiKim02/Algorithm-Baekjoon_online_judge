#include<iostream>

using namespace std;

int fibo1count = 1;
int fibo2count = 0;

int fibo1(int n)
{
	if (n == 1 || n == 2) 
		return 1;
	fibo1count++;
	return fibo1(n - 1) + fibo1(n - 2);
}

int fibosave[41] = { 0 };

int fibo2(int n)
{
	fibosave[1] = 1;
	fibosave[2] = 1;

	for (int i = 3; i <= n; i++) {
		fibosave[i] = fibosave[i - 1] + fibosave[i - 2];
		fibo2count++;
	}
	return fibosave[n];
}

int main()
{
	int num;
	cin >> num;
	fibo1(num);
	fibo2(num);
	cout << fibo1count << " " << fibo2count << "\n";
	return 0;
}