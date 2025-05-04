# Question 2: Name Error Handler
try:
    print(unknown_variable)
except NameError as e:
    print(f"2. Caught a NameError: {e}")
