#Write a program that returns numbers that are divisible by 7 and not a multiple of 5 between 1500 and 4700
l=[]
for i in range(1500, 4701):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))




#Write a program that calculates the factorial of a given number(you can use recursive functions)
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))




#Write a program that takes a phrase and returns the phrase with capital letters
phrase=input("saisir la phrase")
print(phrase.upper())




#for a given list of integers, write a program that returns a list without numbers reapeating
liste=[1,5,3,4,8,6,5,4,1,3]
lis=[]
for i in liste:
    if i not in lis:
        lis.append(i)
print(lis)