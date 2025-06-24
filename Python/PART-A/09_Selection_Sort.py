a = list(map(int,input("Enter Unsorted list :").split()))
n = len(a)

for i in range(n):
    min = i
    for j in range(i+1,n):
        if a[j] < a[min]:
            min =  j

    a[i],a[min] = a[min],a[i]
    
print(a)












# Program to implement Selection Sort
# arr = [64, 25, 12, 22, 11]
# n = len(arr)

# # Selection Sort logic
# for i in range(n):
#     min_idx = i
#     for j in range(i+1, n):
#         if arr[j] < arr[min_idx]:
#             min_idx = j

#     # Swap the found minimum element with the first element
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# print("Sorted array:", arr)