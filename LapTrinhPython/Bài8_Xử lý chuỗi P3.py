a = "and abc akl and"

"Đếm số lần xuất hiện của chuỗi,kí tự nhỏ trong chuỗi to"
a1 = a.count("and")
print(a1) # 2
a2 = a.count('a',0,5)
print(a2)
"kết quả là 2 vì từ a0 đến a5 là a n d a"

"Tìm xem có xuất hiện chuỗi hay kí tự trong chuỗi to hay không"
a3 = a.find('n',0,5)
print(a3)
#  Trả về vị trí của kí tự đó trong chuỗi,nếu không có trả về giá trị -1
" kết quả = 1  "
a4= a.find("abc")
print(a4)
" Kết quả là 4 vì kí tự đầu của abc là a nằm ở vị trí a[4]"

"Dùng index giống find chỉ khác là khi không thấy thì báo lỗi"

" Kiểm tra xem có bắt đầu hay kết thúc bằng abc không"
a5 = a.startswith("abc")
a6 = a.endswith("abc",0,7)
print(a5)
"Kết quả False vì từ a[0] đến a[7] là and abc "
print(a6)
"kết quả True"
