#include<iostream>
#include<vector>
#include<queue>

using namespace std;

typedef vector<int> vecint;

vecint* graph;
short check[20001] = { 0 };
queue<int> q;

int main()
{
	int n;
	cin >> n;
	graph = new vecint[20001];
	for (int i1 = 0; i1 < n; i1++)
	{
		int v, e;
		int start = 1;
		cin >> v >> e;
		for (int i = 0; i < e; i++)
		{
			int a, b;
			cin >> a >> b;
			graph[a].push_back(b);
			graph[b].push_back(a);
		}
		q.push(1);
		check[1] = 1;
		int c = 2;
		int k = q.front();
		while(!q.empty())
		{
			k = q.front();
			c = (check[k] == 1) ? 2 : 1;
			q.pop();
			for (int i = 0; i < graph[k].size(); i++)
			{
				if (check[graph[k][i]] == 0) {
					check[graph[k][i]] = c;
					q.push(graph[k][i]);
				}
				else if(c != check[graph[k][i]])
				{
					cout << "NO" << '\n';
					k = 0;
				}
				if (k == 0)
					break;
			}
			if (k == 0)
				break;


			if (q.empty())
			{
				for (int i = 1; i <= v; i++) {
					if ((check[i] == 0) && (graph[i].size() != 0)) {
						q.push(i);
						break;
					}
				}
			}
		}
		if (k != 0)
			cout << "YES" << '\n';

		for (int i = 0; i <= v; i++) {
			check[i] = 0;
			graph[i].clear();
		}
		while (!q.empty())
			q.pop();
	}
	return 0;
}