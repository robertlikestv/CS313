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


class Stack(object):
    """Provide class dosctring"""
    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.__top = None


    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        resultStr = "["
        current_node = self.__top
        while current_node != None:
            resultStr += str(current_node.getData())
            current_node = current_node.getNext()
            if current_node != None:
                resultStr += ", "
        resultStr += "]"
        return resultStr

         

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top'''
        newNode = Node(newData, None)
        if self.isEmpty():
            self.__top = newNode
        else:
            newNode.setNext(self.__top)
            self.__top = newNode

    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.isEmpty():
            return None
        else:
            poppedNode = self.__top
            self.__top = poppedNode.getNext()
            return poppedNode.getData()


    def isEmpty(self):
        '''Check if the Stack is empty.'''
        if self.__top == None:
            return True
        return False


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.'''
    myStack = Stack()
    myQueue = Queue()
    flag = 0

   
    tempStack = Stack()
    tempQueue = Queue()
    

    #put s in tempStack
    for letter in s:
        #if letter is alphanumeric
        if letter.isalnum():
            #if letter is specifically a letter
            if letter.isalpha():
                #add lowercase version of letter to stack
                myStack.push(letter.lower())
            else:
                #if number, just add to stack
                myStack.push(letter)
        else:
            continue
    
    #put s in tempQueue
    for letter in s:
        #if letter is alphanumeric
        if letter.isalnum():
            #if letter is specifically a letter
            if letter.isalpha():
                #add lowercase version of letter to queue
                myQueue.enqueue(letter.lower())
            else:
                #if number, just add to queue
                myQueue.enqueue(letter)
    
    #if there is nothing left(aka there were no alphanumeric characters)
    if (myStack.isEmpty() == True) & (myQueue.isEmpty() == True):
        #set flag to one, which will return False at the end
        flag += 1

    #while not empty
    while (myStack.isEmpty() == False) & (myQueue.isEmpty() == False):
        #if data from pop (the end) and dequeue (the front) are equal
        if myStack.pop() == myQueue.dequeue():
            #continue to next letter
            continue
        else:
            #set flag to 1, which will fail the program at the end
            flag = 1
            break
    
    if flag > 0:
        return False
    return True



    
    
    ####BELOW IS AN IDEA I HAD THAT DIDN'T WORK...FOR THE BETTER
    '''
    currentNode = myStack.__top
    dataHolder = None

    #cycle through all nodes in tempStack    
    while currentNode != None:
        #if alphanumeric
        if currentNode.getData().isalnum():
            #set index/current node to next node
            currentNode = currentNode.getNext()
            #pop and hold data
            dataHolder = myStack.pop().getData()
            #if data is a letter
            if dataHolder.isalpha():
                #change letter to lowercase
                dataHolder.lower()
            #push data into tempStack
            tempStack.push(dataHolder) 
        else:
            #set index/current node to next node
            currentNode = currentNode.getNext()
            #pop node and don't save it to myStack in order to remove it
            myStack.pop()

    #pop everything back into myStack so it's in the right order
    #set currentNode to tempStack's top
    currentNode = tempStack.__top

    #while current node is not null
    while currentNode != None:
        #set current node to next node
        currentNode = currentNode.getNext()
        #pop and grab data
        dataHolder = tempStack.pop().getData()
        #store data back in myStack
        myStack.push(dataHolder)

    #reset vars for tempQueue
    currentNode = tempQueue.__head
    dataHolder = None

    #cycle through all nodes in tempQueue
    while currentNode:
        #if alphanumeric
        if currentNode.getData().isalnum():
            #set index/current node to next node
            currentNode = currentNode.getNext()
            #add to myQueue
            dataHolder = tempQueue.dequeue().getData()
            if dataHolder.isalpha():
                dataHolder.lower()
            myQueue.enqueue(dataHolder)
        else:
            #set index/current node to next node
            currentNode = currentNode.getNext()
            #dequeue without adding to myQueue
            tempQueue.dequeue()
    
    #now compare
    queueHead = myQueue.__head
    stackTop = myStack.__top
    flag = 0

    while queueHead != None:
        while stackTop != None:
            if queueHead.getData() == stackTop.getData():
                queueHead = queueHead.getNext()
                myQueue.dequeue()
                stackTop = stackTop.getNext()
                myStack.pop()
            else:
                flag += 1
                queueHead = queueHead.getNext()
                myQueue.dequeue()
                stackTop = stackTop.getNext()
                myStack.pop()
    
    if flag > 0:
        return False
    return True
    '''

    """
    while currentNode != None:
    #for all
        if char.isalnum() or char.isspace() or (char == ' '):
            #remove all non-abc & ints & spaces
            char.getData()
        else:
            char.getData()
    
    for char in myQueue:
        if char.isalnum() or char.isspace() or (char == ' '):
            myQueue.dequeue()
            #remove all non-abc & ints & spaces
    

    #for all

        #remove all non-abc & ints
        #remove all spaces
        #convert all to lowercase

    #check if palindrome
        #convert to two equal length strings and compare
        #compare popped characters to dequeued chars using a nested for
   
    ## Helper function ##
    print("stack data")
    myStack.printStack()

    print("queue data")
    myQueue.printQueue()

    # Return appropriate value
    return
    """
    

def isPalindromeEC(s):
    '''Implement if you wish to do the extra credit.'''

    # Return appropriate value
    return
