#include<iostream>

using namespace std;

int main()
{
	char num;
	int intnum;

	int result = 0;
	bool first = true;
	while ((num = getchar()) != '\n')
	{
		
		intnum = num - '0';

		switch (intnum)
		{
		case 0:
			if (!first)
				cout << "000";
			break;
		case 1:
			if (first)
				cout << 1;
			else
				cout << "001";
			first = false;
			break;
		case 2:
			if (first)
				cout << 10;
			else
				cout << "010";
			first = false;
			break;
		case 3:
			if (first)
				cout << 11;
			else
				cout << "011";
			first = false;
			break;
		case 4:
			cout << 100;
			first = false;
			break;
		case 5:
			cout << 101;
			first = false;
			break;
		case 6:
			cout << 110;
			first = false;
			break;
		case 7:
			cout << 111;
			first = false;
		}
	}

	if (first)
		cout << 0;

}