# Question 6: Attribute Error Handler
try:
    number = 42
    number.append(5)
except AttributeError as e:
    print(f"6. Caught an AttributeError: {e}")
