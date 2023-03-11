import Utils.listUtils as utilities

backUp_list = [[]]
my_list = []

def lPrint():
    global my_list
    print(my_list)

def save():
    global my_list
    global backUp_list
    backUp_list += [my_list[:]]

def undo():
    global my_list
    global backUp_list
    my_list = backUp_list[-1][:]
    backUp_list.pop()




