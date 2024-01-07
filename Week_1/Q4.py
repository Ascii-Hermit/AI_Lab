class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

# Example usage:
root = None
root = insert(root,50)
root = insert(root,30)
root = insert(root,70)
root = insert(root,20)
root = insert(root,40)
root = insert(root,60)
root = insert(root,80)

print("Inorder traversal:", inorder(root))

