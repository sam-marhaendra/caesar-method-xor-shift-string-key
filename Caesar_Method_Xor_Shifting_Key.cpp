#include <bits/stdc++.h>
using namespace std;

int main(){
    string S, T, hasil, res1;
    int N;
    getline(cin, S);
    cin >> N >> T;
    int len = T.size();
    for(int i=0;i<S.size();i++){
        res1 += (S[i]-N-10);
    }
    for(int i=0;i<res1.size();i++){
        hasil += (res1[i]^T[i%len]);
    }
    cout << hasil << endl;

    return 0;
}