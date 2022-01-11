"Các phương thức xử lý chuỗi - tiếp"
"Phương thức join - Nối chuỗi s1 bằng chuỗi s"

s = "---"
s1 = "Hom nay la T7"
s2 = ["Hôm","nay","la","T7"]
m1 = s.join(s1)
m2 = s.join(s2)

print(m1)
"H---o---m--- ---n---a---y--- ---l---a--- ---T---7"

print(m2)
"Hom---nay---la---T7"

print(m2.title())
"Hom---Nay---La---T7"
print(len(s))  # 3

"replace(old,ne,count) Thay thế kí tự trong chuỗi"
a = "Anh em oi anh em oi"
b = a.replace("em","emmmm")
print(b)
"Anh emmmm oi anh emmmm oi"

"s.strip(chars)  - loại bỏ kí tự chars ở 2 đầu chuỗi s"
"Ví dụ:"
sm = " Hom nay di hoc"
sn = sm.strip("hoc")
print("sn=",sn)
"Hom nay di"


