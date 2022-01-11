a= [1,2,3,4,5,6,3,5]
b= ["hello","abc","anh em mình:"]

# i sẽ lần lượt nhận các giá trị trong tập a
for i in a:
    print(i)
    "Ket qua: 1,2,3,4,5,6,3,5"
for j in b:
    print(j)
    "Kết quả là: hello , abc. anh em mình:"

c = "Anh yeu em"
for k in c:
    print(k)
print()
"Kết quả là: A,n,h,y,e,u,e,m (xuống dòng)"

d= range(2,7)
for f in d:
    print(f)
    "Kết quả là 2,3,4,5,6"

#################################3
" while"
tien = 50
while tien >= 0:
    print(tien)
    tien = tien - 10
print("Chết đói rồi")
"Kết quả :50,40,30,20,10,0 / Chết đói rồi"