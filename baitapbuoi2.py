def kiemtra():
    n=int(input("nhap so nguyen"))
    if n>0:
        print ("n la so duong")
    elif n<0:
        print ("n la so am")
    else :
        print ("n bang 0")
def kiemtratuoi():
    n=int(input("nhap tuoi"))
    if n > 18:
        print("Adult")
    else:
        print("Minor")
def chuyensonguyen():
    so_thuc = float(input("nhap so thuc"))
    print("so sau khi chuyen doi la",int(so_thuc))
def nhapsonguyen(n):
 n=input("nhap so nguyen")
 if n.isdigit():
     print("so nguyen hop le",int(n))
 else:
     print("please enter a valid number")
def kiemtrasonguyento():
    n=int(input("nhap so nguyen to"))
    songuyento = True
    if n < 2:
        songuyento=False
    else:
        for i in range(2,n):
            if n % i == 0:
                songuyento=False
                break
    if songuyento:
        print("la so nguyen to")
    else:
        print("khong phai so nguyen to")
def demsophantu():
    danhsach = [1,2,3,4,5]
    print("so phan tu trong danh sach la",len(danhsach))
def giatrilonnhat(n):
    danhsach =[3,4,5,6]
    print("so lon nhat",max(danhsach))
def themphantu():
    danhsach = [1,2,4,9]
    them_so = int(input("nhap so moi :"))
    danhsach.append(them_so)
    print("danh sach:",danhsach)
def inphantuthu3():
    danhsach = ["A","B","C","D","E"]
    print("phan tu thu 3 cua danh sach la",danhsach[2])
def tentuoi():
    tentuoi={ "ten" : "doan kinh quoc","tuoi" : 20}
    print ("ten:",tentuoi["ten"])
    print ("tuoi:",tentuoi["tuoi"])
def diemhocsinh():
    diem={"vinh":10,"nghia":9,"toan" : 8}
    print("diem cua vinh",diem["vinh"])
def incacso():
    for i in range (1,11):
        print (i)
def insochan():
    i=0
    while i<=20:
        print(i)
        i += 2

insochan()
nhapsonguyen()