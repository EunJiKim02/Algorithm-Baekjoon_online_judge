#include<iostream>
#include<math.h>
#define MAX 1000000
using namespace std;

bool notprime[MAX] = { false };

// false : prime
// true : not prime

int main()
{
	int m, n;
	int r;
	cin >> m >> n;
	r = sqrt(n);

	notprime[1] = true;

	for (int i = 2; i <= r; i++)
	{
		if (notprime[i] == false)
		{
			for (int j = 2 * i; j <= n; j += i)
				notprime[j] = true;
		}
	}

	for (int i = m; i <= n; i++)
	{
		if (notprime[i] == false)
			cout << i << '\n';
	}

}