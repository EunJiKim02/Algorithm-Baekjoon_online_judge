
#include<iostream>
#include<math.h>
#include<vector>
#define MAX 1000001
using namespace std;

bool notprime[MAX] = { false };
// false : prime
// true : not prime

void getprime();
void get_goldbachnumber(int);


int main()
{

	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int  num;
	getprime();

	while (1)
	{
		cin >> num;
		if (num == 0)
			break;
		get_goldbachnumber(num);
	}
}

void getprime()
{
	int r;
	r = sqrt(MAX);

	notprime[1] = true;

	for (int i = 2; i <= r; i++)
	{
		if (notprime[i] == false)
		{
			for (int j = 2 * i; j <= MAX; j += i) {
				notprime[j] = true;
			}
		}
	}

}

void get_goldbachnumber(int n)
{
	int ans = 0;
	for (int i = 2; i <= n / 2; i++) {
		if ((notprime[i] == false) && (notprime[n - i] == false)) {
			printf("%d = %d + %d\n", n, i, (n - i));
			break;
		}
	}
}