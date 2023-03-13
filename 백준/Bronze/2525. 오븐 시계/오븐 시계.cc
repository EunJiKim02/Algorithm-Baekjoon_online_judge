#include<iostream>

using namespace std;

int main()
{
	int hour, min;
	int addm;
	int resultmin, resulthour;
	cin >> hour >> min;
	cin >> addm;
	resultmin = (min + addm) % 60;
	resulthour = (hour + ((min + addm) / 60)) % 24;

	cout << resulthour<<" " << resultmin;

	return 0;
}