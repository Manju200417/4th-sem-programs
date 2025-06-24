# 6. Implement a sequential search

a = list(map(int,input("Enter a list of numbers separated by space: ").split()))
target = int(input("Enter a target number: "))
for i in range(len(a)):
    if target == a[i]:
        print(f"Yes, {target} is found at index {i}")
        break
else:
    print("target is not found in the list")
    
    
    
    
    
  
  
  
  
  
  
    
    
# def isFound(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# a = [2,4,7,9,3,35,6,57,46]

# target = int(input("Enter a Target number :"))
# result = isFound(a,target)
# if result != -1:
#     print(f"Yes At Index {result}")
# else : 
#     print("Not found")