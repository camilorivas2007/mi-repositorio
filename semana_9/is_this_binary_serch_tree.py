""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    return validate(root, float('-inf'), float('inf'))

def validate(node, min_val, max_val):
    if node is None:
        return True
    if node.data <= min_val or node.data >= max_val:
        return False
    return validate(node.left, min_val, node.data) and validate(node.right, node.data, max_val)
