s= "abcde"
print(s[2])    # kq :c
print(s[2:4])  # in ra cd
print(s[:3])   # in ra abc
print(s[2:])   # in ra cde
print(s*3)     # in ra : abcdeabcdeabcde
print(s + "xy")  # in ra abcdexy

" Các hàm xử lý chuỗi :"
" chr(tạo ra một kí tự từ mã ASCII) , repr(tạo ra đối tượng có kiểu dữ liệu bất kì ra đối tượng mới giống hệt nó nhưng có kiểu Strings"
"str(tạo ra đối tượng từ 1 đối tượng có kiểu strings  sang đối tượng mới giống hệt nó cũng có kiểu Strings)"
c = 65
print(type(c))          # Thuộc lớp int
print(chr(c))           # Kí tự tương ứng là : A
print(type(chr(c)))     # thuộc lớp  string

d = "abd"
print (d)
print(type(d))          # Thuộc lớp int
print(repr(d))           # Kí tự tương ứng là : 'abd'
print(type(repr(d)))


