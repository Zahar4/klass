a = int(input())
v = 0 
if a > 1: 
    far i in range(1,a+1):
        if a%i==0:
            v+=1 
if v ==2:
    print(f" {a} prest")
else:
    print(f" {a} neprest")