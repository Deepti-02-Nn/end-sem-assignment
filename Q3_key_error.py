# Question 3: Key Error Handler
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print(f"3. Caught a KeyError: {e}")
