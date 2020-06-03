"""

#Question 1
print ('\nQuestion 1')

import math
a = 5
b = 5.0
c = 5 > 1
d = '5'
e = 5 * 2
f = '5' * 2
g = '5' + '2'
h = 5 / 2
i = 5 // 2
j = [5, 2, 1]
k = 5 in [1, 4, 6]
l = math.pi

lst = (a,b,c,d,e,f,g,h,i,j,k,l)

for temp in lst:
    datatype = type(temp)
    print (datatype)

#Question 2
#a
print ('\nQuestion 2.a')

letters = "Supercalifragilisticexpialidocious"
print (len(letters))

#b
print ('\nQuestion 2.b')

if letters.find('ice') > 0:
    print ('\'ice\' IS in it!')
else:
    print ('\'ice\' is NOT in it!')
#c
print ('\nQuestion 2.c')

longest = max('Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus', 'Bababadalgharaghtakamminarronnkonn')
print (longest + ' is the longest word among the three.')

#d
print ('\nQuestion 2.d')
names = ('Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein')
first = min(names)
last = max(names)
print (first + ' comes first in dictionary.')
print (last + ' comes last in dictionary.')

#Question 3
#a
print ('\nQuestion 3.a')

def inside(x,y,x1,y1,x2,y2):
    if x>=x1 and x<=x2 and y>=y1 and y<=y2:
        print ('True)
    else:
        print ('Fale')

inside(1,1,0,0,2,3)

inside(-1,-1,0,0,2,3)
    
#b
print ('\nQuestion 3.b')

inside(1,1,0.3,0.5,1.1,0.7)

inside(1,1,0.5,0.2,1.1,2)


#Question 4
print ('\nQuestion 4')

def pig(pstr):
    pstr = pstr.lower()
    if pstr[0] in ['a','e','i','o','u']:
        print (pstr+'way')
    else:
        print (pstr[1:]+pstr[0]+'ay')

pstr = input('Please input any word, we can turn it into pig-Latin\n')
pig(pstr)

#Question 5
print ('\nQuestion 5')

def bldcount(filestr):
    a = b = ab = o = oo =0
    allInfo = open(filestr)
    line = allInfo.readline()
    line = line.split(' ') # very very important!!!!!!!!!
    for each in line:

        if each=='A':
            a+=1
        if each=='B':
            b+=1
        if each=='AB':
            ab+=1
        if each=='O':
            o+=1
        if each =='OO':
            oo+=1   
            
    print ('There are ' + str(a) +  ' patients of blood type A.')
    print ('There are ' + str(b) + ' patients of blood type B.')
    print ('There are ' + str(ab) + ' patients of blood type AB.')
    print ('There are ' + str(o) + ' patients of blood type O.')
    print ('There are ' + str(oo) + ' patients of blood type OO.')
        
filestr = bldcount('bloodtype.txt')


#Question 6
print ('\nQuestion 6')

def curConv(curStr,amount):
    convAmount=0
    allInfo = open("currencies.txt")
    for each in allInfo:
        each = each.split('\t') # very important!!!!!!!!!
        if curStr==each[0]:
            convAmount=float(each[1])*float(amount)
            convAmount="{:.4f}".format(convAmount) # print("%.2f" % a)  print("{:.2f}".format(a))
            print("You have " + convAmount + " US dollars." )
            
curType = input('Please input the  currency\n').upper()
curAmount = input('Please input the amount\n')
curConv(curType,curAmount)

#Question 7
print ('\nQuestion 7')

print("adding 6 +  'a'          SyntaxError: invalid syntax\n")

print("lst = [1,2,3,4,5,6,7,8,9,10]")
print("lst[11]                  IndexError: list index out of range\n")

print("import math")
print("math.sqrt(-1.0)          ValueError: math domain error\n")

print("print(x)                 NameError: name 'x' is not defined\n")

print("open('currenciez.txt')   FileNotFoundError: [Errno 2] No such file or directory: 'currenciez.txt'")


#Question 8
print ('\nQuestion 8')

def frequencies(inputletters):
    #a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0
    #letterlist = 'abcdefghijklmnopqrstuvwxyz'
    #letterCount = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
    letterlist = 'abcdefghijklmnopqrstuvwxyz'
    letterCount = [0]*26
    for each in inputletters:
        index = letterlist.find(each)
        if each==letterlist[index]: 
            letterCount[index]+=1 
        
    print(letterCount)
    
inputletters = input('Please type in any word: ')
frequencies (inputletters)

"""

#Question 9
print ('\nQuestion 9')

def sieve(num): 
    num = int(num)
    L=list(range(2,num+1))
    primeL=[]
    for each in range(num-1):
        primeL.append(L[0])
        L.remove(L[0])
        
        
        print(L)
        
        
    print(primeL)
        #L.remove(each*int(num/each))
        
        
num =input("Enter a number: ")
sieve(num)


"""
# prime numbers are greater than 1
if num > 1:
   # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
        break
    else:
            print(num,"is a prime number")
       # if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")



#Question 10
print ('\nQuestion 10')

import math
def triangleArea(a,b,c):
    a=int(a)
    b=int(b) 
    c=int(c)
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print (area)
    

a = input('Please type in the first side: ')
b = input('Please type in the second side: ')
c = input('Please type in the third side: ')

triangleArea(a,b,c)

"""

        for multi in L:
            #if (each+1)*(multi+1)<=num:
            L.remove((each+1)*(multi+1))
            break