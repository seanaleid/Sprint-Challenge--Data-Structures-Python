class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        """ recursive """
        # only run if node exists
        if node is not None:
            # capture the node.next_node as next_node to pass at the bottom when we call self.reverse_list(next_node, prev)
            next_node = node.next_node
            # to move the head if node.next_node is None 
            if node.next_node is None:
                # (basically if it's the tail, move the head to the tail)
                self.head = node
            # reassign the node.next_node 
            # currently pointing to the right, next_node
            # line 54 points next_node to the left
            node.next_node = prev
            # calls the reverse_list(node, prev) to run again on the next node
            # uses the capture on 46 as the next node to run in place of node
            # and uses the current node above as the prev to be reassigned to the node.next_node
            self.reverse_list(next_node, node)

        """ iterative """
        # snapshot of the current node
        # curr = node
        # snapshot of the prev
        # prev = None
        # while loop to iterate through
        # while curr is not None:
            # snapshot of the current next_value
            # next_node = curr.get_next()
            # change the curr's next pointer to the prev
            # curr.set_next(prev)
            # increment logic
        #     prev = curr
        #     curr = next_node
        # self.head = prev
