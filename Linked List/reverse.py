"""
Example :
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def __repr__(self):
        node = self
        output = ""
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        return output

    # Iterative Solution
    def reverseIteratively(self, head):
        """
        explication : 
        //--------------------------------//
            prev = NULL
            head = 2 -> 1 -> 0 -> NULL
            temp = head
            temp.next = prev  # temp = 2 -> NULL 
            prev = temp
            head = head.next
        //--------------------------------//
            prev = 2 -> NULL 
            head = 1 -> 0 -> NULL
            temp = head
            temp.next = prev  # temp = 1 -> 2 -> NULL 
            prev = temp
            head = head.next
        //--------------------------------//
            prev = 1 -> 2 -> NULL 
            head = 0 -> NULL
            temp = head
            temp.next = prev  # temp = 0 -> 1 -> 2 -> NULL 
            prev = temp
            head = head.next
        //--------------------------------//
            prev = 0 -> 1 -> 2 -> NULL 
        """
        prev = None
        while head:
            temp = ListNode(head.val)
            temp.next = prev
            prev = temp
            head = head.next
        return prev

    # Recursive Solution
    def reverseRecursively(self, head):
        def rev(head, prev):
            if head:
                temp = ListNode(head.val)
                temp.next = prev
                prev = temp
                head = head.next
                return rev(head, prev)
            else:
                return prev

        return rev(head, None)


# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ", testHead)
# 4 3 2 1 0

# testHead.reverseIteratively(testHead)
print("List after reversal (iterative): ", testHead.reverseIteratively(testHead))
# 0 1 2 3 4
# testHead.reverseRecursively(testHead)
print("List after reversal (recursive): ", testHead.reverseRecursively(testHead))
# 0 1 2 3 4
