struct ListNode {
    int val;
    ListNode* next;

    ListNode(int value, ListNode* nextNode = nullptr) {
        val = value;
        next = nextNode;
    }
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;

public:
    LinkedList() {
        head = new ListNode(0);
        tail = head;
    }

    int get(int index) {
        ListNode* cur = head->next;
        int i = 0;
        while (cur) {
            if (i == index) {
                return cur->val;
            }

            i++;
            cur = cur->next;
        }

        return -1;
    }

    void insertHead(int val) {
        ListNode* node = new ListNode(val, head->next);
        head->next = node;

        if (tail == head) {
            tail = node;
        }
    }
    
    void insertTail(int val) {
        ListNode* node = new ListNode(val);
        tail->next = node;
        tail = node;
    }

    bool remove(int index) {
        ListNode* prev = head;
        ListNode* cur = head->next;
        int i = 0;

        while (cur) {
            if (i == index) {
                prev->next = cur->next;

                if (cur == tail) {
                    tail = prev;
                }

                delete cur;
                return true;
            }

            prev = cur;
            cur = cur->next;
            i++;
        }

        return false;
    }

    vector<int> getValues() {
        vector<int> vals;
        ListNode* cur = head->next;

        while (cur) {
            vals.push_back(cur->val);
            cur = cur->next;
        }

        return vals;
    }
};
