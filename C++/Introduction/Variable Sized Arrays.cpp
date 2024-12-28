#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q;
    cin >> n >> q;
    vector<vector<int>> v1;
    for (int a = 0; a < n; a++) {
        int k;
        cin >> k;
        vector<int> v2;
        for (int b = 0; b < k; b++) {
            int elem;
            cin >> elem;
            v2.push_back(elem);
        }
        v1.push_back(v2);
    }
    for (int a = 0; a < q; a++) {
        int i, j;
        cin >> i >> j;
        cout << v1[i][j] << "\n";
    }
    return 0;
}
