#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	vector<int> v;
    stringstream ss(str);
    int i;
    char ch;
    while (ss >> i >> ch) {
        v.push_back(i);
    }
    ss >> i;
    v.push_back(i);
    return v;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}