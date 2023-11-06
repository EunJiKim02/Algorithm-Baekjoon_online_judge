#include <iostream>
#include <vector>
#include<algorithm>

using namespace std;


vector<int> prime = { 11, 13, 17, 19,
31, 37, 53, 59, 71,
73, 79, 97 };

bool is_prime(int number) {
    return binary_search(prime.begin(), prime.end(), number);
}

void backtrack(int M, vector<int>& result, int A, int B, int N) {
    if (result.size() == N - 2) {
        if (is_prime(result[M - 1] * 10 + (B / 10))) {
            result.push_back(B / 10);
            result.push_back(B % 10);
            for (int x : result) 
                cout << x;
            cout << endl;
            exit(0);
        }
        else {
            cout << -1 << endl;
            exit(0);
        }
    }
    for (int i = 1; i < 10; i += 2) { 
        if (is_prime(result[M - 1] * 10 + i)) {
            result.push_back(i);
            backtrack(M + 1, result, A, B, N);
            result.pop_back();
        }
    }
}

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int A, B, N;
    cin >> A >> B >> N;
    if ((B / 10) % 2 == 0) {
        cout << -1 << endl;
        return 0;
    }
    else {
        vector<int> result = { A / 10, A % 10 };
        backtrack(2, result, A, B, N);
    }
 
    cout << -1 << endl;
    return 0;

}