#include <iostream>
#include <stack>

using namespace std;

typedef struct num {
	bool check;
	int data;
	struct num* link;
}Num;

int main()
{
	stack<Num*> nonfind;
	int n;
	Num* start = NULL;
	cin >> n;
	int topindex = 0;
	for (int i = 0; i < n; i++)
	{
		Num *number = (Num*)malloc(sizeof(Num));
		cin >> number->data;
		number->check = false;
		number->link = NULL;
		if (i == 0)
			start = number;
		if (nonfind.empty())
			nonfind.push(number);
		else
		{
			nonfind.top()->link = number;
			if (nonfind.top()->data > number->data)
				nonfind.push(number);
			else {
				while (!nonfind.empty() && nonfind.top()->data < number->data) {
					nonfind.top()->data = number->data;
					nonfind.top()->check = true;
					nonfind.pop();
				}
				nonfind.push(number);
			}
		}
	}
	for (Num* p = start; p; p = p->link) {
		if (p->check)
			cout << p->data << " ";
		else
			cout << -1 << " ";

	}
}