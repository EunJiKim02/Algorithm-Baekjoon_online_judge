#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int fivenumber = 0;
	int twonumber = 0;
	for (int i = 1; i <= n; i++)
	{
		if (i % 5 == 0)
		{
			int k = 5;
			do 
			{
				fivenumber++;
				k = k * 5;
			}while( i % k == 0);
		}
	}
	cout << fivenumber << '\n';
}