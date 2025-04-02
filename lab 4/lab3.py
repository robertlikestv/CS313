class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    '''
    Represents an int binary tree

    Attributes:
        root: pointer to the root node in the tree, defaults to none

    Methods:
        print(): prints all nodes in order
        insert(int): inserts a new node with given int
        min(): returns the minimum value in tree
        max(): returns the maximum value in tree
        __find_node(int): returns the node with the given int value
        contains(int): checks if tree has a node with given int value
        inorder(): prints nodes using inorder (left, root, right)
        preorder(): prints nodes using preorder (root, left, right)
        postorder(): prints nodes using postorder (left, right, root)
        find_successor(int): finds the next smallest int in the tree 
            that's larger than the given int
        delete(int): deletes a node with the given int as data, and 
            replaces it with it's successor if needed
    
    '''
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        new = Node(data)
        parent = None
        current = self.root

        while current is not None:
            parent = current
            if new.data < current.data:
                current = current.left
            else:
                current = current.right
        
        new.parent = parent
        
        if parent is None:
            self.root = new
        elif new.data < parent.data:
            parent.left = new
        else:
            parent.right = new
                

    def min(self):
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        current = self.root
        while current.left is not None:
            current = current.left
        
        return current.data


    def max(self):
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        current = self.root
        while current.right is not None:
            current = current.right
        
        return current.data

    def __find_node(self, data):
        # returns the node with that particular data value else returns None
        current = self.root

        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        
        return None
    
    def test_find_node(self, data):
        # tests the find node method
        return self.__find_node(data)

    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        if self.__find_node(data) is not None:
            return True
        return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        # helper method implemented using generators
        # all the traversals can be implemented using a single method
        
        #Yield data of the correct node/s
        if traversal_type == Tree.INORDER:
            if curr_node is not None:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)

        if traversal_type == Tree.PREORDER:
            if curr_node is not None:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)

        if traversal_type == Tree.POSTORDER:
            if curr_node is not None:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data

    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None

        parent = self.__find_node(data)
        if parent is None:
            return KeyError

        #if right subtree exists
        if parent.right is not None:    
            current = parent.right
            while current.left is not None:
                current = current.left
            return current
        
        #if right subtree doesn't exist
        else:
            while parent is not None:
                current = parent
                parent = parent.parent
                #if current is a left child of a parent node
                if current == parent.left:
                    return parent
        return None

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
    
        deleted = self.__find_node(data)
        parent = deleted.parent
        if deleted is None:
            return KeyError
        
        #if root, want successor, but not guarenteed a sucessor
        elif parent is None:
            if deleted.left is None and deleted.right is None:
                self.root = None
            if deleted.left is not None and deleted.right is None:
                self.root = deleted.left
            if deleted.right is not None and deleted.left is None:
                self.root = deleted.right
            if deleted.left is not None and deleted.right is not None:
                successor = self.find_successor(deleted.data)
                temp_data = successor.data
                self.delete(successor.data)
                deleted.data = temp_data
        
        #a)
        elif deleted.left is None and deleted.right is None:
            if parent.left == deleted:
                parent.left = None
            if parent.right == deleted:
                parent.right = None
        
        #b)
        #if deleted has just a left child
        elif deleted.left is not None and deleted.right is None:
            deleted.left.parent = parent
            #if deleted is a left child, change deleted's parent's left child to deleted's left child
            if parent.left == deleted:
                parent.left = deleted.left
            #if deleted is a right child, change deleted's parent's right child to deleted's left child
            elif parent.right == deleted:
                parent.right = deleted.left

        #if deleted has just a right child
        elif deleted.right is not None and deleted.left is None:
            deleted.right.parent = parent
            #if deleted is a left child, change deleted's parent's left child to deleted's right child
            if parent.left == deleted:
                parent.left = deleted.right
            #if deleted is a right child, change deleted's parent's right child to deleted's right child
            elif parent.right == deleted:
                parent.right = deleted.right

        #c)
        else:
            successor = self.find_successor(deleted.data)
            temp_data = successor.data
            self.delete(successor.data)
            deleted.data = temp_data
