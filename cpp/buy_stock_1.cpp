#include<vector>
#include<iostream>

using namespace std;

class Solution{
    public:
    int maxProfit(vector<int> & prices)
    {
        int min_val = 1e9;
        int max_profit = 0;

        for (int p: prices){
            max_profit = max(max_profit, p - min_val);
            min_val = min(min_val, p);
        }

        return max_profit;
    }
};


int main()
{
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    int max_profit = s.maxProfit(prices);
    cout << max_profit << endl;
    return 0;
}