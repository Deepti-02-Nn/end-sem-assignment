# Question 10: list1.py Module
def append1(x):
    l = []
    l.append(x)
    return l

def extend1(l):
    l2 = [4, 5, 6]
    l.extend(l2)
    return l

def pop0():
    l = [10, 20, 30]
    l.pop(0)
    return l

def remove1(x):
    l = [1, 2, 3, x]
    l.remove(x)
    return l
