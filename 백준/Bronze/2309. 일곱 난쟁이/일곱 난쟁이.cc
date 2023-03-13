#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int height[9] = { 0 };
	int i, j, sum;
	
	for (int i = 0; i < 9; i++)
		cin >> height[i];
	
	sort(height, height+9);
	for (i = 0; i < 9; i++)
	{

		for (j = i+1; j < 9; j++)
		{
			sum = 0;
			for (int k = 0; k < 9; k++)
			{
				if (k == i || k == j)
					continue;
				sum += height[k];
			}
			if (sum == 100)
				break;
		}
		if (sum == 100)
			break;
	}
	for (int k = 0; k < 9; k++)
	{
		if (i == k || j == k)
			continue;
		printf("%d\n", height[k]);
	}
}