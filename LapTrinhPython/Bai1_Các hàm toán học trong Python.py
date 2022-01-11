from math import* #khai báo tất cả Function trong thư viện math và có thể thay bằng mấy dong ở dưới
from math import ceil
from math import floor
from math import exp
from math import log
from random import random,randrange,uniform


print("Gia tri tuyet doi cua 3",abs(-3))

print ("lam tron 3,4: ",round(3.4))
print ("lam tron hai chu so sau dau phay: ",round(3.4444444,2))

print("Lam tron xuong 2,3 (kq la 2):", floor(2.3))
print("Lam tron len 2,3(kq la 3): ", ceil(2.3))

print("Tinh e mu 3", exp(3))

print("Logarit cua 100 co so 10 = ",log(100,10) )

A= max(3,5,2,7)
print("maxA=",A)
B= min(3,4,6,2)
print("minB=",B)

#Chon ngau nhien tu 0 den 1
C = random()
print("C=:",C)
#Chon tu 1 den 40
D= randrange(1,40)
print("D=:",D)
#Chon tu 1 den 40 voi buoc nhay la 3
E= randrange(1,40,3)
print("E=:",E)
#in ra ket qua ngau nhien nhung la so thuc
print("F=",uniform(3,6))

#hàm sin ,arcsin
print("Sin(pi)=",int(sin(pi)) )
print("arcSin(1)=",(asin(1)) )
print("Hàm đo độ",degrees(pi/2))
print("Canh huyen cua 3, 4:",hypot(3,4))
