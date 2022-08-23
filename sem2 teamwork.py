### Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''
X=1
Y=1
Z=1
def Predicat(x,y,z):
    if not (x or y or z) ==  (-x and not y and not z):
        return True
    else: False

print(Predicat(X,Y,Z))
'''
### Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
'''
def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                    print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB)), '.2f'}")
'''




### 1 программист, 2 программиста, 5 программистов
'''
num = int(input('How many people?: '))

def Developers(n):
        
    # 1,21,31,91,101,121,201,221
    if (n==1) or (n>20 and n%10==1) or (n>99 and n%100==1):
        print(str(n) + " программист")

    # 2,3,4,22,23.24
    elif (2<=n<=4) or (n>20 and 2<=n%10<=4) or (n>99 and 2<=n%100<=4):
        print(str(n) + " программиста")
    # 0,5,6,7,8,9,10,11,25,100,105...
    else: print(str(n) + " программистов")


print(Developers(num))

'''


# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Для N = 5: 1, -3, 9, -27, 81

# n = int(input('Input your number: '))

# def Numbers(num):
#     for i in range(0,num):
#         b = (-3)**i
#         print (b, end=' ')

# Numbers(n)

'''
n = int(input('Input your number: '))

def Numbers(num):
    nums = list(range(1,num+1))
    b=1
    for i,j in enumerate(nums):
        if i==0: nums[i] = j
        else: 
            b = b*(-3)
            nums[i] = b
    return nums

print(Numbers(n))
'''

# Калькулятор


what = input('Введите операцию через пробел: ')
def Calculator(operation):

    s = what.split(' ')
    x1 = int(s[0])
    x2 = s[1]
    x3 = s[2]
    match x2:
        case '+': return x1+x3
        case '-': return x1-x3
        case '*': return x1*x3
        case '/': return x1/x3
        

print(Calculator(what))