import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")

class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

class T6_build_heap(unittest.TestCase):

    def test_build_heap(self):
        print("\n")
        input_data = [5, 10, 6, 2, 7]
        heap = mheap.max_heap(data=input_data)
        heap.build_heap()

        self.assertEqual(heap.get_heap(), [10, 7, 6, 2, 5])
        print("\n")

class T7_check_index_err(unittest.TestCase):

    def test_check_index_err(self):
        print("\n")
        input_data = [5, 10, 6, 2, 7]
        heap = mheap.max_heap(5, input_data)
        
        with self.assertRaises(IndexError):
            heap.insert(3)
        print("\n")

class T8_check_key_err(unittest.TestCase):

    def test_check_key_err(self):
        print("\n")
        heap = mheap.max_heap()

        with self.assertRaises(KeyError):
            heap.extract_max()

class T9_test_valid_insert_to_max(unittest.TestCase):
    
    def test_valid_insert_to_max(self):
        print("\n")
        #input_data = [5, 10, 6, 2, 7]
        queue = pqueue.pqueue(5)
        queue.insert(5)
        queue.insert(10)
        queue.insert(6)
        queue.insert(2)
        queue.insert(7)
        max = queue.extract_max()

        self.assertEqual(queue.pheap.get_heap(), [7, 5, 6, 2])
        print("\n")

#1
class T10_pqueue_is_empty_false(unittest.TestCase):

    def test_pq_is_empty_false(self):
        print("check if pqueue is empty")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.is_empty(), False)
        print("\n")

#2
class T11_pqueue_is_empty_true(unittest.TestCase):

    def test_pq_is_empty_true(self):
        print("check if pqueue is empty")
        print("\n")
        pq = pqueue.pqueue(5)
        self.assertEqual(pq.is_empty(), True)
        print("\n")

#3
class T12_get_heap(unittest.TestCase):

    def test_get_heap(self):
        print("check get heap returns properly")
        print("\n")
        heap = mheap.max_heap(3, [1, 2, 3])
        self.assertEqual(heap.get_heap(), [1, 2, 3])
        print("\n")

#4
class T13_sort_empty(unittest.TestCase):

    def test_sort_empty(self):
        print("check no errors occur when sorting an empty heap")
        print("\n")
        heap = mheap.max_heap()

        with self.assertRaises(KeyError):
            heap.sort_in_place()

#5
class T14_build_heap(unittest.TestCase):

    def test_build_heap_2(self):
        print("\n")
        input_data = [3, 1, 4, 8, 2]
        heap = mheap.max_heap(data=input_data)
        heap.build_heap()

        self.assertEqual(heap.get_heap(), [8, 3, 4, 1, 2])
        print("\n")

#6
class T15_build_heap(unittest.TestCase):

    def test_build_heap_2(self):
        print("\n")
        input_data = [7, 9, 1, 5, 3]
        heap = mheap.max_heap(data=input_data)
        heap.build_heap()

        self.assertEqual(heap.get_heap(), [9, 7, 1, 5, 3])
        print("\n")
    
if __name__ == '__main__':
    unittest.main()