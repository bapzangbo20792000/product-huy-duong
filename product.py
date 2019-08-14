#product
hanghoa={
'tenhang':'',
'dongia':'',
'soluong':'',
'thanhtien':''
}
khachhang={
'tenkhachhang':'',
'ngayhoadon':'',
'sohoadon':'',
'hangdamua':'',
'tongtien':''
}
hoadon=[]
listkhachhang=[] #lu tru nhieu hoa don cua nhieu khach hang
def NhapKhachhang(khachhang):
    khachhang['tenkhachhang']=input('nhap ten khach hang ')
    khachhang['ngayhoadon']=int(input('nhap ngay hoa don( nhap so) '))
    khachhang['sohoadon']=input('nhap so hoa don ')
def NhapHangHoa(hanghoa):
    hanghoa['tenhang']=input('nhap ten hang ')
    hanghoa['dongia']=int(input('nhap don gia( nhap so) '))
    hanghoa['soluong']=int(input('nhap so luong( nhap so) '))
    hanghoa['thanhtien']=hanghoa['dongia']*hanghoa['soluong']
def InHoaDon(thongtinhoadon):
    STT=0
    print('\33[93mso hoa don: '+str(thongtinhoadon['sohoadon']))
    print('ngay hoa don: '+str(thongtinhoadon['ngayhoadon']))
    print('ten khach hang: '+str(thongtinhoadon['tenkhachhang']))
    print('+-----+--------------+----------+---------+------------+')
    print('| STT | TEN HANG HOA | SO LUONG | DON GIA | THANH TIEN |')
    print('+-----+--------------+----------+---------+------------+')
    for hanghoa in thongtinhoadon['hangdamua']:
        STT+=1
        print('|'+str(STT).rjust(5,' ')+'|'+str(hanghoa['tenhang']).rjust(14,' ')+'|'+str(hanghoa['soluong']).rjust(10,' ')+'|'+str(hanghoa['dongia']).rjust(9,' ')+'|'+str(hanghoa['thanhtien']).rjust(12,' ')+'|')
        print('+-----+--------------+----------+---------+------------+')
    print('|                               TONG TIEN |'+str(thongtinhoadon['tongtien']).rjust(12,' ')+'|')
    print('+-----+--------------+----------+---------+------------+')
    print('               -- design by huy duong --                ')
def TongTien(hoadon):
    tongtien=0
    for thanhtien in hoadon:
        tongtien+=thanhtien['thanhtien']
    return tongtien
def TinhDoanhThuTheoNgay(a,b,listkhachhang):
    doanhthu=0
    for ngay in listkhachhang:
        if (int(a)<=ngay['ngayhoadon']<=int(b)):doanhthu+=int(ngay['tongtien'])
    return  doanhthu

def Nhap1HoaDon(khachhang,hoadon):
    NhapKhachhang(khachhang)
    while True:
        NhapHangHoa(hanghoa)
        hoadon.append(hanghoa.copy())
        print('\33[92mban co muon nhap nua khong( an k de thoat)')
        chon = input()
        if chon == 'k': break
def TimSoLuongSanPham(listkhachhang,tensp):
    soluong=0
    for listkh in listkhachhang:
        for dictkh in listkh['hangdamua']:
            if dictkh['tenhang']==tensp:
                soluong+=dictkh['soluong']
    return  soluong
def menu():
    print('+---------------------------------------+----+')
    print('|nhap hoa don                           | 1  |')
    print('|---------------------------------------+----+')
    print('|nhap them hoa don                      | 2  |')
    print('|---------------------------------------+----+')
    print('|tinh doanh thu tu ngay a den ngay b    | 3  |')
    print('|---------------------------------------+----+')
    print('|tinh tong tien cho khach hang          | 4  |')
    print('|---------------------------------------+----+')
    print('|tinh so luong san pham ban ra          | 5  |')
    print('|---------------------------------------+----+')
    print('|in hoa don                             | 6  |')
    print('|---------------------------------------+----+')
    print('|ket thuc                               | 7  |')
    print('+---------------------------------------+----+')
while True:
    menu()
    chon = int(input('\33[92mnhap lua chon cua ban vao day: '))
    if chon == 1or chon==2:
        Nhap1HoaDon(khachhang, hoadon)
        khachhang['tongtien'] = TongTien(hoadon)
        khachhang['hangdamua'] = hoadon * 1
        listkhachhang.append(khachhang.copy())
        hoadon.clear()
    elif chon==3:
        ngaybatdau=input('nhap ngay bat dau ')
        ngayketthuc=input('nhap ngay ket thuc ')
        print('\n\33[96mdoanh thu tu ngay '+str(ngaybatdau)+' den ngay '+str(ngayketthuc)+' la: '+str(TinhDoanhThuTheoNgay(ngaybatdau,ngayketthuc,listkhachhang))+'\n')
    elif chon==4:
        tenkhachhang=input('nhap ten khach hang can tinh tien ')
        for idx in listkhachhang:
            if idx['tenkhachhang']==tenkhachhang:
                print('tong so tien can thanh cua '+str(tenkhachhang)+'la: '+str(idx['tongtien']))
    elif chon==5:
        tensp=input('nhap ten san pham can tinh SL ')
        print('san pham '+tensp+' ban duoc: '+str(TimSoLuongSanPham(listkhachhang,tensp)))
    elif chon==6:
        for idx in listkhachhang:
            InHoaDon(idx)
    elif chon==7: break


