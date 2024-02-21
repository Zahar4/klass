#1
a = 0
b = 1 

n = int(input()) - 2
print(a)
print(b)
while n > 0:
    n-=1 
    b = a+b 
    a = b-a
    print(b)

#1 
print ("Введите чётные числа от 0 до 20")
for i in range( 0 , 21 , 2)
      print (i)
print ("Каждое третье число от -1 до -21:")
i = -1
while i >= -21:
    print(i)
    i -= 3
