" Split('char',số lần chia) --- cứ gặp kí tự 'char' thì chia chuỗi ,bỏ kí tự 'char' "

a = " các bạn này hôm nay lam gi the "
b = a.split('n',3)
print(b)
"[' các bạ', ' ', 'ày hôm ', 'ay lam gi the ']"
print(b[3])
"ay lam gi the "

#"Mã hóa : s.encode("utf-8 hoặc utf-16 hoặc utf-32") s// Giải mã s'.decode("utf-8 hoặc utf-16 hoặc utf-32")
s = "anh yeu em"
s5 = s.encode("utf-8")
s6 = s5.decode("utf-8")
print(s6)


print(s.isalpha())    # tất cả kí tự trong chuỗi là chữ - False vì có khoảng trống
print(s.isdecimal())  # tất cả kí tự trong chuỗi là chữ - False vì có khoảng trống