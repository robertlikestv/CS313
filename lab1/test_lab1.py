import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")
    
    def test_enqueue_one_item(self):
        #test if enqueue works from an empty queue
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        self.assertEqual(q.__str__(), '[1]')
        print("\n")

    def test_dequeue_from_empty_error(self):
        #test if dequeing from an empty queue gives error
        print("\n")
        q = lab1.Queue()
        print("return false if doesn't return Null")
        self.assertEqual(q.dequeue(), None)
        print("\n")

class T1_TestingStack(unittest.TestCase):

    def test_is_empty_false(self):
        # testing if queue is empty
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")
    
    def test_pop_on_empty_error(self):
        #testing if error isn't given
        print("\n")
        s = lab1.Stack()
        print("return false if doesn't return Null")
        self.assertEqual(s.pop(), None)
        print("\n")
    
    def test_pop_on_one_item(self):
        #test if pops on one item
        print("\n")
        s = lab1.Stack()
        s.push("1")
        s.pop()
        print("return false if data doesn't pop properly")
        self.assertEqual(s.__str__(), "[]")
        print("\n")


class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string_false(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")

    def test_basic_string_true(self):
        # testing with basic string, but passes
        print("\n")
        string = "racecar"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")

    def test_capitals_string_true(self):
        # testing with capitals
        print("\n")
        string = "RaCecar"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")
    
    def test_spaces_string_true(self):
        # testing with spaces
        print("\n")
        string = "tac  ocat"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")
    
    def test_special_chars_string_false(self):
        # testing with special character not passing
        print("\n")
        string = "&$(^^)$&"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, False)
        print("\n")
    
    def test_nums_string_true(self):
        # testing with integers passing
        print("\n")
        string = "63488436"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")
    
    def test_required_string_true(self):
        # testing with required string from instructions
        print("\n")
        string = "TaCo CaT"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertEqual(p, True)
        print("\n")
    

if __name__ == '__main__':
    unittest.main()
