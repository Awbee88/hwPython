### Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# num = int(input('Input number if week day: '))

# def Week(day):
#     if 1<=day<6: print('No')
#     elif 5<day<8: print('Yes')
#     else: print('Incorrect')

# Week(num)



# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x_point = int(input('Input x: '))
y_point = int(input('Input y: '))

def Coordinate(x,y):
    if x==0 or y==0: print('Error!')
    elif x>0 and y>0: print('1')
    elif x>0 and y<0: print('4')
    elif x<0 and y>0: print('2')
    elif x<0 and y<0: print('3')

Coordinate(x_point,y_point)
