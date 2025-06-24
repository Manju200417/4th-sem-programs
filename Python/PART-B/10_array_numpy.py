#10. Create Array using Num Py and Perform Operations on Array 
import numpy as np

# Create array
a = np.array([50,40,30,20,10])

# Operations
print("Original Array:", a)
print("Add 5:", a + 5)
print("Multiply by 2:", a * 2)
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Sum:", np.sum(a))
print("Sort:", np.sort(a))
print("Square Root:", np.sqrt(a))
print("Array Data Type:", a.dtype)
print("Array Size:", a.size)
print("Array Dimension:", a.ndim)