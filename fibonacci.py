# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(10))


# a = 0 
# b = 1
# n = int(input("Enter the # of terms in sequence: "))
# print(a,b,end=" ")

# while(n - 2):
#     c = a + b
#     a, b = b, c
#     print(c, end=" ")
#     n = n-1

def nthfib(n):
    a, b = 0,1
    for i in range(n): 
        print(a, b)
        a, b = b, a+b
    return a

print(nthfib(4))