#include<iostream>

using namespace std;

int gcd(int a, int b) {
	while (b != 0) {
		int t = b;
		b = a % b;
		a = t;
	}
	return a;
}

int lcm(int a, int b)
{
	return (a * b / gcd(a, b));
}

int main()
{
	int a, b;
	cin >> a >> b;
	if (a > b)
	{
		cout << gcd(a, b) << '\n';
		cout << lcm(a, b) << '\n';
	}
	else
	{
		cout << gcd(b,a) << '\n';
		cout << lcm(b,a) << '\n';
	}
}