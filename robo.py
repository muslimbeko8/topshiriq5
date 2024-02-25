# ls = input().split()
# num1, num2 = 0, 0
# a,b = 0, 0
# m = 0
# for i in range(len(ls)):
#     num1, num2 = map(int, ls[i].split(":"))
#     a += num1
#     b += num2
#     if num1 > num2:
#         m += 3
#     elif num2 == num1:
#         m += 1
# print(f"{m} scores {a}-{b}")



# a = input()
# ls = "Nothing"
# while a != '':
#    t = "Like" if a[0] ==  "L" else "dislike"
#    a = a[len(t):]
#     ls =  "Nothing" if ls == t else t 
# print(ls)


# sez = "0123456789"
# s = input()
# n = 5
# b = ""
# for i in range(len(s)):
#     k = sez.index(s[i])
#     b += sez[(k + n)]
# print(b)



# for i in range(int(input())):
#     print(bin(int(input()))[2:].count('1'))

# n = input()
# print(len(n))
# for i in range(len(n)):
#     print(bin(ord(n[i]))[2:])

# ls = list(map(int,input().split()))
# print(list(filter(lambda i :i % 2 == 0, ls)))




#         m += 3
#     elif num2 == num1:
#         m += 1
# print(f"{m} scores {a}-{b}")  



# a = input()
# ls = "Nothing"
# while a != '':
#    t = "Like" if a[0] ==  "L" else "dislike"
#    a = a[len(t):]
#     ls =  "Nothing" if ls == t else t 
# print(ls)



# sez = "0123456789"
# s = input()
# n = 5
# b = ""
# for i in range(len(s)):
#     k = sez.index(s[i])
#     b += sez[(k + n)]
# print(b)



# for i in range(int(input())):
#     print(bin(int(input()))[2:].count('1'))

# n = input()
# print(len(n))
# for i in range(len(n)):
#     print(bin(ord(n[i]))[2:])

# ls = list(map(int,input().split()))
# print(list(filter(lambda i :i % 2 == 0, ls)))








# ls = [34,345,463,7546,7467,5,34,35,341,1,2,4,5,78,5,56,3464]
# for i in range(len(ls)):
#     for j in range(len(ls)):
#         if ls[i] < ls[j]:
#             t = ls[i]
#             ls[i] = ls[j]
#             ls[j] = t
# print(ls)

# def sortla(ls:list, i:int):
#     if ls == []: 
#         return []
#     else:
#         pass




# ls = list(map(int,input().split()))
# for i in range(len(ls)):
#     for j in range(i+1,len(ls)):
#         if len(str(ls[i])) > len(str(ls[j])):
#             t = ls[i]
#             ls[i] = ls[j]
#             ls[j] = t

# print(ls)




# x1, v1, x2, v2 = map(int, input().split())

# if v1 > v2:
#   if (x2 - x1) % (v1 - v2) == 0:
#     print('YES')
#     exit()
# print('NO')

#! ord,  ASCII harflarni ornini olib beradi
#! chr   ornidagi harflarni olib beradi
#! print(ord("1"))
#! print(chr(97))
# from math import factorial
# d ='0123456789'
# p = input()[5:]
# c = 0
# for i in d:
#     if i in p:
#         c += 1
# print((factorial(7) // factorial(7-c)) * (c-1) // c)
# qu, qa, qo = 'quduq', 'qaychi', "qog'oz"

# a, v, g = input(), input(), input()

# if a == qu:
#     if v == qa and g == qa:
#         print('Ali')
#         exit()
# if a == qa:
#     if v == qo and g == qo:
#         print('Ali')
#         exit()
# if a == qo:
#     if v == qu and g == qu:
#         print('Ali')
#         exit()   
# if v == qu:
#     if a == qa and g == qa:
#         print('Vali')
#         exit()
# if v == qa:
#     if a == qo and g == qo:
#         print('Vali')
#         exit()
# if v == qo:
#     if a == qu and g == qu:
#         print('Vali')
#         exit() 
# if g == qu:
#     if a == qa and v == qa:
#         print("G'ani")
#         exit()
# if g == qa:
#     if a == qo and v == qo:
#         print("G'ani")
#         exit()
# if g == qo:
#     if a == qu and v == qu:
#         print("G'ani")
#         exit() 

# print('?')


# rus = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
# uzb = "qwertyuiop[]asdfghjkl;'zxcvbnm,.QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,."
# st = input()
# for i in st:
#     print(uzb[rus.index(i)], end='')


# n = int(input())
# lst = list(map(int,input().split()))

# n = input()
# print(n*4)



# import os
#!_______________________________________________________________NIMA___________________________________________________________________
# ls = []
# while 1 > 0:
#     b = int(input("yozish 1\no'chirish 2\nchiqish 0\nSon kiriting: "))
#     if b == 0:
#             os.system("cls")
#             exit()
#     elif b == 1:
#         n = int(input("boshiga 1\noxiriga 2\nindexga 3\nKiriting: "))
#         if n == 1:
#             q = int(input("nechta malumot qoshmmoqchisiz: "))
#             print("nima qo'shmoqchisiz: ")
#             for i in range(q):
#                 ls.insert(0, input())
#         elif n == 2:
#             q = int(input("oxiriga nechta malumot qoshmmoqchisiz: "))
#             print("nima qo'shmoqchisiz: ")
#             for i in range(q):
#                 ls.append(input())
#         elif n == 3:
#             z = int(input("Nechanchi indexga qoshmoqchsiz: "))
#             print(z, " - indexga nima qoshmoqchisiz", ls.insert(z,input("kiriting: ")))
#         print("LIST:  ", ls)
#         print("\n\n\n")
#     elif b == 2:
#         if ls == []:
#             print("list bosh ochirgani hech narsa yoq")
#             continue
#         m = int(input("listni oxiridan o'chirish 1\nlistni indexdan o'chirish 2\nlistni qiymatni o'chirish 3\nlistni to'zalab beradi 4\nSon kiriting: "))
#         if m == 1:
#             ls.pop()
#         elif m == 2:
#             g = int(input("nechanchi indexni ochirmoqchisiz: "))
#             ls.pop(g)
#         elif m == 3:
#             print(ls)
#             r = input("nimani ochirmoqchisiz: ")
#             ls.remove(r)
#         elif m == 4:
#             ls.clear()
#         print("LIST:  ",ls)
#         print("\n")
#!____________________________________________________________________________________________________________________________________________





# ls = {"1":"24", "2":"135", "3":"26", "4":"157",  "5":'2468', "6":"359", "7":"48", "8":"5790", "9":"68", "0":"8"}
# n = input()
# for i in range(len(n)-1):
#     b = ls.get(n[i])
#     if not n[i+1] in b:
#         print("NO")
#         exit()
# print("YES")




# n = int(input())
# if n % 400 == 0 or n % 4 == 0  and n % 100 != 0:
#     print("12/09/{:04d}".format(n))
# else:
#     print("13/09/{:04d}".format(n))





