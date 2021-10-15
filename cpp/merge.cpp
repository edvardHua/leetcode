#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

class Solution
{
    public:
        void merge(vector<int> &num1, int m, vector<int> &num2, int n)
        {
            // 方法一，直接合并后排序
            // for (int i = 0; i != n; i ++){
            //     num1[m + i] = num2[i];
            // }
            // sort(num1.begin(), num1.end());

            // 方法二，合并排序，但是是从尾部开始
            int tmp;
            int k = m + n -1;
            m -= 1;
            n -= 1;
            while(m >= 0 && n >= 0){
                if (num1[m] >= num2[n]){
                    num1[k] = num1[m];
                    m -= 1;
                }else{
                    num1[k] = num2[n];
                    n -= 1;
                }
                k -= 1;
            }

            for (int i = n; i >= 0; i --){
                num1[i] = num2[i];
            }

        }
};

int main()
{

    vector<int> num1 = {1, 2, 3, 0, 0, 0};
    vector<int> num2 = {2, 4, 6};

    int m = 3;
    int n = 3;

    Solution s;
    s.merge(num1, m, num2, n);
    for (int i = 0; i < 6; i ++){
        cout << num1[i] << endl;
    }
    return 0;
}