/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int c = 0;
        ListNode* prev = nullptr;
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        if(l1->val + l2->val < 10)
        {
            c = 0;
            curr->val = l1->val + l2->val;
        }
        
        else
        {
            c = 1;
            curr->val = l1->val + l2->val - 10;
        }

        prev = curr;
        l1 = l1->next;
        l2 = l2->next;

        while(l1 && l2)
        {
            curr = new ListNode(c);
            prev->next = curr;
            if(l1->val + l2->val + c < 10)
            {
                c = 0;
                curr->val = curr->val + l1->val + l2->val;
            }

            else
            {
                c = 1;
                curr->val = curr->val + l1->val + l2->val - 10;
            }

            prev = curr;
            l1 = l1->next;
            l2 = l2->next;
        }

        while(l1)
        {
            curr = new ListNode(c);
            prev->next = curr;
            if(c + l1->val == 10)
            {
                c = 1;
                curr->val = 0;
            }

            else
            {
                c = 0;
                curr->val = curr->val + l1->val;
            }

            prev = curr;
            l1 = l1->next;
        }

        while(l2)
        {
            curr = new ListNode(c);
            prev->next = curr;
            if(c + l2->val == 10)
            {
                c = 1;
                curr->val = 0;
            }

            else
            {
                c = 0;
                curr->val = curr->val + l2->val;
            }

            prev = curr;
            l2 = l2->next;
        }

        if(c == 1)
        {
            curr = new ListNode(1);
            prev->next = curr;
        }

        return head;
    }
};
