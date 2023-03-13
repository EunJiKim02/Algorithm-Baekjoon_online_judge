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

int main()
{
	int arr[100] = { 0 };
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int number;
		cin >> number;
		long long sum = 0;
		for (int j = 0; j < number; j++)
			cin >> arr[j];
		for (int j = 0; j < number - 1; j++)
		{
			for(int k = j+1; k < number; k++)
				sum += (arr[j] > arr[k]) ? gcd(arr[j], arr[k]) : gcd(arr[k], arr[j]);
		}
		cout << sum << '\n';
	}
	return 0;
}