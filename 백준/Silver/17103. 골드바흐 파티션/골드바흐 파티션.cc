
#include<iostream>
#include<math.h>
#include<vector>
#define MAX 1000001
using namespace std;

bool notprime[MAX] = { false };
// false : prime
// true : not prime

void getprime();
int get_goldbachnumber(int);
vector<int> prime;


int main()
{

	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int k, num;
	cin >> k;
	getprime();

	for (int i = 0; i < k; i++)
	{
		cin >> num;
		cout << get_goldbachnumber(num) << '\n';
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
	for (int i = 2; i <= MAX; i++)
	{
		if (notprime[i] == false)
			prime.push_back(i);
	}

}

int get_goldbachnumber(int n)
{
	int ans = 0;
	for (int i = 2; i <= n/2; i++) {
		if ((notprime[i] == false) && (notprime[n - i] == false))
			ans++;
	}
	return ans;
}