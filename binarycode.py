from binarytree import build

nodes = [6, 3, 8, 2, 11, 13]

binary_tree = build(nodes)
print("Binary trees from list :\n",
      binary_tree)

print('\nList from binary tree:',
      binary_tree.values)

