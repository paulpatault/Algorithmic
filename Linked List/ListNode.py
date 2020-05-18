class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        node = self
        output = ""
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        return output
