#include<iostream>
#include<stack>
using namespace std;

int* length;
int* index;
int* arr;

int main()
{
	int n;
	cin >> n;
	stack<int> in;
	length = (int*)calloc(sizeof(int), (n + 1));
	index = (int*)calloc(sizeof(int), (n + 1));
	arr = (int*)calloc(sizeof(int), (n + 1));

	for (int i = 1; i <= n; i++)
		cin >> arr[i];


	for (int i = 1; i <= n; i++)
	{
		int maxindex = 0;
		for (int j = 1; j < n; j++)
		{
			if (arr[i] > arr[j] && length[maxindex] < length[j])
				maxindex = j;
		}
		length[i] = length[maxindex] + 1;
		index[i] = maxindex;
	}

	int longest = 1;
	for (int i = 1; i <= n; i++)
	{
		if (length[i] > length[longest])
			longest = i;
	}

	for (int i = longest; i != 0;)
	{
		in.push(i);
		i = index[i];
	}

	cout << length[longest] << '\n';
	while (!in.empty())
	{
		cout << arr[ in.top() ] << ' ';
		in.pop();
	}
}