#include<iostream>
#include<deque>
#include<string>

using namespace std;

int main()
{
	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int repeat;
	string command;
	deque<int> d;
	int number;
	bool empty;

	cin >> repeat;
	for (int i = 0; i < repeat; i++)
	{
		empty = d.empty();
		cin >> command;
		if (command == "push_front")
		{
			cin >> number;
			d.push_front(number);
		}
		else if (command == "push_back")
		{
			cin >> number;
			d.push_back(number);
		}
		else if (command == "pop_front")
		{
			if (empty)
				cout << -1 << "\n";
			else {
				cout << d.front() << "\n";
				d.pop_front();
			}
		}
		else if (command == "pop_back")
		{
			if (empty)
				cout << -1 << "\n";
			else {
				cout << d.back() << "\n";
				d.pop_back();
			}
		}
		else if (command == "size")
		{
			cout << d.size() << "\n";
		}
		else if (command == "empty")
		{
			if (empty) 
				cout << 1 << "\n";
			else
				cout << 0 << "\n";
		}
		else if (command == "front")
		{
			if (empty)
				cout << -1 << "\n";
			else
				cout << d.front() << "\n";
		}
		else
		{
			if (empty)
				cout << -1 << "\n";
			else
				cout << d.back() << "\n";
		}

	}

	return 0;
}