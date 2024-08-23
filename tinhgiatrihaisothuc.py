# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:54:36 2024

@author: TranDuongBaoTran 
"""
import math

a=float(input("Nhập a: " ))
b=float(input("Nhập b: "))
gt1=math.sqrt(a)-math.sqrt(b)
gt2=a**(1/4)-b**(1/4)
gt3=math.sqrt(a)+(a*b)**(1/4)
gt4=a**(1/4)+b**(1/4)

ketqua=(gt1/gt2)-(gt3/gt4)
print("Kết quả của biểu thức là: ",ketqua)

