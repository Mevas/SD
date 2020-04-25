class Node:
    def __init__(self, value):
        self.value = value

        self.parent = None
        self.child = None
        self.left = None
        self.right = None

        self.degree = 0

    def __str__(self):
        return str(self.value)


class FibonacciHeap:
    root_list = None
    min_node = None
    total_nodes = 0

    def __str__(self):
        return f'Heap ({self.total_nodes} nodes) - Root: {" -> ".join([str(node.value) for node in self.iterate_list(self.root_list)]) if self.total_nodes else "Empty"}'

    # Insert a new value into the heap
    def insert(self, value):
        # Create a new Node instance
        node = Node(value)
        node.left = node.right = node

        self.merge_with_root_list(node)

        # Check if the new node is smaller than the current minimum
        if self.min_node is None or node.value < self.min_node.value:
            self.min_node = node

        # Keeping track of total nodes
        self.total_nodes += 1
        return node

    # Return but DON'T remove the minimum node
    def find_min(self):
        return self.min_node

    # Return AND remove the minimum node
    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                # Attach child nodes to parent list
                children = list(self.iterate_list(min_node.child))
                for node in children:
                    self.merge_with_root_list(node)
                    node.parent = None

            # Remove the node
            self.remove_from_root_list(min_node)

            # Set the new min node in the heap
            if min_node == min_node.right:
                self.min_node = self.root_list = None
            else:
                self.min_node = min_node.right
                self.consolidate()

            # Keeping track of total nodes
            self.total_nodes -= 1

        return min_node

    # Merge two fibonacci heaps by concatenating the root lists and then adjusting the minimum node accordingly
    def merge(self, heap_to_merge):
        # Initialize the new heap
        merged_heap = FibonacciHeap()
        merged_heap.root_list, merged_heap.min_node = self.root_list, self.min_node

        # Adjust pointers when merging the two heaps
        last = heap_to_merge.root_list.left
        heap_to_merge.root_list.left = merged_heap.root_list.left
        merged_heap.root_list.left.right = heap_to_merge.root_list
        merged_heap.root_list.left = last
        merged_heap.root_list.left.right = merged_heap.root_list

        # Update the minimum node
        if heap_to_merge.min_node.value < merged_heap.min_node.value:
            merged_heap.min_node = heap_to_merge.min_node

        # Update total nodes
        merged_heap.total_nodes = self.total_nodes + heap_to_merge.total_nodes

        return merged_heap

    def consolidate(self):
        consolidated = [None] * self.total_nodes
        nodes = list(self.iterate_list(self.root_list))

        # Combine nodes of equal degree to consolidate the heap
        for node in nodes:
            degree = node.degree
            while consolidated[degree] is not None:
                cons_node = consolidated[degree]

                if node.value > cons_node.value:
                    temp = node
                    node, cons_node = cons_node, temp

                self.heap_link(cons_node, node)

                consolidated[degree] = None
                degree += 1
            consolidated[degree] = node

        # Find new minimum in the consolidated heap
        for node in consolidated:
            if node is None:
                continue

            if node.value < self.min_node.value:
                self.min_node = node

    # Function to link a node to another in the root list and update child list
    def heap_link(self, node1, parent):
        self.remove_from_root_list(node1)
        node1.left = node1.right = node1
        self.merge_with_child_list(parent, node1)
        parent.degree += 1
        node1.parent = parent

    # ---------------------------- #
    # DOUBLE LINKED LIST FUNCTIONS #
    # ---------------------------- #

    def iterate_list(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right

    # Merge a node with the child list of a parent node
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
            return

        node.right = parent.child.right
        node.left = parent.child
        parent.child.right.left = node
        parent.child.right = node

    # Remove a node from the parent list
    def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right

        node.left.right = node.right
        node.right.left = node.left

    # Merge a node with the parent list
    def merge_with_root_list(self, node):
        if self.root_list is None:
            self.root_list = node
            return

        node.right = self.root_list.right
        node.left = self.root_list
        self.root_list.right.left = node
        self.root_list.right = node

