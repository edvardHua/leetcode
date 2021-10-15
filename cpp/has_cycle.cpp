#include<iostream>
#include<unordered_set>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(NULL){}
};

class Solution{
    public:
    bool hasCycle(ListNode* head){
        // 第一个方法是使用 hashmap
        // unordered_set<ListNode*> seen;
        // while(head != nullptr){
        //     if (seen.count(head)){
        //         return true;
        //     }
        //     seen.insert(head);
        //     head = head->next;
        // }
        // return false;

        // 第二个方法是使用快慢指针来做
        if (head == nullptr || head->next == nullptr){
            return false;
        }

        ListNode* slow = head;
        ListNode* fast = head->next;

        while(slow != fast){
            if (fast == nullptr || fast->next == nullptr){
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }

        return true;

    }
};


int main(int argc, char const *argv[]){

    Solution s;
    s.hasCycle(NULL);
    return 0;
}