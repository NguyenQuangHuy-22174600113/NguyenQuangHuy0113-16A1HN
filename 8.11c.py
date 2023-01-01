import math
from re import X
n=int(input('Nhap gia tri n= '))
x=float(input('Nhap gia tri cua x = '))
so_hang_1=math.pow((x*x+x+1),n)
so_hang_2=math.pow((x*x-x+1),n)
A=float(so_hang_1+so_hang_2)
print('Gia tri của bieu thuc =%f'%A)