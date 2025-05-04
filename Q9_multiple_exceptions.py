# Question 9: Multiple Exception Handler
try:
    value = int("hello")
    print(my_list[10])
    print(undefined_variable)
except (ValueError, IndexError, NameError) as e:
    print(f"9. Caught an error (ValueError, IndexError, or NameError): {e}")
