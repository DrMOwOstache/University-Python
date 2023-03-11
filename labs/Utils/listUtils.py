"""
A list of functions with different effects on a given list
"""
backUp = []

# 1
def add(l, val):
    """
    adds a variable to the end of the list
    :param l: the list of variable
    :param val: the value added
    :return: the modified list
    """
    return l[:] + [val]


def insert(l, ind, val):
    """
    adds a variable at a specific index
    :param l: the list of variable
    :param ind: the index where the value is inserted
    :param val: the value inserted
    :return: the modified list
    """
    try:
        if (ind < 0 or ind > len(l) - 1):
            raise IndexError("from_index is not a valid index")

        return l[:ind] + [val] + l[ind:]
    except IndexError:
        print("from_index is not a valid index")


# 2
def remove_element(l, from_index):
    """
    removes variables from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :return: the modified list
    """

    if (from_index < 0 or from_index > len(l) - 1):
        raise IndexError("from_index is not a valid index")

    return l[:from_index] + l[from_index + 1:]

def remove_interval(l, from_index, to_index):
    """
    removes variables from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :param to_index: end index
    :return: the modified list
    """

    if (from_index < 0 or from_index > len(l) - 1):
        raise IndexError("from_index is not a valid index")
    if (to_index < 0 or to_index > len(l) - 1):
        raise IndexError("to_index is not a valid index")

    return l[:from_index] + l[to_index + 1:]


def replace(l, old_value, new_value):
    """
    replace a variable at a given index
    :param l: the list of variable
    :param old_value: old variable
    :param new_value: new variable
    :return: the modified list
    """
    for i in range(len(l)):
        if (l[i] == old_value):
            l = l[:i] + [new_value] + l[i+1:]
    return l


# 3
def prime(l, from_index, to_index):
    """
    gets the list of prime numbers from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :param to_index: end index
    :return: the modified list
    """
    try:
        if from_index <= to_index:

            if (from_index < 0 or from_index > len(l) - 1):
                raise IndexError("from_index is not a valid index")
            if (to_index < 0 or to_index > len(l) - 1):
                raise IndexError("to_index is not a valid index")

            if ((l[from_index] * 10) % 10 > 0):
                return prime(l, from_index + 1, to_index)
            if l[from_index] < 2:
                return prime(l, from_index + 1, to_index)
            if l[from_index] == 2:
                return [l[from_index]] + prime(l, from_index + 1, to_index)
            if l[from_index] % 2 == 0:
                return prime(l, from_index + 1, to_index)
            i = 3
            while i * i <= l[from_index]:
                if l[from_index] % i == 0:
                    return prime(l, from_index + 1, to_index)
                i += 2
            return [l[from_index]] + prime(l, from_index + 1, to_index)
        return []

    except IndexError:
        print("%% One of the indexes are out of range %%")
        return ''

def odd(l, from_index, to_index):
    """
    gets the list of odd numbers from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :param to_index: end index
    :return: the modified list
    """
    try:
        if from_index <= to_index:
            if (from_index < 0 or from_index > len(l) - 1):
                raise IndexError("from_index is not a valid index")
            if (to_index < 0 or to_index > len(l) - 1):
                raise IndexError("to_index is not a valid index")

            if l[from_index] % 2 == 1:
                return [l[from_index]] + odd(l, from_index + 1, to_index)
            return odd(l, from_index + 1, to_index)
        return []

    except IndexError:
        print("%% One of the indexes are out of range %%")
        return ''

#4
def sequence_sum(l, from_index, to_index):
    """
    gets the sum of the numbers from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :param to_index: end index
    :return: the modified list
    """
    try:
        if (from_index < 0 or from_index > len(l) - 1):
            raise IndexError()
        if (to_index < 0 or to_index > len(l) - 1):
            raise IndexError()

        s = 0
        for i in l[from_index: to_index + 1]:
            s += i
        return s

    except IndexError:
        print("%% One of the indexes are out of range %%")
        return ''


def sequence_gcd(l, from_index, to_index):
    """
    gets the greatest common divisor of the numbers from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :param to_index: end index
    :return: the modified list
    """
    try:
        if (from_index < 0 or from_index > len(l) - 1):
            raise IndexError()
        if (to_index < 0 or to_index > len(l) - 1):
            raise IndexError()
        if ((l[from_index] * 10) % 10 > 0):
            raise TypeError()

        x = int(l[from_index])
        while(from_index < to_index):
            y = int(l[from_index + 1])
            if x < y:
                (x, y) = (y, x)

            if(y == 0):
                raise ZeroDivisionError()

            if ((l[from_index] * 10) % 10 > 0 or (l[from_index+1] * 10) % 10 > 0):
                raise TypeError()

            r = float(x % y)

            while r > 0:
                x = y
                y = r
                r = x % y
            x = y
            from_index += 1

        return y
    except IndexError:
        print("%% One of the indexes are out of range %%")
        return ''
    except TypeError:
        print("%% There is a value that can't be used in gcd %%")
        return ''
    except ZeroDivisionError:
        print("%% Cannot divide with o %%")
        return ''


def sequence_max(l, from_index, to_index):
    """
    gets the biggest number from a given index to another
    :param l: the list of variable
    :param from_index: begining index
    :param to_index: end index
    :return: the modified list
    """
    try:
        if(from_index < 0 or from_index > len(l)-1):
            raise IndexError("from_index is not a valid index")
        if (to_index < 0 or to_index > len(l) - 1):
            raise IndexError("to_index is not a valid index")

        maxi = l[from_index]
        for i in l[from_index + 1 : to_index + 1]:
            if maxi < i:
                maxi = i
        return maxi

    except IndexError:
        print("%% One of the indexes are out of range %%")
        return ''

def filter_prime(l):
    """
    returns all the prime numbers from a given list
    :param l: the list of variable
    :return: the modified list
    """
    return prime(l, 0, len(l)-1)

def filter_negative(l):
    """
    returns all the negative numbers from a given list
    :param l: the list of variable
    :return: the modified list
    """
    new_list = []
    for i in l:
        if i < 0:
            new_list += [i]
    return new_list



