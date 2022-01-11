#Toan tu va
x = 3&5
"3= 0000 0011"
"5= 0000 0101"
"do do ket qua bang 1"
print(x)
#Toan tu luy thua y = 2^3
y = 2**3
print("Y =", y)
#Toan tu dich bit
z1 = x<<2
print("z1=",z1)
" Vi x= 1 = 0000 0001 ,x dich sang trai 2 bit nen z= 0000 0100 = 4 "
z2 = x>>2
print("z2=",z2)
" Vi x= 1 = 0000 0001 ,x dich sang phai 2 bit nen z= 0000 0000 = 0 "

#Toan tu dong nhat-so sanh,ket qua tra ve la True or False
a= 1234
b= 2736
c= a is b
print(c) # ket qua la False
