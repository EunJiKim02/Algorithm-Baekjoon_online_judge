#include<iostream>

using namespace std;


int main()
{
	int n;
	int maxindex;
	cin >> n;
	int* arr = (int*)calloc(sizeof(int), n+1);
	int* a = (int*)calloc(sizeof(int), n+1);
	int* aRev = (int*)calloc(sizeof(int), n+1);

	for (int i = 1; i <= n; i++)
		cin >> arr[i];
	a[1] = 1;
	for (int i = 2; i <= n; i++) {
		maxindex = 0;
		for (int j = 1; j < i; j++)
		{
			if ((a[maxindex] < a[j]) && (arr[j] < arr[i]))
				maxindex = j;
		}
		if (maxindex == 0)
			a[i] = 1;
		else
			a[i] = a[maxindex] + 1;
	}

	aRev[n] = 1;
	for (int i = n; i >= 1; i--) {
		maxindex = 0;
		for (int j = n; j > i; j--)
		{
			if ((aRev[maxindex] < aRev[j]) && (arr[j] < arr[i]))
				maxindex = j;
		}
		if (maxindex == 0)
			aRev[i] = 1;
		else
			aRev[i] = aRev[maxindex] + 1;
	}
	maxindex = 0;
	for (int i = 1; i <= n; i++)
	{
		if ((a[maxindex] + aRev[maxindex]) < (a[i] + aRev[i]))
			maxindex = i;
	}
	printf("%d ", aRev[maxindex] + a[maxindex] - 1);
}