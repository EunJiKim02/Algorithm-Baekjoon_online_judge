#include <iostream>
using namespace std;

int* col;
int n;
int result = 0;

void dfs(int i) {
    for (int k = 1; k < i; k++) {
        if ((col[i] == col[k]) || (abs(col[i] - col[k]) == (i - k)))
            return;
    }
    if (i == n) {
        result += 1;
    }
    else {
        for (int j = 1; j < n+1; j++) {
            col[i + 1] = j;
            dfs(i + 1);
            col[i + 1] = -1;
        }
    }

    return;
}

int main(void)
{
    cin >> n;
    col = (int*) calloc(n+1, sizeof(int));
    dfs(0);
    cout << result << '\n';
    return 0;
}