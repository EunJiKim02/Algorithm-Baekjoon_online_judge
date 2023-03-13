#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

bool visited[200001] = { false };

void dfs(int r, int * cnt, int * count, vector<int>* graph) {
	visited[r] = true;
	count[r] = ++(*cnt);
	for (int i = 0; i < graph[r].size(); i++)
	{
		if (visited[graph[r][i]] == false)
			dfs(graph[r][i], cnt, count, graph);
	}

}

int main(void)
{

	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int u, v, a, b, r;

	queue<int> q;
	cin >> u >> v >> r;
	vector<int>* graph = new vector<int>[u + 1];

	int* count = (int*)calloc(sizeof(int), u + 1);
	int cnt = 0;

	for (int i = 0; i < v; i++)
	{
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 1; i <= u; i++)
	{
		sort(graph[i].begin(), graph[i].end());
	}


	visited[r] = true;
	count[r] = cnt;
	dfs(r, &cnt, count, graph);
	
	for (int i = 1; i <= u; i++)
	{
		cout << count[i] << "\n";
	}

	return 0;

}
