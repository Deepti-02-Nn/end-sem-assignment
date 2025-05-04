# Question 1: Zero Division Error Handler
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"1. Caught a ZeroDivisionError: {e}")
