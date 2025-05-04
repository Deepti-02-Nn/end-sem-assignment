# Question 8: Module Not Found Error Handler
try:
    import non_existing_module
except ModuleNotFoundError as e:
    print(f"8. Caught a ModuleNotFoundError: {e}")
