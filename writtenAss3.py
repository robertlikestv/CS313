import time

class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data = data

    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''
        self.__next_node = next_node

    def getData(self):
        '''Return the "data" data field.'''
        return self.__data

    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """Provide class dosctring"""
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.'''
        resultStr = "["
        current_node = self.__head
        while current_node != None:
            resultStr += str(current_node.getData())
            current_node = current_node.getNext()
            if current_node != None:
                resultStr += ", "
        resultStr += "]"
        return resultStr

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail.'''
        # Hint: Think about what's different for the first node added to the Queue
        newNode = Node(newData, None)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode


    def dequeue(self):
        '''Return the head of the Queue
        Update head.'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            return None
        else:
            tempNode = self.__head
            self.__head = tempNode.getNext()
            return tempNode.getData()


    def isEmpty(self):
        '''Check if the Queue is empty.'''
        if self.__head == None:
            return True
        return False
    
    def push(self, newData):
        start = time.time()
        self.enqueue(newData)
        end = time.time()
        print("Push time elapsed: ", start-end)

    def pop(self):
        start = time.time()
        tempQ = Queue()
        #FIXME: set as self.__q.__head
        #current_node = self.__head
        if self.__head != None:
            while self.__head.getNext() != None:
                tempQ.enqueue(current_node)
                current_node = self.dequeue()
            self = tempQ
        end = time.time()
        print("Pop time elapsed: ", start-end)
        return current_node

"""
#FIXME: Turn into a child of Queue
class Qstack(Queue):

    def push(self, newData):
        start = time.time()
        self.enqueue(newData)
        end = time.time()
        print("Push time elapsed: ", start-end)

    def pop(self):
        start = time.time()
        tempQ = Qstack()
        #FIXME: set as self.__q.__head
        current_node = self.__head
        while current_node.getNext() != None:
            tempQ.enqueue(current_node)
            current_node = self.dequeue()
        self = tempQ
        end = time.time()
        print("Pop time elapsed: ", start-end)
        return current_node
"""

q = Queue()
for i in range(10):
    q.push(i)

for i in range(10):
    q.pop()