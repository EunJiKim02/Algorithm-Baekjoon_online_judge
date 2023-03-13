#include<iostream>
#include<stack>

using namespace std;

int main()
{
	stack<char> temp;
	char c;
	while ((c = getchar()) != '\n') {
		if (c == '<')
		{
			while (!temp.empty())
			{
				cout << temp.top();
				temp.pop();
			}
			do {
				cout << c;
			} while ((c = getchar()) != '>');
			cout << '>';
			continue;
		}
		else
		{
			if (c == ' ')
			{
				while (!temp.empty())
				{
					cout << temp.top();
					temp.pop();
				}
				cout << ' ';
			}
			else
			{
				temp.push(c);
			}
		}
	}
	while (!temp.empty())
	{
		cout << temp.top();
		temp.pop();
	}

	return 0;
}