#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main(void)
{
	stack<int> s;
	string option;
	int num;
	int number;
	cin >> num;

	for (int i = 0; i < num; i++)
	{
		cin >> option;

		if (option.compare("push") == 0)
		{
			cin >> number;
			s.push(number);
		}
		else if (option.compare("pop") == 0)
		{
			if (s.empty())
				cout << -1 << endl;
			else {
				cout << s.top() << endl;
				s.pop();
			}
		}
		else if (option.compare("size") == 0)
		{
			cout << s.size() << endl;
		}
		else if (option.compare("empty") == 0)
		{
			if (s.empty())
				cout << 1 << endl;
			else
				cout << 0 << endl;
		}
		else
		{
			if (s.empty())
				cout << -1 << endl;
			else
				cout << s.top() << endl;
		}
	}

}