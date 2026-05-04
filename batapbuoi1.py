def hoandoi(a,b):
    print ("sau khi hoán đổi a={a}, b={b}")
def chuvihcn(chieudai,chieurong):
    print ("chu vi hcn la", (chieudai+chieurong)*2)
def trungbinhcong(a,b,c):
    print ("trung binh cong 3 so la",(a+b+c)/3)
def binhphuong(n):
    print ("binh phuong cua", n ,"la", n*n)
def chiahet(n):
    if n % 5 == 0 :
        print (n,"chia het cho 5")
    else :
        print(n,"khong chia het cho 5")
def doidonvi(c):
    f=c*1.8 +32
    print(c,"độ C = ",f,"độ F")
def noichuoi(ho,ten):
    
    print ("họ và tên la",{ho+ten})
def solonnhat(a,b):
    if a>b:
        print("so lon nhat la",a)
    elif a<b:
        print("so lon nhat la",b)
    else:
        print("hai so bang nhau")
def tienhang(soluong,dongia):
    tongtien=soluong*dongia
    print("tong tien la",tongtien)
def demkytu(s):
    print("so ki tu",{len(s)})

hoandoi(1,2)
chuvihcn(2,3)
trungbinhcong(1,2,4)
binhphuong(3)
chiahet(50)
doidonvi(4)
noichuoi("doan","quoc")
solonnhat(77,88)
tienhang(5,5000)
demkytu("hanin")
