#include <iostream>
#include <stack>
#include <string>
using namespace std;


int main()
{
	int number;
	cin >> number;
	getchar();
	stack<char> s;
	for (int i = 0; i < number; i++) {
		string sentence;
		getline(cin, sentence);
		for (int j = 0; j < sentence.length(); j++)
		{
			if (sentence.at(j) == ' ')
			{
				while (1)
				{
					if (s.empty())
						break;
					cout << s.top();
					s.pop();
				}
				cout << ' ';
			}
			else
				s.push(sentence.at(j));
		}
		while (1)
		{
			if (s.empty()) {
				cout << '\n';
				break;
			}

			cout << s.top();
			s.pop();
		}

	}
	return 0;
}