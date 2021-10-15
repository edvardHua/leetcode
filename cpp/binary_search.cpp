#include<iostream>
#include<vector>

using namespace std;

class Solution{
    public:
    int binary_search(vector<int>& arr, int target){
        int left = 0;
        int right = arr.size() - 1;
        while(right > left){
            int mid = (left + right) / 2;
            if (arr[mid] == target){
                return mid;
            }
            if (arr[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return -1;
    }
};


int main()
{
    vector<int> arr = {1,2,7,-2,-10,19,0};
    Solution s;
    int ind = s.binary_search(arr, -22);
    cout << ind << endl;
    return 0;
}