from random import random
N=999999999
n=0
for i in range(N):
    x=random()
    y=random()
    r=x**2+y**2
    if r<=1.0:
        n=n+1
pi=4*(n/N)
print(f'经过{N}轮扔豆子,圆周率pi为{round(pi,2)}')