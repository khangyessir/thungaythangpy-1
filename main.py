thu_dict = {
    1: 'thu2',
    2: 'thu3',
    3: 'thu4',
    4: 'thu5',
    5: 'thu6',
    6: 'thu7',
    0: 'Chu nhat'
}
while True:
  ngay = int(input('Nhap ngay: '))
  while 0 > int(ngay) > 31:
      print('vui long nhap lai!')
      ngay = int(input('Nhap ngay: '))
  thang = int(input('Nhap thang: '))
  while 0 > thang > 12:
      print('vui long nhap lai!')
      thang = int(input('Nhap thang: '))
  while ngay == 31:
      if thang in [2, 4, 6, 9, 11]:
          print('vui long nhap lai!')
          thang = int(input('Nhap thang: '))
  while ngay == 30:
      if thang in [1, 2, 3, 5, 7, 8, 10, 12]:
          print('vui long nhap lai!')
          thang = int(input('Nhap thang: '))
  nam = int(input('Nhap nam: '))
  thu = (ngay + (nam - 1) * (366 if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0) else 365)) % 7 +3
  thu = thu_dict.get(thu, 'Invalid day')
  print('Thu: ', thu)

