# Question 7: File Not Found Error Handler
try:
    with open("non_existing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"7. Caught a FileNotFoundError: {e}")
