#include<iostream>
#include<stack>
#include<string>

using namespace std;

int OperRank(char k)
{
	switch (k)
	{
	case '*': case '/':
		return 3;
	case '+': case '-':
		return 2;
	case '(':
		return 4;
	case ')':
		return 1;
	default:
		return 0;
	}
}


int main()
{
	stack<char> oper;
	string ex;
	char tmp;
	cin >> ex;
	for (int i = 0; i < ex.length(); i++){
		if (OperRank(ex.at(i)) == 0)
			cout << ex.at(i);
		else{
			if (oper.empty()){
				if (ex.at(i) == '(') {
					oper.push(')');
					continue;
				}
				oper.push(ex.at(i));
				continue;
			}
			if (ex.at(i) == ')'){
				while (oper.top() != ')'){
					cout << oper.top();
					oper.pop();
				}
				oper.pop();
				continue;
			}
			tmp = oper.top();
			if (ex.at(i) == '(') {
				oper.push(')');
				continue;
			}
			if (OperRank(tmp) < OperRank(ex.at(i))) {
				oper.push(ex.at(i));
			}
			else if (OperRank(tmp) == OperRank(ex.at(i))) {
				while (!oper.empty() && OperRank(oper.top()) == OperRank(ex.at(i))) {
					cout << oper.top();
					oper.pop();
				}
				oper.push(ex.at(i));
			}
			else
			{
				while (!oper.empty()) {
					if (oper.top() == ')')
						break;
					cout << oper.top();
					oper.pop();
				}
				oper.push(ex.at(i));
			}

		}
	}
	while (!oper.empty()) {
		cout << oper.top();
		oper.pop();
	}
	return 0;
}