" Object Oriented Programming "
" =>> Ta tạo ra kiểu dữ liệu riêng, và các hàm, phương thức riêng"
" x và y mà cùng kiểu dữ liệu thì sẽ có các phương thức riêng xử lý cho nó, nếu dùng phương thức trong kiểu dữ liệu khác thì sẽ lỗi"
" Cú pháp : class Tênđốiượng...........Ví dụ : class sinhvien "
"def: định nghĩa 1 hàm đầu tiên.............Ví dụ def _init_ "

class sinhvien:
    def __init__(self,hoten,ms_sv):
        self.name = hoten
        self.MS   = ms_sv
    def diemTB(self, *a) :
        if len(a)==0:
          diemtb = 0
        else:
            tong = 0
            for i in a:
                tong = tong + i
            diemtb =  tong / len(a)
        return diemtb
sv1 = sinhvien("anh",1234)
print(sv1.name)
print(MS)

" Lỗi "

