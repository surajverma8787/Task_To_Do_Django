#include <bits/stdc++.h>
#define int long long int
#define IOS()                         \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
#define mod 1000000007
const int sz = 2 * 1e5 + 5;
using namespace std;
signed main()
{
    IOS();
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    int q;
    cin >> q;
    int pref[n + 1] = {0};
    for (int i = 0; i < q; i++)
    {
        int s, l, r;
        cin >> s >> l >> r;
        pref[l] += s;
        pref[r + 1] -= s;
    }
    for (int i = 1; i < n; i++)
    {
        pref[i] += pref[i - 1];
    }
    for (int i = 0; i < n; i++)
        a[i] += pref[i];
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += a[i];
    cout << sum << "\n";
}