# Question 12: m5.py (without using __init__.py)
from package_name import list1
from package_name import set2
from package_name import dict3

print("append1:", list1.append1(5))
print("extend1:", list1.extend1([1, 2, 3]))
print("pop0:", list1.pop0())
print("remove1:", list1.remove1(3))

print("\nslen2:", set2.slen2({1, 2, 3}))
print("adds2:", set2.adds2(10))
print("remove2:", set2.remove2(2))

print("\nlen3:", dict3.len3({'x': 100, 'y': 200}))
print("add3:", dict3.add3('name', 'Alice'))
print("keys3:", dict3.keys3())
print("values3:", dict3.values3())
