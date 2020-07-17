class BSTNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if value is None
        if self.value is None:
            # assign self.value to value
            self.value = value
        # check if the value is less than self.value
        elif value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # Else 
            else:
                # Repeat the process on left subtree
                self.left.insert(value)
        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # if there is no right childe, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)