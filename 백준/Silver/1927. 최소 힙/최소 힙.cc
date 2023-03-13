#include<iostream>

using namespace std;


int arr[100001] = { 0 };

void insert(int data, int *count)
{
	arr[++(*count)] = data;

	for (int i = (*count);i > 1; i /= 2)
	{
		if (arr[i] < arr[i / 2])
		{
			int temp = arr[i];
			arr[i] = arr[i/2];
			arr[i / 2] = temp;
		}
	}
}

void delete_heap(int * count)
{
	cout << arr[1] << "\n";

	arr[1] = arr[(*count)];
	arr[(*count)] = 0;
	(*count)--;
	
	for (int i = 1; (i <= (*count/ 2)) && (i*2+1 <= 100001);)
	{
		
		if ((arr[i * 2 + 1] == 0))
		{
			if(arr[i] >= arr[i * 2])
			{ 
				int temp = arr[i];
				arr[i] = arr[i * 2];
				arr[i * 2] = temp;
				i = i * 2;
			}

			break;
		}

		if ((arr[i] > arr[i * 2])) //i > i*2
		{
			if (arr[i * 2] < arr[i * 2 + 1]) // i > i*2+1 > i*2
			{
				int temp = arr[i];
				arr[i] = arr[i * 2];
				arr[i * 2] = temp;
				i = i * 2;
			}
			else // i > i * 2 > i * 2 + 1
			{
				int temp = arr[i];
				arr[i] = arr[i * 2 + 1];
				arr[i * 2 + 1] = temp;
				i = (i * 2 + 1);
			}

		}
		else if (arr[i] > arr[i * 2 +1]) { // i * 2 > i > i *2 +1 
			int temp = arr[i];
			arr[i] = arr[i * 2 + 1];
			arr[i * 2 + 1] = temp;
			i = (i * 2 + 1);
		}
		else // ? > ? > i
			break;
	}

}

int main(void)
{
	cin.tie(NULL);
	cin.sync_with_stdio(false);

	int number, repeat;
	int count = 0;
	cin >> repeat;

	for (int i = 0; i < repeat; i++)
	{
		cin >> number;
		if (number == 0)
		{
			if (count == 0)
				cout << 0 << "\n";
			else
				delete_heap(&count);
			
		}
		else
		{
			insert(number, &count);

		}
	}
	return 0;
}