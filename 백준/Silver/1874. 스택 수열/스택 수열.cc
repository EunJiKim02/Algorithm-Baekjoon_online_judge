#include<iostream>
#include<stack>

using namespace std;

int main()
{
	int n;
	cin >> n;
	stack<int> s;
	int snumber = 1;
	int arr[100001] = { 0 };
	int i;
	char arr2[200000] = {0};
	int check = 0;

	for (i = 0; i < n; i++)
	{
		int number;
		cin >> number;
		arr[i] = number;
	} // 배열 받음

	int oneton = 1;
	for (i = 0; i < n; i++) // 숫자가 해결되면 다음 숫자로 넘기기
	{
		while(1) 
		{
			if (oneton <= n)
			{
				if ((!s.empty()) && (s.top() == arr[i])) {
					//cout << "-" << "\n";
					arr2[check++] = '-';
					s.pop();
					break;
				}
				else {
					//cout << "+" << "\n";
					arr2[check++] = '+';
					s.push(oneton++);
				}
			}
			else { // oneton == n
				if (s.top() != arr[i])
					break;
				arr2[check++] = '-';
				//cout << "-" << "\n";
				s.pop();
				break;
			}
			
		}


	}



	if (!s.empty())
		cout << "NO\n";
	else
	{
		for (int i = 0; i < check; i++)
		{
			cout << arr2[i] << "\n";
		}
	}

	return 0;
}