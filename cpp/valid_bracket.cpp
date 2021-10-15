#include<iostream>
#include<stack>
#include<unordered_map>

using namespace std;

class Solution
{
    public:
    
    bool isValid(string s)
    {
        int n = s.size();
        if (n % 2 == 1){return false;}

        // 注意，char 是 '', string 是 ""
        unordered_map<char, char> pairs = {
            {'{', '}'},
            {'[', ']'},
            {'(', ')'}
        };

        stack<char> stk;
        for (char ch: s){
            if (pairs.count(ch)){
                if (stk.empty() || stk.top() != pairs[ch]){
                    return false;
                }
                stk.pop();
            }else{
                stk.push(ch);
            }
        }
        return stk.empty();
    }
};


int main()
{
    string test = "[{}]";
    Solution s;
    bool res = s.isValid(test);
    cout << res << endl;

    return 0;
}