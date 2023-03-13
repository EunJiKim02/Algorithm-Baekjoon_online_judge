#include<iostream>
#include<queue>
#include<string>

using namespace std;

int main()
{
	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int repeat;
	string command;
	queue<int> q;
	int number;
	bool empty;

	cin >> repeat;
	for (int i = 0; i < repeat; i++)
	{
		empty = q.empty();
		cin >> command;
		if (command == "push")
		{
			cin >> number;
			q.push(number);
		}
		else if (command == "pop")
		{
			if (empty)
				cout << -1 << "\n";
			else {
				cout << q.front() << "\n";
				q.pop();
			}
		}
		else if (command == "size")
		{
			cout << q.size() << "\n";
		}
		else if(command == "empty")
		{
			if (empty) {
				cout << 1 << "\n";
			}
			else 
			{
				cout << 0 << "\n";
			}
		}
		else if (command == "front")
		{
			if (empty) 
				cout << -1 << "\n";
			else
				cout << q.front() << "\n";
		}
		else
		{
			if (empty)
				cout << -1 << "\n";
			else
				cout << q.back() << "\n";
		}

	}

	return 0;
}