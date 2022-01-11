"Chọn một kí tự bất kì trong chuỗi"
from random import choice
s = choice("abchs")
print(s)


a= "anh129"

"Căn lề giữa"
b= a.center(20,"*")
print(b)
# kq la : *******anh129******* gồm 20 kí tự

"Căn lề trái"
c= a.ljust(20,"#")
print(c)
"Kết quả là :anh129##############"

"Căn lề phải"
d= a.rjust(20,"#")
print(d)
"Kết quẩ là : #############anh129"

"Tạo chuỗi mới có chữ cái đầu viết hoa:"
e = a.capitalize()
print(e) # Anh129

"Tạo chuỗi mới là chữ thường"
m= 'ABC'
print("m=",m.lower()) # kết quả là abc

"Đảo chữ in hoa sang thường và ngược lại"
n= m.swapcase()
print("n=",n)   # Kết quả là : abc

"Viết chữ hoa đầu mỗi chuỗi"
z = " Anh diem nguyen Van 129"
z1 = z.title()
print(z1)
"kết quả là : Anh Diem Nguyen Van 129"






