#include<iostream>
#include<unordered_set>

using namespace std;

struct ListNode{
    int val;
    ListNode* next;
    ListNode(int x): val(x), next(nullptr){}
};

class Solution{
    public:

    ListNode* is_intersection(ListNode* a, ListNode* b){

        unordered_set<ListNode*> visited;

        // 方法一，使用 set 来判断是否相交
        ListNode* temp = a;
        while(temp){
            visited.insert(temp);
            temp = temp->next;
        }

        temp = b;
        while(temp){
            if(visited.count(temp)){
                return temp;
            }
            temp = temp->next;
        }

        return nullptr;
    }

    ListNode* is_intersection2(ListNode* a, ListNode* b){
        // 方法二，使用双指针来判断是否相交
        if(!a || !b){ return nullptr; }

        ListNode* headA = a;
        ListNode* headB = b;
        // 这里其实还是很 trick 的
        // 因为相等的情况下不是相交就是互相为 null
        while(headA != headB){
            
            // if (headA == headB){
            //     return headA;
            // }
            // if(headA == nullptr){
            //     headA = b;
            // }else{
            //     headA = headA->next;
            // }

            // if(headB == nullptr){
            //     headB = a;
            // }else{
            //     headB = headB->next;
            // }

            headA = headA == nullptr? headA = b : headA = headA->next;
            headB = headB == nullptr? headB = a : headB = headB->next;

        }

        return headA;
    }

};


int main()
{
    cout << "hello" << endl;
    return 0;
}