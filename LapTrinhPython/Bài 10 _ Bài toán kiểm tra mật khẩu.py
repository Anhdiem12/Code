"Tối thiểu 6 kí tự, tối đa 12 kí tự"
"Có ít nhất một chữ in hoa và 1 chữ thường"
"Có ít nhất một chữ só"
"Có ít nhất một kí tự đặc biệt @ $ # "

mk = input(" Nhập mật khẩu :")
kq = False
if (len(mk) >= 6 & len(mk)<=12):
  "isupper ()= : Tất cả là in hoa thì trả về True, islower(): Tất cả là chữ thường thì là false"
  if ( (mk.isupper() == False) & ( mk.islower()== False) ):
      for i in mk:
          if i.isdecimal()==True:
              kq1 = True
          if i == "@" or i == "#" or i== "&":
              kq2 = True
      if kq1== True & kq2 == True:
          kq=  True

if kq == False :
    print(" k Thỏa mãn")
else:
    print(" dc")

"DONE"