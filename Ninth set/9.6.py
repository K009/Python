class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def is_leaf(self):
        return self.right is None and self.left is None

def count_leafs(top):
    if top is None:
        return
    sum = 0
    stack = list()
    stack.append(top)
    while stack:
        node = stack.pop()
        if node.right:
        	stack.append(node.right)
        	if node.right.is_leaf():
        		sum +=1
        if node.left:
        	stack.append(node.left)     
        	if node.left.is_leaf():   		
        		sum +=1        	
    return sum


def calc_total(top):
    if top is None:
        return
    sum = top.data
    stack = list() 
    stack.append(top)
    while stack:
        node = stack.pop()
        #visit(node)
        if node.right:
        	sum += node.right.data
        	stack.append(node.right)
        if node.left:
        	sum += node.left.data
        	stack.append(node.left)
    return sum



root = None           # puste drzewo
root = Node("alone")  # drzewo z jednym węzłem
# Ręczne budowanie większego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(calc_total(root))
print(count_leafs(root))