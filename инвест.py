x = int(input('Денег у Майкла:'))
y = int(input("Денег у Ивана:"))
z = int(input('Нужно денег для стартапа:'))
w = x + y
if (x >= z) and (y >= z):
    print('2')
elif (x >= z) and (y < z):
    print('Майкл')
elif (y >= z) and (x < z):
    print('Иван')
elif w >= z:
    print('1') 
else:
    print('0')