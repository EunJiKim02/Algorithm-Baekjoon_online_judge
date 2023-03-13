#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	unsigned long long length = 0;

	// 1 ~ 9 : += 1
	// 10 ~ 99 : += 2
	// 100 ~ 999 : += 3
	// 1000 ~ 9999 += 4
	// 10000 ~ 99999 += 5
	// 100000 ~ 999999 += 6
	// 1000000 ~ 9999999 += 7
	// 10000000 ~ 99999999 += 8
	// 100000000 += 9
	int ans = 0;
	if (n < 10) {
		ans += (n);
		cout << ans;
		return 0;
	}
	else
		ans += (9) * 1;

	if (n < 100){
		ans += (n - 9) * 2;
		cout << ans;
		return 0;
	}
	else
		ans += (99 - 9) * 2;

	if (n < 1000) {
		ans += (n - 99) * 3;
		cout << ans;
		return 0;
	}
	else
		ans += (999 - 99) * 3;

	if (n < 10000) {
		ans += (n - 999) * 4;
		cout << ans;
		return 0;
	}
	else
		ans += (9999 - 999) * 4;

	if (n < 100000) {
		ans += (n - 9999) * 5;
		cout << ans;
		return 0;
	}
	else
		ans += (99999 - 9999) * 5;

	if (n < 1000000) {
		ans += (n - 99999) * 6;
		cout << ans;
		return 0;
	}
	else
		ans += (999999 - 99999) * 6;

	if (n < 10000000) {
		ans += (n - 999999) * 7;
		cout << ans;
		return 0;
	}
	else
		ans += (9999999 - 999999) * 7;

	if (n < 100000000) {
		ans += (n - 9999999) * 8;
		cout << ans;
		return 0;
	}
	else
		ans += (99999999 - 9999999) * 8;


	ans += 9;
	cout << ans;
}