
# Linear transformation of 2d matrix 
# x [a , c] + y [b , d]
# result = linear combination matrix transformation

# 2nd dev - matrix multiplication as composition

m1 = [ 
        1, 2,
        3, 4
]

m2 = [
        5, 6,
        7, 8
     ]




def transformation(m1, m2):
    output = [0] * 4
    
    output[0] = (m1[0] * m2[0]) + (m1[2] * m2[1]) 
    output[1] = (m1[1] + m2[0]) + (m1[3] * m2[1])
    output[2] = (m1[0] * m2[2]) + (m1[2] * m2[3])
    output[3] = (m1[1] * m2[2]) + (m1[3] * m2[3])
    
    return output

print(transformation(m1, m2))

