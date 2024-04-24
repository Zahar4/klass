n = int(input('товар'))
z = int(input('стоимость'))
s = int(input('кошелёк'))
k = int(input('количество'))
f = n*z#стоимость всего товара
c = s*k#денег у покупателей
while c>z:
    if s-z ==0:
        