import numpy as py

class MyVector:

    def __init__(self, name_id, colour, type, values = []):
        """
        initializes the vector
        :param name_id: a string id
        :param colour: colour of the point
        :param type:
        :param values:
        """
        try:
            if self.__checkColour(colour) == False:
                raise TypeError("the colour does not belong to the predefined colours")
            self.__name_id = str(name_id)
            self.__colour = str(colour)
            self.__type = int(type)
            self.__values = py.array(values)
        except TypeError:
            raise TypeError("one of the values are not correct")

    @property
    def name_id(self):
        return self.__name_id

    @property
    def colour(self):
        return self.__colour

    @property
    def type(self):
        return self.__type

    @property
    def values(self):
        return self.__values

    @name_id.setter
    def name_id(self, other):
        self.__name_id = str(other)

    @colour.setter
    def colour(self, other):
        if self.__checkColour(other):
            self.__colour = str(other)
        else:
            raise TypeError(" colour is not correctly defined")

    @type.setter
    def type(self, other):
        self.__type = int(other)

    @values.setter
    def values(self, other = []):
        self.__values = py.array(other)

    def __checkColour(self, colour):
        """
        checks if the colour belongs to the accepted colours
        :param colour: the checked colour
        :return: true if the condition is checked
        """
        listColour = ['r','g','b','y','m']
        if colour in listColour:
            return True
        return False

    def __add__(self, other):
        """
        add a number or another vector to the existing vector
        :param other: a vector or an intiger
        :return: the sum of the two objects
        """
        if isinstance(other, MyVector):
            return MyVector(self.__name_id, self.__colour, self.__type, self.__values + other.__values)
        return MyVector(self.__name_id, self.__colour, self.__type, self.__values + other)

    def __sub__(self, other):
        """
        substracts a number or another vector from the existing vector
        :param other: a vector or an intiger
        :return: the subtraction's solution
        """
        if isinstance(other, MyVector):
            return MyVector(self.__name_id, self.__colour, self.__type, self.__values - other.__values)
        return MyVector(self.__name_id, self.__colour, self.__type, self.__values - other)

    def __mul__(self, other):
        """
        the dot product of two vectors of to vectors or the multiplication of a vector with a scalar
        :param other: a vector or an intiger
        :return: the product of the two objects
        """
        if isinstance(other, MyVector):
            return py.dot(self.__values, other.__values)
        return MyVector(self.__name_id, self.__colour, self.__type, self.__values * other.__values)

    @property
    def sum(self):
        return self.__values.sum()

    @property
    def prod(self):
        return self.__values.prod()

    @property
    def avg(self):
        return self.__values.sum()/self.__values.size
    @property
    def min(self):
        return self.__values.min()

    @property
    def max(self):
        return self.__values.max()




