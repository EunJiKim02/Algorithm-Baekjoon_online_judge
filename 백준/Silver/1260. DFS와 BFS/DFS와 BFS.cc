#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

void dfs(bool * visited, int v, vector<int>* graph)
{
	visited[v] = true;
	cout << v << ' ';
	for (int i = 0; i < (int)graph[v].size(); i++)
	{
		if (visited[graph[v][i]] == false) 
			dfs(visited, graph[v][i], graph);
	}
}

void bfs(bool * visited, int v, vector<int> * graph)
{
	queue<int> q;
	q.push(v);
	cout << v << ' ';
	visited[v] = true;
	while (!q.empty())
	{
		int front = q.front();
		q.pop();

		for (int i = 0; i < (int)graph[front].size(); i++)
		{
			if (visited[graph[front][i]] == false) {
				cout << graph[front][i] << ' ';
				q.push(graph[front][i]);
				visited[graph[front][i]] = true;
			}

		}
	}
}


int main()
{
	int a, b, n;
	int k, s;
	cin >> a >> b >> n;
	vector<int>* graph = new vector<int>[a + 1];
	bool* visited = (bool*)calloc(a + 1, 1);
	for (int i = 0; i < b; i++)
	{
		cin >> k >> s;
		graph[k].push_back(s);
		graph[s].push_back(k);
	}

	for (int i = 1; i <= a; i++)
		sort(graph[i].begin(), graph[i].end());

	dfs(visited, n, graph);
	cout << '\n';
	for (int i = 0; i <= a; i++)
	{
		visited[i] = false;
	}
	bfs(visited, n, graph);
}