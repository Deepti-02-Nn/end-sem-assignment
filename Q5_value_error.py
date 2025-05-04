# Question 5: Value Error Handler
try:
    num = int("abc")
except ValueError as e:
    print(f"5. Caught a ValueError: {e}")
