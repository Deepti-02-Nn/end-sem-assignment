# Question 10: set2.py Module
def slen2(s):
    return len(s)

def adds2(x):
    s = set()
    s.add(x)
    return s

def remove2(x):
    s = {1, 2, 3, x}
    s.remove(x)
    return s
