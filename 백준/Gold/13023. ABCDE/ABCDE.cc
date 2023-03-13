#include<iostream>
#include <vector>

using namespace std;

void dfs(int r, bool* visited, vector<int>* graph, int* max, int* count)
{
	visited[r] = true;
	if (*count > *max)
		*max = *count;
	if (*max == 4)
	{
		cout << 1;
		exit(0);
	}
	(*count)++;
	for (int i = 0; i < graph[r].size(); i++)
	{
		if (visited[graph[r][i]] == false) {
			dfs(graph[r][i], visited, graph, max, count);
			visited[graph[r][i]] = false;
		}
	}
	(*count)--;
}

int main()
{
	int n, f;
	cin >> n >> f;
	vector<int>* graph = new vector<int>[n + 1];
	bool* visited = (bool*)calloc(n + 1, 1);
	int count = 0, max = 0;

	int a, b;
	for (int i = 0; i < f; i++)
	{
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 0; i < n; i++)
	{
		for (int i = 0; i < n; i++)
			visited[i] = false;
		count = 0;
		dfs(i, visited, graph, &max, &count);
	}
	cout << 0 << '\n';

}