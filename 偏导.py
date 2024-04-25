from sympy import *

x,y,z,k1,k2=symbols('x,y,z,k1,k2')
x1,x2,k = symbols('x1,x2,k')
f=x*y*z
g1=x+y-1
g2=x-y+z**2-1
#构造拉格朗日等式
L=f+k1*g1+k2*g2
print("L="+str(L))
dx=diff(L,x)
dy=diff(L,y)
dz=diff(L,z)
dk1=diff(L,k1)
dk2=diff(L,k2)
print("dx="+str(dx))
print("dy="+str(dy))
print("dz="+str(dz))
print("dk1="+str(dk1))
print("dk2="+str(dk2))
m=solve([dx,dy,dz,dk1,dk2],[x,y,z,k1,k2])
print(m)
min=10e9
max=-10e9
for index in m:
    x,y,z=index[0],index[1],index[2]
    print(x,y,z)
    f=x*y*z
    print("f=",f)
    print("f=",float(f))
#
# f = 60-10*x1-4*x2+(x1)**2+(x2)**2-x1*x2
# g = x1+x2-8
# #构造拉格朗日等式
# L=f-k*g
# #求导，构造KKT条件
# dx1 = diff(L, x1)   # 对x1求偏导
# print("dx1=",dx1)
# dx2 = diff(L,x2)   #对x2求偏导
# print("dx2=",dx2)
# dk = diff(L,k)   #对k求偏导
# print("dk=",dk)
# dx1= -k + 2*x1 - x2 - 10
# dx2= -k - x1 + 2*x2 - 4
# dk= -x1 - x2 + 8
# #求出个变量解
# m= solve([dx1,dx2,dk],[x1,x2,k])
# print(m)
# {x1: 5, x2: 3, k: -3}
# #给变量重新赋值
# x1=m[x1]
# x2=m[x2]
# k=m[k]
# #计算方程的值
# f = 60-10*x1-4*x2+(x1)**2+(x2)**2-x1*x2
# print("方程的极小值为：",f)
