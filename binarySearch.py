# binary search
a = [1, 2, 3, 4, 5, 6, 7]
def binarySearch(a, target):
    n = len(a)
    l = 0
    r = n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if target == a[mid]: 
            return a[mid]
        if a[mid] > target: 
            l = mid + 1
        else:
            r = mid - 1
    return -1 

# print(binarySearch(a, 9))

# find first value greater than or equal to x
a = [2, 3, 5, 6, 8, 12]

def binarySearchGtX(a, target):
    ans = -1  
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = l + (r - l) // 2
        print(a[mid])
        if a[mid] >= target:
            ans = a[mid]  
            r = mid - 1
        else:
            l = mid + 1 
    return ans

# print(binarySearchGtX(a, 4))

# Find the smallest element in a rotated sorted array
# Search in Rotated Sorted Array, https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
# This is the harder of two rotated-array problems in Leetcode.

a = [6 ,7, 15, 9, 2, 3]
def search(a, target): 
    # For each number we can check if we should go to the left/right by comparing it with target and with a[0]. 
    # Also, comparing target with a[0] tells us in which part (big or small numbers) the target is.
    n = len(a)
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == target:
            return mid # no need to store the answer, just return it

        # if the target is greater than the first index of the array
        # and the middle is greater than the target or the middle is less than the first index
        # or
        # target is less than first index and mid is less than first index and mid is greater than or equal to target
            # search left       
        if (target >= a[0] and 
            (a[mid] >= target or a[mid] < a[0])) or \
            (target < a[0] and (a[mid] < a[0] and a[mid] >= target)):
            right = mid - 1
        else:
            left = mid + 1
    return -1
print(search(a, 8))