import Utils.listUtils as func

my_list = [1, 5, 6, 7, 3, 6, 4, 12, 13, 9, 3]

def testAdding():
    print("testing adding")
    assert func.add(my_list, 4) == my_list + [4]
    assert func.insert(my_list, 6, 5) == [1, 5, 6, 7, 3, 6, 5, 4, 12, 13, 9, 3]
    assert func.insert(my_list, 0, 10) == [10, 1, 5, 6, 7, 3, 6, 4, 12, 13, 9, 3]
    print("**DONE**")

def testModifyElements():
    print("testing modify elements")
    assert func.remove_element(my_list, 5) == [1, 5, 6, 7, 3, 4, 12, 13, 9, 3]
    assert func.remove_interval(my_list, 3, 8) == [1, 5, 6, 9, 3]
    assert func.replace(my_list, 3, 100) == [1, 5, 6, 7, 100, 6, 4, 12, 13, 9, 100]
    print("**DONE**")

def testGetNumbers():
    print("testing get numbers")
    assert func.prime(my_list,3,8) == [7, 3, 13]
    assert func.prime(my_list, 5, 6) == []
    assert func.odd(my_list, 0, len(my_list)-1) == [1, 5, 7, 3, 13, 9, 3]
    print("**DONE**")

def testObtainDifChara():
    print("testing obtain different characteristics from sub-arrays")
    assert func.sequence_sum(my_list, 6, 9) == 4 + 12 + 13 + 9
    assert func.sequence_gcd(my_list, 5, 7) == 2
    assert func.sequence_max(my_list, 2, 9) == 13
    assert func.sequence_max([-1, -10, -100, -24125, -45],0,4) == -1
    print("**DONE**")

def testFilter():
    print("testing filter values")
    assert func.filter_prime(my_list) == [5, 7, 3, 13, 3]
    assert func.filter_negative(my_list) == []
    assert func.filter_negative([-1,2,3,-20]) == [-1,-20]
    print("**DONE**")

#[1, 5, 6, 7, 3, 6, 4, 12, 13, 9, 3]
if __name__ == "__main__":
    testAdding()
    testModifyElements()
    testGetNumbers()
    testObtainDifChara()
    testFilter()