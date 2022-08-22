### Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


num = float(input('Input your number: '))

def SumDigits(n):
    n = str(n)
    sum=0
    for i in n:
        if i!='0' and i!='.':
            sum += int(i)
    return sum
    


print(SumDigits(num))



### Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = int(input('Input your number: '))

# def Numbers(n):
#     nums = list(range(1,n+1))
#     sum =1
#     for i,j in enumerate(nums):
#         if i==0: nums[i] = j
#         else: 
#             sum = sum * j
#             nums[i] = sum
#     return nums
        

# print (Numbers(num))