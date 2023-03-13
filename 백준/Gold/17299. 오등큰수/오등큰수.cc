#include<iostream>
#include<stack>
#include<vector>
#define MAX 1000000

int count[MAX] = { 0 };

typedef struct num {
	int data;
	bool check;
}Num;

int main()
{
	int n;
	std::cin >> n;
	std::vector<Num*> v;
	std::stack<Num*> nonfind;
	for (int i = 0; i < n; i++)
	{
		int number;
		std::cin >> number;
		Num* curr = (Num*)malloc(sizeof(Num));
		curr->check = false;
		curr->data = number;
		v.push_back(curr);
		count[number]++;
	}
	for (int i = 0; i < v.size(); i++)
	{
		if (nonfind.empty())
			nonfind.push(v[i]);
		else
		{
			if (count[nonfind.top()->data] > count[v[i]->data])
				nonfind.push(v[i]);
			else {
				while (!nonfind.empty() && count[nonfind.top()->data] < count[v[i]->data]) {
					nonfind.top()->data = v[i]->data;
					nonfind.top()->check = true;
					nonfind.pop();
				}
				nonfind.push(v[i]);
			}
		}
	}

	for (int i = 0; i < v.size(); i++)
	{
		if (v[i]->check)
			std::cout << v[i]->data << ' ';
		else
			std:: cout << -1 << ' ';
	}

	return 0;
}