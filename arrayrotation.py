
# n = size of array
# d = number by which we shift
# def rotate_array(arr, n, d):
#     temp = []
#     i = 0 
#     # add d items to temp array
#     while (i < d): 
#         temp.append(arr[i])
#         i += 1
#     i = 0 
#     # shift rest of the array
#     while (d < n): 
#         arr[i] = arr[d]
#         i = i + 1
#         d = d + 1
#     # store back d elements
#     print("arr slice is", arr[:])
#     print("arr[:i] is", arr[:i])
#     arr[:] = arr[:i] + temp
#     return arr

# arr = [1, 2, 3, 4, 5, 6, 7]
# print("Array after left rotation is: ", end=' ')
# print(rotate_array(arr, len(arr), 2))


# List slicing method
def rotateList(arr,d,n):
  print("arr[:]", arr[:])
  print("arr[d:n]", arr[d:n])
  print("arr[0:d]", arr[0:d])
  arr[:]=arr[d:n]+arr[0:d]
  return arr
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr))) 

    