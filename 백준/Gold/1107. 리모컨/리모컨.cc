#include<iostream>
#include<math.h>

using namespace std;

int numisIn(int n, int x)
{
	if (n == 0 )
		return 0;
	else
		return ( n % 10 == x ) ? 1 : numisIn( n / 10, x);
}

int getlength(int n)
{
	if (n == 0)
		return 1;
	int count = 0;
	while (n != 0)
	{
		count++;
		n /= 10;
	}
	return count;
}


int main()
{

	int n, m;
	int k;
	int min = 0;
	int i;

	int arr[10] = { 0,1,2,3,4,5,6,7,8,9 };
	cin >> n;
	cin >> m;

	for (int i = 0; i < m; i++)
	{
		cin >> k;
		arr[k] = -1;
	}

	min = abs(100 - n);

	int small = n;
	int big = n;


	if (m == 0)
	{
		if (getlength(n) < min)
			min = getlength(n);
		cout << min << '\n';
		return 0;
	}
	else if (m == 10) {
		cout << min << '\n';
		return 0;
	}
	while (1)
	{
		if (arr[0] == -1 && n == 0 && big == small) {
			big++;
			small--;
		}
		if (small >= 0) {
			for (i = 0; i < 10; i++)
			{
				if (arr[i] == -1 && (numisIn(small, i) == 1))
					break;
				if (arr[i] == -1 && i == 0 && small == 0)
					break;
			}
			if (i == 10)
			{
				if (min > abs(small - n) + getlength(small))
					min = abs(small - n) + getlength(small);
				break;
			}
		}
		if (big <= 1000000)
		{
			for (i = 0; i < 10; i++)
			{
				if (arr[i] == -1 && (numisIn(big, i) == 1))
					break;
				if (arr[i] == -1 && i == 0 &&  big == 0)
					break;
			}
			if (i == 10)
			{
				if (min > abs(big - n) + getlength(big))
					min = abs(big - n) + getlength(big);
				break;
			}
		}

		small--;
		big++;


	}
	
	cout << min << '\n';
}