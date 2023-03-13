#include<iostream>
#include<vector>

using namespace std;


void printresult(char x, char y)
{
	cout << x << "+=" << y << '\n';
}

int main()
{
	long long a, b;
	cin >> a >> b;
	vector <pair<int, int>> result;
	int count = 0;
	if (a == b) {
		cout << count << '\n';
		return 0;
	}

	while (a % 2 == 0) {
		a /= 2;
		result.push_back({ 'B', 'B' });
		count++;
	}
	while (b % 2 == 0) {
		b /= 2;
		result.push_back({ 'A', 'A' });
		count++;
	}

	while (a != b)
	{

		if (a < b)
		{
			b += a;
			result.push_back({ 'B', 'A' });
		}
		else // a > b
		{
			a += b;
			result.push_back({ 'A', 'B' });
		}
		count++;
		while (a % 2 == 0) {
			a /= 2;
			result.push_back({ 'B', 'B' });
			count++;
		}
		while (b % 2 == 0) {
			b /= 2;
			result.push_back({ 'A', 'A' });
			count++;
		}
	}
	cout << count << '\n';
	for (int i = 0; i < count; i++)
		printresult(result.at(i).first, result.at(i).second);
}