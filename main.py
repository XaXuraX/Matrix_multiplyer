a11 = int(input("Enter a11:"))
a12 = int(input("Enter a12:"))
a13 = int(input("Enter a13:"))
a21 = int(input("Enter a21:"))
a22 = int(input("Enter a22:"))
a23 = int(input("Enter a23:"))
a31 = int(input("Enter a31:"))
a32 = int(input("Enter a32:"))
a33 = int(input("Enter a33:"))
b11 = int(input("Enter b11:"))
b12 = int(input("Enter b12:"))
b13 = int(input("Enter b13:"))
b21 = int(input("Enter b21:"))
b22 = int(input("Enter b22:"))
b23 = int(input("Enter b23:"))
b31 = int(input("Enter b31:"))
b32 = int(input("Enter b32:"))
b33 = int(input("Enter b33:"))

A = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
B = [[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]]

print ("A=")
for i in A :
    print(i)
    
print("B=")
for j in B :
    print(j) 
    
r11 = a11*b11 + a12*b21 + a13 * b31
r12 = a11*b12 + a12*b22 + a13 * b32
r13 = a11*b13 + a12*b23 + a13 * b33
r21 = a21*b11 + a22*b21 + a23 * b31
r22 = a21*b12 + a22*b22 + a23 * b32
r23 = a21*b13 + a22*b23 + a23 * b33
r31 = a31*b11 + a32*b21 + a33 * b31
r32 = a31*b12 + a32*b22 + a33 * b32
r33 = a31*b13 + a32*b23 + a33 * b33

AB = [[r11,r12,r13],[r21,r22,r23],[r31,r32,r33]]
    
print("AB=")
for k in AB :
    print(k) 

