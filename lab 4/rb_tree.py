class Node(object):
    """
    Represents a single node in a Red-Black Tree.

    Attributes:
        data (any): The value stored in the node.
        left (Node): The left child of the node.
        right (Node): The right child of the node.
        parent (Node): The parent of the node.
        color (str): The color of the node, either 'red' or 'black'.
    """
    def __init__(self, data, left=None, right=None, parent=None, color='red'):
        """
        Initializes a new Node object.

        Args:
            data (any): The value to be stored in the node.
            left (Node, optional): Reference to the left child. Defaults to None.
            right (Node, optional): Reference to the right child. Defaults to None.
            parent (Node, optional): Reference to the parent node. Defaults to None.
            color (str, optional): The color of the node. Defaults to 'red'.
        """
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class rb_tree(object):
    """
    Represents a Red-Black Tree, a self-balancing binary search tree.

    Attributes:
        PREORDER (int): Constant for preorder traversal.
        INORDER (int): Constant for inorder traversal.
        POSTORDER (int): Constant for postorder traversal.
        root (Node): The root node of the tree.
        sentinel (Node): The sentinel node used as a placeholder for null references.
    """
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        """
        Initializes a new Red-Black Tree with a sentinel node.
        """
        self.root = None
        self.sentinel = Node(None, color='black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel

    def print_tree(self):
        """
        Prints the values of the nodes in the tree in preorder traversal.
        """
        self.__print_tree(self.root)

    def __print_tree(self, curr_node):
        """
        Recursively prints the values of the subtree rooted at the given node.

        Args:
            curr_node (Node): The root of the current subtree.
        """
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        """
        Recursively prints the values of the subtree rooted at the given node,
        along with their colors.

        Args:
            curr_node (Node): The root of the current subtree.
        """
        if curr_node is not self.sentinel:
            if curr_node.color == "red":
                node_color = "R"
            else:
                node_color = "B"
            print(str(curr_node.data) + node_color, end=' ')
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        """
        Prints the values of all nodes in the tree in preorder traversal, including
        their colors.
        """
        self.__print_with_colors(self.root)

    def __iter__(self):
        """
        Returns an iterator for inorder traversal of the tree.

        Returns:
            generator: An iterator for the tree's nodes.
        """
        return self.inorder()

    def inorder(self):
        """
        Performs an inorder traversal of the tree.

        Returns:
            generator: An iterator for the nodes in inorder.
        """
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        """
        Performs a preorder traversal of the tree.

        Returns:
            generator: An iterator for the nodes in preorder.
        """
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        """
        Performs a postorder traversal of the tree.

        Returns:
            generator: An iterator for the nodes in postorder.
        """
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """
        Recursively traverses the tree in the specified order.

        Args:
            curr_node (Node): The current node being traversed.
            traversal_type (int): The type of traversal (PREORDER, INORDER, POSTORDER).

        Yields:
            Node: The next node in the traversal.
        """
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    def find_min(self, start_node=None):
        """
        Finds the minimum value node in the subtree rooted at the given node.

        Args:
            start_node (Node, optional): The root of the subtree. Defaults to None.

        Returns:
            Node: The node with the minimum value.
        """
        current_node = start_node if start_node else self.root
        while current_node.left is not self.sentinel:
            current_node = current_node.left
        return current_node

    def find_node(self, data):
        """
        Finds the node containing the specified data.

        Args:
            data (any): The value to search for in the tree.

        Returns:
            Node: The node containing the specified data.

        Raises:
            KeyError: If the data is not found in the tree or if the tree is empty.
        """
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    def __get(self, data, current_node):
        """
        Helper function to recursively find the node containing the specified data.

        Args:
            data (any): The value to search for.
            current_node (Node): The node currently being checked.

        Returns:
            Node: The node containing the data, or None if not found.
        """
        if current_node is self.sentinel:
            print(f"Couldn't find data: {data}")
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            return self.__get(data, current_node.left)
        else:
            return self.__get(data, current_node.right)

    def find_successor(self, data):
        """
        Finds the successor of the node containing the specified data.

        Args:
            data (any): The value whose successor is to be found.

        Returns:
            Node: The successor node, or None if no successor exists.

        Raises:
            KeyError: If the node with the given data is not found.
        """
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError("Node not found in the tree.")

        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        return successor if successor else None

    def insert(self, data):
        """
        Inserts a new node with the specified data into the tree.

        Args:
            data (any): The value to be added to the tree.
        """
        if self.root:
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else:
            self.root = Node(data, parent=self.sentinel, left=self.sentinel, right=self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)

    def bst_insert(self, data):
        """
        Inserts a new node into the tree following the Binary Search Tree (BST) rules
        without maintaining the Red-Black Tree properties.

        Args:
            data (any): The value to be added to the tree.
        """
        if self.root:
            self.__put(data, self.root)
        else:
            self.root = Node(data, parent=self.sentinel, left=self.sentinel, right=self.sentinel)

    def __put(self, data, current_node):
        """
        Helper function to recursively find the correct position for a new node.

        Args:
            data (any): The value to be added.
            current_node (Node): The node currently being checked.

        Returns:
            Node: The newly added node.
        """
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else:
                new_node = Node(data, parent=current_node, left=self.sentinel, right=self.sentinel)
                current_node.left = new_node
        else:
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else:
                new_node = Node(data, parent=current_node, left=self.sentinel, right=self.sentinel)
                current_node.right = new_node
        return new_node

    def left_rotate(self, x):
        """
        Performs a left rotation at the given node.

        Args:
            x (Node): The node at which to perform the rotation.

        Raises:
            KeyError: If the right child of the node is not valid.
        """
        y = x.right
        if y == self.sentinel:
            raise KeyError("Cannot left rotate without a valid right child.")
        
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x
        
        y.parent = x.parent
        if x.parent == self.sentinel:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        """
        Performs a right rotation at the given node.

        Args:
            y (Node): The node at which to perform the rotation.

        Raises:
            KeyError: If the left child of the node is not valid.
        """
        x = y.left
        if x == self.sentinel:
            raise KeyError("Cannot right rotate without a valid left child.")
        
        y.left = x.right
        if x.right != self.sentinel:
            x.right.parent = y
        
        x.parent = y.parent
        if y.parent == self.sentinel:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y
        y.parent = x

    def __rb_insert_fixup(self, z):
        """
        Restores the Red-Black Tree properties after an insertion.

        Args:
            z (Node): The newly inserted node.
        """
        while z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  

                # case 1
                if y.color == "red": 
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    # case 2
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    # case 3
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else: 
                y = z.parent.parent.left 
                # case 1
                if y.color == "red": 
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    # case 2
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    # case 3
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"

    def delete(self, data):
        """
        Deletes the node containing the specified data from the tree.

        Args:
            data (any): The value to be deleted.

        Raises:
            KeyError: If the node with the specified data is not found.
        """
        z = self.find_node(data)
        if z == self.sentinel:
            raise KeyError(f"Node with data {data} not found.")
        
        y = z
        y_original_color = y.color
        if z.left == self.sentinel:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.sentinel:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.find_min(start_node=z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == "black":
            self.__rb_delete_fixup(x)

    def __rb_delete_fixup(self, x):
        """
        Restores the Red-Black Tree properties after a deletion.

        Args:
            x (Node): The node that replaces the deleted node.
        """
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right

                # case 1
                if w.color == "red": 
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                
                # case 2
                if w.left.color == "black" and w.right.color == "black": 
                    w.color = "red"
                    x = x.parent
                else:
                    # case 3
                    if w.right.color == "black":  
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right

                    # Case 4
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else: 
                w = x.parent.left  

                # case 1
                if w.color == "red": 
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                
                # case 2
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    # case 3
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                        
                    # case 4
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def __rb_transplant(self, u, v):
        """
        Replaces one subtree as a child of its parent with another subtree.

        Args:
            u (Node): The node to be replaced.
            v (Node): The node to replace u.
        """
        if u.parent == self.sentinel:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent