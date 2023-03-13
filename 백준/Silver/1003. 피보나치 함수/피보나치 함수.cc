#include<iostream>

using namespace std;

int cnt0[2] = { 0 };
int cnt1[2] = { 0 };


int main()
{
    int n;
    int k;
    int tmp = 0;
    cin >> n;
    cnt0[0] = 1;
    cnt1[0] = 0;
    cnt0[1] = 0;
    cnt1[1] = 1;
    for (int i = 0; i < n; i++)
    {
        cnt0[0] = 1;
        cnt1[0] = 0;
        cnt0[1] = 0;
        cnt1[1] = 1;
        cin >> k;
        if (k == 0)
            cout << "1 0\n";
        else if (k == 1)
            cout << "0 1\n";
        else {
            for (int j = 2; j <= k; j++) {
                tmp = cnt0[0];
                cnt0[0] = cnt0[1];
                cnt0[1] = cnt0[1] + tmp;
                tmp = cnt1[0];
                cnt1[0] = cnt1[1];
                cnt1[1] = cnt1[1] + tmp;
            }
            cout << cnt0[1] << ' ' << cnt1[1] << '\n';
        }

    }

}
