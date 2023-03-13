#include<iostream>
#define SIZE 50
#define SWAP(x, y, temp) (temp = x, x = y, y = temp)

using namespace std;

int Max = 0;
int n;
char arr[SIZE][SIZE] = { 0 };

void rowmax(int r)
{
	int check = 1;
	for (int i = 1; i < n; i++)
	{
		if (arr[r][i - 1] == arr[r][i])
			check++;
		else
		{
			if (Max < check)
				Max = check;
			check = 1;
		}
	}
	if (Max < check)
		Max = check;
}

void colmax(int c)
{
	int check = 1;
	for (int i = 1; i < n; i++)
	{
		if (arr[i-1][c] == arr[i][c])
			check++;
		else
		{
			if (Max < check)
				Max = check;
			check = 1;
		}
	}
	if (Max < check)
		Max = check;
}

int main()
{
	cin >> n;
	int temp;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cin >> arr[i][j];
	}
	//change row
	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < n; j++)
		{
			SWAP(arr[i][j - 1], arr[i][j], temp);
			colmax(j - 1);
			colmax(j);
			rowmax(i);
			SWAP(arr[i][j - 1], arr[i][j], temp);
		}
	}

	//change col
	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j < n; j++)
		{
			SWAP(arr[j - 1][i], arr[j][i], temp);
			rowmax(j - 1);
			rowmax(j);
			colmax(i);
			SWAP(arr[j - 1][i], arr[j][i], temp);
		}
	}
	cout << Max << '\n';
}