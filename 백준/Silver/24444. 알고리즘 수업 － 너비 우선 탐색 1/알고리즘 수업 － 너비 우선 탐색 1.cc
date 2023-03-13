#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int main(void)
{

	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int u,v, a, b, r;

	queue<int> q;
	cin >> u >> v >> r;
	vector<int>* graph = new vector<int>[u + 1];
	
	int* count = (int*)calloc(sizeof(int),u+1 );
	int cnt = 0;
	//결국 tree도 그래프의 일종이기 때문에 그래프를 생성하는 방식으로 만들어준다. 
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

	bool visited[200001] = { false };
	visited[r] = true;

	q.push(r);
	count[r] = ++cnt;
	while (!q.empty())
	{
		int front = q.front();
		q.pop();

		for (int i = 0; i < graph[front].size(); i++)
		{
			if (!visited[graph[front][i]])
			{
				q.push(graph[front][i]);
				count[graph[front][i]] = ++cnt;
				visited[graph[front][i]] = true;
			}
		}
		if (cnt == u)
			break;
	}
	for (int i = 1; i <= u; i++)
	{
		cout << count[i] << "\n";
	}

	return 0;

}
