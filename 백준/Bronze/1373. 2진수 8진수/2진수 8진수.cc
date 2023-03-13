#include<iostream>
#include<math.h>
#include<string>
#include<vector>

using namespace std;

int main()
{
	string number;
	vector<int> resultnumber;
	int result, i;
	cin >> number;
	result = 0;
	int index = 0;

	int size = number.size() - 1;
	resultnumber.push_back(0);

	for(i = 0; ; i++, size--)
	{
		result += ((number.at(size) - '0') * pow(2, i));
		resultnumber[index] = result;
		if (!size)
			break;
		if (i % 3 == 2) {
			index++;
			resultnumber.push_back(0);
			result = 0;
			i = -1;
		}
	}

	for (int i = index; i >= 0; i--)
	{
		cout << resultnumber.at(i);
	}

	return 0;
}