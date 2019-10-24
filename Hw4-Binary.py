class Tree:
    # creates nodes for trees, each with a value and connections to child nodes
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    # constructor is used to call fuctions to fill in the list and create a complete tree
    def __init__(self, tree):
        self._root = self.create_tree(self.fill_list(tree), 0, len(tree)-1)

    # creates the nodes and linsk them to form a tree
    def create_tree(self, a, start, end):
        if start>end:
            return None # ends when there is no more data in list to add to tree
        else:
            node = self.TreeNode(a[start]) # creates node
            node.left = self.create_tree(a, 2 * start + 1, end) # recurs to position in list of left child node
            node.right = self.create_tree(a, 2 * start + 2, end) # recurs to position in list of rightt child node
            return node # inserts completed node into tree

    # create tree function only works with a completed tree(list) so this function completes the list
    def fill_list(self, a):
        last_val = a[-1] # gets last value in list
        for i, item in enumerate(a):
            # if the item in the list is none, it creates left and right None values so the tree can become "full"
            if item is None:
                if 2 * i + 1 <= a.index(last_val): # makes sure that new nodes arent created after last real value
                    a.insert(2 * i + 1, None)
                    a.insert(2 * i + 2, None)
        return a # returns complete list to be used to create a tree

def preorder(r):
    # recursion continues until no more nodes
    if r.val is not None:
        print(r.val, end=" ") # prints value at node
        if r.left is not None:
            preorder(r.left) # traverses left through tree until no more left nodes
        if r.right is not None:
            preorder(r.right) # traverses right through tree until no more right nodes

def inorder(r):
    # traverses left until it can't anymore
    if r.left is not None:
        inorder(r.left)
    # prints the leftmost value
    if r.val is not None:
        print(r.val, end=" ")
    # traverses right until it can't anymore
    if r.right is not None:
        inorder(r.right)


def main():
    """tree1 = Tree([1, None, 2, 3])
    print("Preorder Traversal")
    preorder(tree1._root)
    print()
    print("********")
    print("Inorder Traversal")
    inorder(tree1._root)"""

    """tree2 = Tree([1, 2, 3, None, 4, None, 5, 6, 7, 8, None, None, None, 9])
    print("Preorder Traversal")
    preorder(tree2._root)
    print()
    print("********")
    print("Inorder Traversal")
    inorder(tree2._root)"""

    tree3 = Tree([1, 2, None, 3, 4, None, 5, None, None, 6, 7, None, None, None, 8])
    print("Preorder Traversal")
    preorder(tree3._root)
    print()
    print("********")
    print("Inorder Traversal")
    inorder(tree3._root)


if __name__ == '__main__':
    main()
