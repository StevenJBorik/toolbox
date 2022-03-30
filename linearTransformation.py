
# Linear transformation of 2d matrix 
# x [a , c] + y [b , d]


v1 = [ 
        1,
        2
]

v2 = [
        3,
        4
     ]

x, y = any, any 

def transformation(v1, v2, x, y):
    v3 = [x, y]
    print(v3[0])
    print(v3[1])
    transV3 = [0] * 5
    transV3[0] = (v3[0] * v1[0]) + (v3[1] * v2[0]) 
    transV3[1] = (v3[0] * v1[1]) + (v3[1] * v2[1])
    return transV3

print(transformation(v1, v2, 1, 2))
