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

print(binarySearchGtX(a, 4))
