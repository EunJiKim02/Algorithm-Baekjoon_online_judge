#include<iostream>
#include <vector>
#define MAX 10

using namespace std;

bool visited[MAX] = { 0 };
vector<int> s;
int m, n;

int arr[MAX] = { 0 };

void dfs(int v, int cnt)
{
	if (cnt == n) {
		for (int i = 0; i < s.size(); i++)
			cout << s[i] << ' ';

		cout << '\n';
		
		return;
	}
	for (int i = v; i <= m; i++) {
		if (visited[i] == false) {
			visited[i] = true;
			s.push_back(i);
			dfs(i, cnt+1);
			visited[i] = false;
			s.pop_back();

		}
	}
}


int main()
{

	cin >> m >> n;


	for (int i = 0; i < n; i++)
		arr[i+1] = i+1;

	dfs(1, 0);
	
	return 0;
}