#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main()
{
	int number;
	int check = 0;
	cin >> number;
	for (int i = 0; i < number; i++) {
		check = 0;
		string s;
		cin >> s;
		for (int j = 0; j < s.size(); j++)
		{
			if (s.at(j) == '(')
				check++;
			else
				check--;
			if (check < 0)
				break;
		}
		if (check == 0)
			cout << "YES"<<"\n";
		else
			cout << "NO"<<"\n";

	}
	return 0;
}