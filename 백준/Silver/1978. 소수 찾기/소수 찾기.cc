#include<iostream>

using namespace std;

int main() {
    int n, number;
    cin >> n;
    int result = 0;
    for (int i = 0; i < n; i++)
    {
        int count = 0;
        cin >> number;
        if (number == 1)
            continue;
        for (int j = 2; j < number; j++)
        {
            if (number % j == 0)
                count++;
        }
        if (count == 0)
            result++;
    }

    cout << result;
    return 0;
}