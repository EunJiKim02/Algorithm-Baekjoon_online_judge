#include<iostream>
#define MAX 1001

long long arr[MAX] = { 0 };

int main()
{
	int n;
	std::cin >> n;
	arr[1] = 1;
	arr[2] = 2;
	for (int i = 3; i <= n; i++)
		arr[i] = (arr[i - 1] + arr[i - 2])%10007;
	printf("%lld", arr[n]);
}