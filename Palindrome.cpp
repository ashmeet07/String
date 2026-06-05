//Using two pointer approach checking palindrome in c++
#include <bits/stdc++.h>
using namespace std;

string checkPalindrome(string s){
    int i=0,j=s.size()-1;
    while(i<j){
        if(s[i]==s[j]){
            i++;j--;
            continue;
        }
        else{
            return "False";
        }
    }
    return "True";
}

int main() {
    string s="Hello";
    cout<<checkPalindrome(s);
    cout<<"Hello World";

    return 0;
}
