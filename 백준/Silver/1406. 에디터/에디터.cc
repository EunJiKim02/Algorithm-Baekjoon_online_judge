#include<iostream>
#include<string>
#include<deque>

using namespace std;

int main()
{
	deque<char> front;
	deque<char> back;
	char s[100001] = { 0 };
	int n;
	cin >> s;
	getchar();
	cin >> n;
	for (int i = 0; i < 100001; i++)
	{
		if (s[i] == 0)
			break;
		front.push_back(s[i]);
	}

	for (int i = 0; i < n; i++) {
		char command;
		cin >> command;
		switch (command)
		{
		case 'L':
			if (front.empty())
				break;
			back.push_back(front.back());
			front.pop_back();
			break;
		case 'D':
			if (back.empty())
				break;
			front.push_back(back.back());
			back.pop_back();
			break;
		case 'B':
			if (!front.empty())
				front.pop_back();
			break;
		case 'P':
			char c;
			cin >> c;
			front.push_back(c);
		}
	}
	
	while (!front.empty())
	{
		cout << front.front();
		front.pop_front();
	}
	while (!back.empty())
	{
		cout << back.back();
		back.pop_back();
	}
	cout << '\n';
	return 0;
}