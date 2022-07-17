import unittest
import ArrayStack




class TestArrayStack(unittest.TestCase):

    def test_add(self):
        stack = ArrayStack.ArrayStack()
        stack.push(1)
        result = stack.size()
        self.assertEqual(result, 1) 

    def test_add_order(self):
        stack = ArrayStack.ArrayStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        result1 = stack.get(0)
        result2 = stack.get(1)
        result3 = stack.get(2)
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 3)

    def test_resize(self):
        stack = ArrayStack.ArrayStack()
        for i in range(20):
            stack.push(1)

        size = stack.size()
        self.assertNotEqual(size, len(stack.a))
        self.assertLess(size, len(stack.a))

    def test_remove(self):
        stack = ArrayStack.ArrayStack()
        stack.push(1)
        value = stack.pop()
        size = stack.size()
        self.assertEqual(value, 1)
        self.assertEqual(size, 0)
        with self.assertRaises(IndexError):
            stack.pop()
   
    def test_remove_order(self):
        stack = ArrayStack.ArrayStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        value1 = stack.pop()
        value2 = stack.pop()
        value3 = stack.pop()
        value4 = stack.pop()
        value5 = stack.pop()
        self.assertEqual(value1, 5)
        self.assertEqual(value2, 4)
        self.assertEqual(value3, 3)
        self.assertEqual(value4, 2)
        self.assertEqual(value5, 1)

if __name__ == "__main__":
    unittest.main()
