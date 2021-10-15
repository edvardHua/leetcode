#include<iostream>
#include<algorithm>

using namespace std;

class Soultion{
    public:
        string addString(string num1, string num2){
            int i = num1.length() - 1;
            int j = num2.length() - 1;

            string ans = "";
            int add = 0;
            while(i >= 0 || j >= 0){

                int n1 = i >= 0 ? num1[i] - '0': 0;
                int n2 = j >= 0 ? num2[j] - '0': 0;
                int sum = n1 + n2 + add;

                ans.push_back('0' + sum % 10);
                add = sum / 10;
                i -= 1;
                j -= 1;
            }
            reverse(ans.begin(), ans.end());
            return ans;
        }
};


int main(int argc, char const *argv[])
{
    Soultion s;
    string res = s.addString("123", "23");
    cout << res << endl;
    return 0;
}

