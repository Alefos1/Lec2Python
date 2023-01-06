# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

# n = int(input("Введите число:"))
# def  A(num):
#    tot = 0
#    while(num > 0):
#        dig = num % 10
#        tot = tot + dig
#        num = num//10
#    return tot
# print(A(n))

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

# N = int(input('Введите число '))

# f = 1
# for i in range(N):
#    i = i + 1
#    f = i * f
    
# print(f, end = " ")

# Задайте список из n чисел 
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите число: ')) 

# def sequence(n):

#    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))

# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

# import random
# list = [0,1,2,3,4,5,6,7,8,9]
# print ("Начальный список: " + str(list))
# for i in range(len(list)-1, 0, -1):
#    j = random.randint(0, i + 1) 
#    list[i], list[j] = list[j], list[i] 
# print ("Перемешанный список: " +  str(list))