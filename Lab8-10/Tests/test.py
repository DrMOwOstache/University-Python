import Utils.MyVector as vector
import numpy as py
import unittest as test

class VectorTests(test.TestCase):
    def setUp(self):
        self.__myList = vector.MyVector("dfq", 'r', 3, [1, 2, 3])
        self.__second = vector.MyVector("pop", 'g', 3, [4, 5, 5])

    def test_Vector(self):
        #print(self.__myList * self.__second)
        self.assertTrue((self.__myList + self.__second).values.all() == py.all(py.array([5, 7, 8])).all())
        self.assertTrue((self.__myList + 2).values.all() == py.array([3, 4, 5]).all())
        self.assertTrue((self.__myList - self.__second).values.all() == py.array([-3, -3, -2]).all())
        self.assertTrue((self.__myList * self.__second) == 29)

    def test_Reduction(self):
        self.assertEqual(self.__myList.sum, 6)
        self.assertEqual(self.__myList.prod, 6)
        self.assertEqual(self.__myList.avg, 2)
        self.__myList.values = [1, -2, 3]
        #print(self.__myList.values)
        self.assertEqual(self.__myList.min, -2)
        self.__myList.values = [1, 2, -3]
        self.assertEqual(self.__myList.max, 2)