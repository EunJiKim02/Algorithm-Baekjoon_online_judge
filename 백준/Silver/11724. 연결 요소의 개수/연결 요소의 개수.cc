#include<iostream>
#include<vector>

using namespace std;

typedef vector<int> vecint;

void dfs(int v, bool* visited, vecint* graph)
{
	visited[v] = true;
	for (int i = 0; i < (int)graph[v].size(); i++)
	{
		if (visited[graph[v][i]] == false)
			dfs(graph[v][i], visited, graph);
	}
}

int main()
{
	int m, n;
	int u, v;
	vecint* graph;
	bool* visited;
	int count = 0;

	cin >> n >> m;
	graph = new vecint[n + 1];
	visited = (bool*)calloc(1, (n + 1));
	for (int i = 0; i < m; i++)
	{
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	for (int i = 1; i <= n; i++)
		visited[i] = false;

	for (int i = 1; i <= n; i++)
	{
		if (visited[i] == false) {
			dfs(i, visited, graph);
			count++;
		}
	}

	cout << count;
}