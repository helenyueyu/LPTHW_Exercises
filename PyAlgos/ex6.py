# Balanced trees: balanced structure (elements on left side differ from those on the right side by at most one); reduces access times
# Unbalanced trees : tree itself is built faster, but searching and sorting times are lengthened
# Heaps: A sophisticated tree that allows data insertions into a tree structure (max vs. min heaps)


class binaryTree: 
  def __init__(self, nodeData, left=None, right=None): 
    self.nodeData = nodeData
    self.left = left
    self.right = right

  def __str__(self): 
    return str(self.nodeData)

# Because by default, leafs have no more connections, so we put None for both left and right 


tree = binaryTree("Root")
BranchA = binaryTree("Branch A")
BranchB = binaryTree("Branch B")
tree.left = BranchA
tree.right = BranchB

LeafC = binaryTree("Leaf C")
LeafD = binaryTree("Leaf D")
LeafE = binaryTree("Leaf E")
LeafF = binaryTree("Leaf F")
BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF

def traverse(tree): 
  if tree.left != None: 
    traverse(tree.left)
  if tree.right != None: 
    traverse(tree.right)
  print(tree.nodeData)

traverse(tree)

