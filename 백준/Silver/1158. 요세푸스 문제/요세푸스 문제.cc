#include<iostream>
#include<queue>

using namespace std;

int main()
{
	queue<int> q;
	int n, k;
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
		q.push(i);
	
	int count = 0;
	cout << "<";
	while (!q.empty())
	{
		if ((count++) % k == k-1)
		{
			cout << q.front();
			q.pop();
			if (q.size() != 0)
				cout << ", ";
		}
		else {
			q.push(q.front());
			q.pop();
		}
	}
	cout << ">" << "\n";

}