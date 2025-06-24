# 7. Demonstrate Exceptions in Python 
try:
   print(10 / 0)
except Exception as e: 
    print("Error:", e)
finally:
    print("This will always execute.")