class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self, res=""):
        res += self.value + " "
        if self.left:
            res = self.left.preorder(res)
        if self.right:
            res = self.right.preorder(res)
        return res


def invert(node):
    temp = node.left
    node.left = node.right
    node.right = temp

    if node.left:
        node.left = invert(node.left)
    if node.right:
        node.right = invert(node.right)
    return node


root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.left = Node("f")

print(root.preorder())
# a b d e c f
print("\n")
invert(root)
print(root.preorder())
# a c f b e d
