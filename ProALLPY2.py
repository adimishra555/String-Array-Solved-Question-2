# s='hello wolrd'
# lenght=0
# for i in s:
#     lenght+=1
# print(f'the length of the {s} is {lenght}')



# s="hello world"
# res=""
# for i in s:
#     res=i+res
# print(res)

# s='hello world'
# u='word'
# r=''
# for i in s.split():
#     if i=="world":
#         r+=u+' '
#     else:
#         r=i+" "
        
# print(r)


# s='hello world'
# l=[]
# st=''
# for i in s:
#     l+=[i]
# print(l)


# s = 'hello welcome to python'
# print(','.join(s.split()))
# for i in s.split():
#     print(i,end=' , ')



# s='hello world'
# print(s[::2])


# s='hello python'
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)



# def swap(s):
#     str=''
#     for i in s:
#         if 'a'<=i<='z' and i!=" ":
#             str+=chr(ord(i)-32)
#         else:
#             str+=chr(ord(i)+32)
#     return str
# var=swap("Hello World")
# print(var.split('@'))

# s=['hELLO', 'wORLD']
# print(' '.join(s))
# print(str(s))



# l1 = [1,3,5,7]
# l2 = [2,4,6,8]
# l3 = [3,6,9,12]
# l4 = []

# for i in zip(l1,l2,l3):
#     l4.append(i)
# print(l4)

# print(sum([l1,l2,l3],[]))

# s = 'malayalam'
# if s==s[::-1]:
#     print('it is palindrome ')
# else:
#     print('it is not palindrome')


# s = 'hello world'
# ch='w'
# for i,j in enumerate(s):
#     if j==ch:
#         print(f'the char is present in the index {i}')
# print()
        
        
        
# sentence = 'hello world welcome to python programming hi there'
# d={}
# for i in sentence.split():
#     if i[0] in d:
#         d[i[0]]+=[i]
#     else:
#         d[i[0]]=[i]
# print(d)



# sentence = 'hello world welcome to python programming hi there'
# from collections import defaultdict
# res=defaultdict(str)

# for i in sentence.split():
#     res[i[0]]+=i+" "
# print(res)
    
    
    
# s = 'hellohai'
# for i in s:
#     if s.count(i)>1:
#         print(s.replace(i,'-'))
# print(s)
        
        
        
# def outer(func):
#     def inner(*a,**b):
    
#         # res=func(*a,**b)
#         # return abs(res)
#         return abs(func(*a,**b))
#     return inner

# @outer

# def sub(a,b):
#     return a-b
# print(sub(10,30))



# l = [34, 'hello', 'apple', 56.7, 4546, 67.8,
# 'google', 45]

# def res(lst):
#     res=[]
#     for i in lst:
#         if isinstance(i,str):
#             res.append(i)
#         elif isinstance(i,int):
#             res+=[int(str(i)[::-1])]
#         elif isinstance(i,float):
#             res+=[float(str(i)[::-1])]
#     return res
# print(res(l))



# class simple:
#     def __init__(self,a,b):
#         self.a=a            
#         self.b=b
    
#     def add(self,dx,dy):
#         return self.a+dx,self.b+dy

#     def sub(self,dx,dy):
#         return self.a-dx, self.b-dy
# s=simple(5,6)
# print(s.add(10,20))
# print(s.sub(20,30))



# class Custom:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
    
#     def __getitem__(self,key):
#         return self.__dict__[key]

# c=Custom("jaya",21)
# print(c['name'])
# print(c.name)


# s = 'Hi How are you'
# res=''
# for i in s:
    # res=i+res
# print(res)


# for i in s.split():
#     res=i[::-1]+' ' +res
# print(res)


# l = [1,3,5,7,2,4,6,7,3,1]
# dupl=[]
# ndupl=[]
# for i in l:
#     if i not in ndupl:
#         ndupl.append(i)
#     else:
#         dupl.append(i)
# print(dupl)
# print(ndupl)
    
    
    
# s = 'Life is full of surprises and miracles'
# lword=''
# for i in s.split():
#     if len(lword)<len(i):
#         lword=i
# print(lword)


# d = {'a': 'apple', 'one': 1, 'b': 'ball', 'three': 3,'four':4, 'n': 45.7}
# d1={}
# for i,j in d.items():
#     if isinstance(j,str):
#         d1[i]=j[::-1]
#     else:
#         d1[i]=j
# print(d1)


# a = ['hello', 'hai', 'world']
# b = ['hello', 'hai', 'world', 'python']

# for i in b:
#     if i not in a:
#         print(i,end=' ')


# def rev(*args):
#     for i in  args:
#         if isinstance(i, (str,list,tuple)):
#             return i[::-1]
#         return args
# print(rev("hellow java"))


# def fun(string,i):
#     if i==0:
#         print(string[1::2])
#     else:
#         print(string[0::2])
# fun('TRACXN',0)
# fun('TRACXN',1)



# s = 'Sony12India567pvt21ltd'
# sum=0
# for i in s:
    # if i.isdigit():
        # sum+=int(i)
# print(sum)

# from re import findall
# var=findall('[0-9]+',s)
# print(var)
# sum=0
# for i in var:
#     sum+=int(i)
# print(sum)


# l = ['hello', '123', 'hai', 'python', '345']
# d=[]
# for i in l:
#     if i.isdigit():
#         d.append(i)
# d.append(int(i))
# print(d)


s = 'hiihellowordhellowar'
# res={}
# for i in s:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1
# print(res)
        
        
        
# from collections import defaultdict
# d=defaultdict(int)

# for i in s:
#     d[i]+=1
# print(d)
    
    
# l = [1,3,5,7]
# var= lambda i:i**2
# print(list(map(var,l)))



# names = ['apple', 'google', 'yahoo', 'gmail','flipkart', 'amazon']
# l=[]
# for i in names:
#     if len(i)%2==0:
#         l.append(i)
# print(l)



# names = ['apple', 'google', 'yahoo', 'gmail','flipkart', 'amazon']
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=len(i)
# print(d)


# d = {}
# for name in names:
#     if len(name) % 2 == 0:
#         d[name] = len(name)
# print(d)


# l = [[1,2,3], [4,5,6], [7,8,9]]
# print([sum(i) for i in l])
# print(sum([sum(i) for i in l]))


# d = {'a': 100, 'b':{'m':'man', 'n':'nose', 'o':'ox'}}

# def replace(dict_,old,new):
#     for i,j in dict_.items():
#         if isinstance(j, dict):
#             for k,l in j.items():
#                 if l==old:
#                     j[k]=new
#     return dict_
# print(replace(d,'nose','net'))
    
    
# names = ['listen', 'hello', 'eat', 'desserts',
# 'silent', 'peek', 'ate',
# 'keep', 'tea', 'stressed']

# d={}
# for i in names:
#     var=''.join(sorted(i))
#     if var not in d:
#         d[var]=[i]
#     else:
#         d[var]+=[i]
# print(d)


# s = 'This is a programming language and programming is fun'
# s1=''
# for i in s.split():
#     if len(s1)<len(i) and s.count(i)==1:
#         s1=i
# print(s1)
        
        
# s = 'hiihellowordhellowar'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# s = 'helloworld'
# d={}
# for i in s:
#     if s.count(i)>1:
#         d[i]=s.count(i)
# print(d)


# names = ['apple', 'google', 'yahoo', 'gmail',
# 'flipkart', 'amazon']
# l=[]
# for i in names:
#     if len(i)%2==0:
#         l.append(i)
# print(l)

# names = ['apple', 'google', 'yahoo', 'gmail',
# 'flipkart', 'amazon']
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=len(i)
# print(d)


# s = ['hello', 'hai', 'python']
# l=[]
# for i in s:
#     l=[i]+l
# print(l)

# names = ['listen', 'hello', 'eat', 'desserts',
# 'silent', 'peek', 'ate',
# 'keep', 'tea', 'stressed']
# d={}
# for i in names:
#     nme=''.join(sorted(i))
#     if nme not in d:
#         d[nme]=i
#     else:
#         d[nme]+=i
# print(d)


# names = ['apple', 'google', 'gmail', 'apple',
# 'yahoo', 'google']
# d=[]
# for i in names:
#     if names.count(i)>1:
#         if i not in d:
#             d.append(i)
# print(d)


# names = ['apple', 'google', 'gmail', 'apple',
# 'yahoo', 'google']
# print({i:names.count(i) for i in names})


# n=int(input('Enter the number:'))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('it is prime number')
# else:
#     print('it is not prime number')


# numbers = [10,30, 50, 40, 60, 20]
# n=0
# for i in numbers:
#     if i>n:
#         n=i
# print(n)


# def last(n):
#     # var=str(n)
#     var=n%10
#     # return int(var[-1])
#     return var
# print(last(1234))


# def tail(args,n):
    # return list(args[-n:])
# print(tail('hellow world',2))


# def isperfactsqure(num):
#     res=num//2
#     for i in range(res):
#         if i*i==num:
#             return True,f' {num} it is perfact squre'
#     return False ,f'{num} it is not perfact squre'

# print(isperfactsqure(11))
# print(isperfactsqure(169))


# n=int(input('Enter the number:'))
# res=0
# for i in range(1,n):
#     if n%i==0:
#         res+=1
# if (n==res):
#     print('it is perfact number')
# else:
#     print('it is not perfact number')


# l = ['apple', 123,45.6, 'google', [1,2,3], '4+6',
# 3+3j]
# d=[]
# for i in l:
#     if isinstance(i,(int,float,complex)):
#         d.append(i)

# print(d)


# all_products = ['iphone', 'mac', 'gmail', 'googlemaps', 'iwatch', 'windows',
#  'ios','google drive', 'one drive']
# from collections import defaultdict
# apple_product=[]
# google_product=[]
# window_product=[]

# d=defaultdict(list)

# for i in all_products:
#     if i in apple_product:
#         d['apple_product']+=[i]
#     elif i in google_product:
#         d['google_product']+=[i]
#     elif i in window_product:
#         d['window_product']+=[i]
# print(d)
        
        
# names = ['apple', 'google', 'yahoo', 'gamil',
# 'facebook', 'flipkart', 'amazon']

# def rotate(l,n):
#     return l[n:]+l[:n]
# print(rotate(names,-3))


# s = 'hai hello how are you'
# rs=''
# for i in s:
#     if s.count(i)==1:
#         rs+=i
# print(rs)





# l = [1,2,3,4,5,6,7,8,9]
# res=[]
# for i,j in enumerate(l):
#     if i%2==0:
#         res.append(j)
#     else:
#         res.append(j)
#         print(res)
#         res=[]
# print(res)


# s = 'hi there how are you'
# res=[]
# for i in s:
#     if i not in res:
#         res.append(i)
#     else:
#         print(i)
#         break
# print(res)
    
    
# n=int(input('Enter the number:'))
# t=n
# d=0
# while n>0:
#     a=n%10
#     d=d+a*a*a
#     n=n//10
# if (t==d):
#     print('it is armstrong number')
# else:
#     print('it is not armsstrong number')












# rs=[]
# for i in s:
#     if i not in rs:
#         rs.append(i)
#     else:
#         print(i)
#         break
# print(rs)
    
    
# items = ['lotus-flower', 'lilly-flower', 'catanimal', 'dog-animal',
# 'sunflower-flower']

# d={}
# for i in items:
#     var=i.split('-')
#     if var[-1] not in d:
#         d[var[-1]]=[var[0]]
#     else:
#         d[var[-1]]+=[var[0]]
# print(d)


# files = ['apple.txt', 'yahoo.pdf', 'google.pdf',
# 'gmail.txt', 'amazon.pdf',
# 'flipkart.txt']
# d={}
# for i in files:
#     var=i.split('.')
#     if var[-1] not in d:
#         d[var[-1]]=[var[0]]
#     else:
#         d[var[-1]]+=[var[0]]
# print(d)


# s = 'ghello12world34welcome! 123'
# res=''
# for i in s:
#     if i.isdigit()!=True:
#         res+=i
# print(res)


# sentence = 'Hi there! how are you:) How are you doing toady!'
# from re import findall
# var=findall('[a-zA-Z0-9]+',sentence)
# print(len(var))
        
        
# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_even={}
# for i in numbers:
#     if i%2==0:
#         if 'even' not in odd_even:
#             odd_even['even']=[i]
#         else:
#             odd_even['even']+=[i]
#     else:
#         if 'odd' not in odd_even:
#             odd_even['odd']=[i]
#         else:
#             odd_even['odd']+=[i]
# print(odd_even)
        
        
# s = 'hello world hi apple you yahoo to you'.split()
# max_word=[]
# for i in s:
#     if len(i)>len(max_word) :
#         max_word=i


# print(max_word)


# s = '0-0,4-8,20-20,43-45'.split(',')
# res=[]
# for i in s:
#     var=i.split('-')
#     for j in range(int(var[0]),int(var[1])+1):
#         res.append(j)
# print(res)


# total_length = ([1, 2, 3], (4,5), ['apple', 'google',
# 'yahoo', 'gmail'],
# (1,2,3), {'a':1, 'b': 2})

# def total_sum(*args):
#     sum=0
#     for i in args:
#         for j in i:
#             sum+=len(j)
#     return sum
# print(total_sum(
#     ([1, 2, 3], (4,5), ['apple', 'google',
# 'yahoo', 'gmail'],
# (1,2,3), {'a':1, 'b': 2})
# ))



# names = ['apple', 'google', 'yahoo', 'apple',
# 'yahoo', 'google', 'gmail',
# 'apple', 'gmail', 'yahoo']

# d={}
# for i,j in enumerate(names):
#     if j not in d:
#         d[j]=[i]
#     else:
#         d[j]+=[i]
# print(d)
          
          
# s = 'hello 123 world 567 wlcome to 9724 python'
# sum_even=0
# for i in s:
#     if i.isdigit() and int(i)%2==0:
#         sum_even+=int(i)
# print(sum_even)


# numbers = [1,2,3,0,4,3,2,4,2,2,0,4]
# s=sorted(numbers)
# max_=[i for i in s if i>= s[-1]]
# print(max_)


# s = 'hello world welcome to python'
# for i in s:
#     if i==' ':
#         res=s.replace(i,'\n')
# print(res)


# s = 'hello world welcome to python'
# from re import sub
# res=sub('[AEIOUaeiou]','*',s)
# print(res)


# num = ['1', '12', '13', '12345', '125', '905', '55',
# '5', '95655', '55555']
# from re import findall
# res=list(filter(lambda s:findall(r'.*5$',s),num))
# print(res)


# l=[]
# for i in num:
#     if i.endswith('5'):
#         l.append(int(i))
# print(l)



# names = ['apple', 'google', 'yahoo', 'apple',
# 'yahoo', 'google', 'gmail',
# 'apple', 'gmail', 'yahoo']
# d={}
# for i,j in enumerate(names):
#     if j not in d:
#         d[j]=[i]
#     else:
#         d[j]+=[i]
# print(d)


# word1 = 'hello 1 2 3 4 5'.split()
# word2 = 'world 5 6 7 8 9'.split()

# l=[]
# for i,j in zip(word1,word2):
#     if i.isdigit() and j.isdigit():
#         l.append(int(i)+int(j))
# print(l)


# numbers = ['857', '987', '8', '128', '88888', '547',
# '7674', '89', '589',
# '38888', '2889']
# from re import findall
# res=list(filter(lambda number:findall(r'^8.*',number),numbers))
# print(res)


# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
# print([str(i)+" : "+j for i in l1 for j in l2])


# a = "10.20.30.40"
# res = a.split(".")[::-1]
# print(".".join(res))


# a = [3, 5, -4, 8, 11, 1, -1, 6]
# for i in a:
#     for j in a:
#         if i-j==10 or i+j==10 and i!=j:
#             print(i,j)


# def prefix(func):
#     def inner(*a):
#         for i in a:
#             print(f'+91 {i}')
#         func(a)
#     return inner

# @prefix
# def phone(*num):
#     return num
# prefix(phone(91118722828,1827338,735364))


# def divexp(a,b):
#     assert a>0,'Error'
#     if b==0:
#         raise 'zerodevisionerror'
#     else:
#         c=a/b
#     return c
# a=eval(input('Enter a'))
# b=eval(input('Enter b'))
# print(divexp(10,20))


# items = ['$123.45', '$434.23', '$567.89']
# res=[]
# for i in items:
#     res.append(i.strip('$'))
# print(res)


# n=int(input('Enter the number:'))

# a=0
# b=1
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print('  ',c,end=' ')
    
    
    
# items = ['glory', 'glass', 'signt', 'tight']
# res=set(items[0])
# for i in items[1:]:
#     res=res.intersection(set(i))
#     print(res)
# for i in res:
#     print(i)
    
    
# def countNumbers(arr):
#     for i in range(len(arr)):
#         n, m = arr[i]
#         count = 0

#         for num in range(n, m + 1):
#             digits = set()
#             is_distinct = True

#             for digit in str(num):
#                 if digit in digits:
#                     is_distinct = False
#                     break
#                 else:
#                     digits.add(digit)

#             if is_distinct:
#                 count += 1

#         print(count)
# arr = [[1, 20], [9,19]]


# countNumbers(arr)


# def binary(n):
    # return '{0:b}'.format(int(n))
# print(binary(10))

# print(bin(10)[2:])

# arr = [4, 2, 7, 1, 9, 5]
# max_ele=0
# for i in arr:
#     if i>max_ele:
#         max_ele=i
# print(max_ele)



# arr=[1,2,4,7,7,5]
# sort=sorted(arr)
# print(sort[1],sort[-2])


# arr=[1,2,4,7,7,5]
# sort=sorted(arr)
# fhalf=sort[:len(sort)]
# lhalf=sort[len(sort):]
# print(fhalf,lhalf)
# print(lhalf,fhalf)


# arr=[1,2,4,7,7,5]
# mid=len(arr)//2
# fhalf=sorted(arr[:mid])
# lhalf=sorted(arr[mid:], reverse=False)
# print(fhalf+lhalf)
# print(lhalf+fhalf)


# def rotate(arr,n):
#     return arr[n:]+arr[:n]
# print(rotate([1,2,3,4,5,6],3))



# arr = [10, 89, 9, 56, 4, 80, 8]
# sum=0
# for i in arr:
#     sum=sum+i
# print(sum)
# print(sum/len(arr))

# arr=[2,4,1,3,5]
# arr.sort()
# n=len(arr)
# m=n//2
# if n%2==0:
#     print( (arr[m-1]+arr[m])/2)
# else:
#     print(arr[m])


# def findpair(pairs):
#     s=set()
#     for (i,j) in pairs:
#         s.add((i,j))
#         if (j,i) in s:
#             print((i,j))
# findpair( [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)])

#  ! Maximum Product Subarray in an Array

# arr = [1,2,3,4,5,0]
# def maxproduct(arr,n):
#     res=arr[0]
#     for i in range(n):
#         mul=arr[i]
#         for j in range(i+1,n):
#             res=max(res,mul)
#             mul*=arr[j]
#     return res

# n=len(arr)
# print('maximun subarray product is :',maxproduct(arr,n))


# ! Replace elements by its rank in the array
# l=[100, 2, 70, 12 , 90]
# k=sorted(l)
# for i in l:
#     p=k.index(i)
#     print(p+1,end=' ')


# nums = [4, -2, 0, 6, -4]
# ans=-1
# for i in range(1,len(nums)):
#     if sum(nums[:i])==sum(nums[i+1:]):
#         ans=i
#         break
# print('Equilibrium index of an array:')
# print(ans)
        
        
# arr=[6, 7, 9, 5, 3, 10]
# search=7
# for i,j in enumerate(arr):
#     if j==search:
#         print(i)
    
    
    
# arr1= [1,3,4,5,2]
# arr2= [2,4,3,1,7,5,15]
# ar1=set(arr1)
# ar2=set(arr2)
# if ar1.issubset(ar2):
#     print(True)
# else:
#     print(False)



# fact=1
# n=int(input('Enter the number:'))

# for i in range(1,n+1):
#     fact=fact*i
# print('factorial of',n,'is ',fact)


# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         n=n*fact(n-1)
#         return n

# n=int(input('Enter the number:'))
# print('factorial of',n, 'is',fact(n))



# count=0
# n=int(input('Enter the number'))

# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('it is prime number')
# else:
#     print('it is not prime number')



# a=0
# b=1
# n=int(input('Enter the number:'))

# for i in range(n):
#     c=a+b
#     a=b
#     b=c
# print(' ',c,end=' ')



# n=int(input('Enter the number:'))
# temp=n
# rev=0
# while (n>0):
#     d=n%10
#     rev=rev*10+d
#     n=n//10
    
# if (temp==rev):
#     print('the number is palindrome')
# else:
#     print('the number is not palindrome')


# def fact(n):
#     f=1
#     i=1
#     while i<=n:
#         f=f*i
#         i+=1
#     return f

# nline=int(input('Enter the number of lines:'))

# for x in range(nline):
#     for y in range(x+1):
#         print(fact(x)//(fact(y)*fact(x-y)),' ',end=' ')
#     print()


# year=int(input('Enter the year to be want to check:'))

# if (year%4==0 and year%100!=0 or year%400==0):
#     print('the year is a leap year')
# else:
#     print('the year is not a leap year')


# i=1
# sum=0
# n=int(input('Enter the number:'))

# while i<n:
#     if (n%i==0):
#         sum+=i
#     i+=1


# if sum==n:
#     print('it is perfact number')
# else:
#     print('it is not perfact number')


# n=int(input('Enter the nuber:'))
# temp=n
# r=0

# while n>0:
#     a=n%10
#     r=r+a*a*a
#     n=n//10
    
# if (r==temp):
#     print('it is armstrong number')
# else:
#     print('it is not armstrong number')


# count=0
# n=int(input('ENter the number:'))

# for i in range(1,n+1):
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         print(cn,end=' ')
    
    
    
# n=int(input('Enter the number of row for floyd triangle: '))
# a=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end=' ')
#         a+=1
#     print()


# n=int(input('Enter the number:'))
# sum=0
# while (n>0):
#     x=n%10
#     sum=sum+x
#     n=n//10
# print('sum of digits of the number is',sum)


# num=int(input('Enter the number:'))
# pow=int(input('Enter the power:'))
# sum=1
# i=1

# while i<=pow:
#     sum=sum*num
#     i+=1
# print(num,'to the power ',pow,'is:',sum)



# c=float(input('Enter the temp in Centigarde:'))
# f=(1.8*c)+32
# print('temperature in fahrenheit={0:.2f}'.format(f))
    
    
# f=float(input('Enter the temp in faahrenheit:'))
# c=(f-32)*5/9
# print('temperature in fahrenheit={0:.2f}'.format(c))


# a=int(input('Enter the number:'))
# b=int(input('Enter the escond number:'))
# if a>b:
#     min=a
# else:
#     min=b
# while (1):
#     if (min%a==0 and min%b==0):
#         print('LCM is:',min)
#         break
#     min=min+1


# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)

# a=int(input('Enter the number:'))
# b=int(input('ENter the second number:'))

# ans=gcd(a,b)
# print('GCD is:',ans)


# def gcd(a,b):
#     if (b==0):
#         return a
    
#     else:
#         return gcd(b,a%b)
# ans=gcd(10,30)
# print(ans)
    


# radius=int(input('Enter the radius of the circle:'))
# area=3.14*radius**2
# print('Area of circle:{0:.2f}'.format(area))


# ! Area of Equilateral Triangle
# import math
# side=int(input('Enter the length of side:'))
# area=(math.sqrt(3)*(side**2))/4
# print('Area of Equilateral triangle :{0:.2f}'.format(area))



# def insertion_sort(arr):
#     for i in range(len(arr)):
#         temp=arr[i]
#         pos=i

#         while pos>0 and arr[pos-1]>temp:
#             arr[pos]=arr[pos-1]
#             pos=pos-1
#             arr[pos]=temp
#     return arr

# num_arr=[74,11,7,14,35]
# print(insertion_sort(num_arr))


# def selection_sort(arr):
#     for i in range(len(arr)):
#         min=i
#         for j in range(i+1, len(arr)):
#             if arr[j]<arr[min]:
#                 min=j
#         arr[min],arr[i]=arr[i],arr[min]
#     return arr
# num_arr=[11,1,77,84,9]
# print(selection_sort(num_arr))


# s='abcdemghij123456778'
# d='abc'
# for i in s:
#     if d in s:
#         print(d,'is present in s')
    
#     print(d, 'is not present in s')

# ! Convert Binary to Decimal 


# def bin_to_decimal(binary):
#     decimal=0
#     power=len(binary)-1

#     for i in binary:
#         decimal+=int(i)*(2**power)
#         power-=1
        
#     return decimal
# print(bin_to_decimal('1101'))

# ! Convert binary to octal
# def binary_to_octal(binary):
#     while len(binary)%3!=0:
#         binary+='0'
    
#     octal=''
#     i=0
#     while i<len(binary):
#         group=binary[i:i+3]
#         decimal=int(group,2)

#         octal_digit=oct(decimal)[2:]
#         octal+=octal_digit
#         i+=3
#     return octal

# print(binary_to_octal('1101'))


# ! decimal to binary
# def decimal_to_binary(decimal):
#     binary=''
#     if decimal==0:
#         return '0'

#     while decimal >0:
#         binary=str(decimal%2)+binary
#         decimal //=2
#     return binary

# print(decimal_to_binary(15))

# ! convert number to word
# def number_to_word(number):
#     digit_word={
#         '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
#     }
#     num_str=str(number)
#     words=[digit_word[i] for i in num_str]
#     result=' '.join(words)
#     return result
# print(number_to_word(101213))


# str='Take u forward is Awesome'
# vowel=0
# space=0
# consonent=0
# for i in str:
#     if i in 'AEIOUaeiou':
#         vowel+=1
#     elif i in ' ':
#         space+=1
#     else:
#         consonent+=1

# print(vowel)
# print(space)
# print(consonent)
    
    
    
# str='a+((b-c)+d)'
# import re
# res=re.sub(r'[({})]','',str)
# print(res)


# str = 'takeuforward'
# count=0
# for i in str:
#     if str.count(i)>1:
#         count+=1
# print(count)


# from collections import defaultdict
# d=defaultdict(int)

# for i in str:
#     d[i]+=1
# print(d)
# var=dict(d)
# print(d.most_common())
# from collections import Counter
# print(var.most_common())


# str1 = 'abcdef'
# str2='cefz'

# str3=''
# for i in str1:
#     if i not in  str2:
#         str3+=i
# print(str3)



# ! Change every letter with next lexicographic alphabet 

# ? ==>1

# str = 'abcdxyz'
# def lexico(char):
#     if 'a'<=char<='z':
#         return chr((ord(char)-ord('a')+1)%26+ord('a'))
        
#     elif 'A' <=char<='Z':
#         return chr((ord(char)-ord('A')+1)%26+ord('A'))

#     else:
#         return char

# def transform_str(input_string):
#     transformed_str=''.join(lexico(i) for i in input_string)
#     return transformed_str

# transfored_str=transform_str(str)
# print('original string',str)
# print(transfored_str)


# ? ===>2
# s='Google Doc'.split()
# res=''
# for i in s:
#     if len(i)>len(res):
#         res=i
# print(res)


# string = 'zxcbg'

# def bubble_sort(str):
#     n=len(str)
#     str_list=list(str)

#     for i in range(n):
#         for j in range(0,n-i-1):
#             if str_list[j]>str_list[j+1]:
#                 str_list[j],str_list[j+1]=str_list[j+1],str_list[j]
#     sort_str=''.join(str_list)
#     return sort_str
# print(bubble_sort(string))



# string='abcdefghij google microsoft'.split()
# res=''

# for i in string:
#     if string.count(i)>1:
#         res+=i
# print(res)

# def hellow(java):
#     print("ram ram ji")

# hellow("jaya")

# s='Google Doc'.split()
# l_word=''
# for i in s:
#     if len(i)>len(l_word):
#         l_word=i
# print(l_word)


# def bubble(str):
#     n=len(str)
#     char=list(str)
#     for i in range(n-1):
#         for j in range(0,n-i-1):
#             if char[j]>char[j+1]:
#                 char[j], char[j+1] = char[j+1], char[j]
    
#     sort_str=''.join(char)
#     return sort_str

# print(bubble('zxcbg'))

#  ! Find word with highest number of repeated letters in string in python using list comprehension
# str='abcdefghij google microsoft'

# def max_count_word(str):
#     words=str.split()

#     def count_repeated_letter(word):
#         return sum(1 for i in word if word.count(i)>1)

#     max_count_word=max(words,key=count_repeated_letter,default='')
#     return max_count_word

# res=max_count_word(str)
# print(f'Word with highest number of repeated letter is : {res}')


# str = 'jayA'
# res=''
# for i in str:
#     if i in res:
#         res+=chr(ord(i)+32)
#     else:
#         res+=chr(ord(i)-32)
# print(res)



# def is_palin(num):
#     return str(num)==str(num)[::-1]

# def palindrome_range(start,end):
#     return [i for i in range(start,end+1) if is_palin(i)]
# res=palindrome_range(100,500)
# print('palindrome number in range of {start} & {end} is {res}')


# def is_palin(num):
#     return str(num)==str(num[::-1])

# print(list(i for i in range(100,200) if is_palin(i)))
    
    
    
# ! =====================================>>>
# import calendar
# year=int(input('Enterthe year:'))
# month=int(input('Enter the month:'))
# cal=calendar.month(year,month)

# print(cal)


# ax2+bx+c=0
# import math
# a=float(input('Enter the Coefficients of a:'))
# b=float(input('Enter the Coefficients of b:'))
# c=float(input('Enter the Coefficients of c:'))

# discriminant=b**2-4*a*c
# if discriminant>0:
#     root1=(-b+math.sqrt(discriminant))/(2*a)
#     root2=(-b-math.sqrt(discriminant))/(2*a)
#     print(f'Root 1: {root1}')
#     print(f'Root 2: {root2}')

# elif discriminant==0:
#     root=-b/(2 *a)
#     print(f'Root: {root}')

# else:
#     real_part=-b/(2 * a)
#     imag_part=math.sqrt(abs(discriminant))/(2*a)
#     print(f' Root 1: {real_part}+{imag_part}i')
#     print(f' Root 2: {real_part}+{imag_part}i')



# year=int(input('Entet the year:'))
# if (year%400==0 and year%100!=0 or year%400==0):
#     print('it is leap year')
# else:
#     print('it is not leap year')


# n=int(input('Enter the number:'))
# count=0
# for i in range(1,n+1):
#     if (n%i)==0:
#         count=count+1
# if count==2:
#     print('it is prime number')
# else:
#     print('it is not prime number')


# l=1
# u=20
# for num in range(l,u+1):
#     if num>1:
#         for i in  range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)



# num=int(input('Enter the number:'))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(f'the factorial of {num} is {fact}')



# for i in range(1,11,1):
#     for j in range(10,2,-1):
#         print(i*j, end=' ')
#     print()

# a=0
# b=1
# nterms=int(input('How many terms do you want to generate the fibonacci numbers:'))
# for i in range(1,nterms+1):
#     c=a+b
#     a=b
#     b=c
#     print(c)


# n=int(input('Enter the number:'))
# t=n
# r=0
# while t>0:
#     a=n%10
#     r=r+a*a*a
#     n=n//10
# if r==t:
#     print('it is armestrong number')
# else:
#     print('it is not armstrong number')


# limit=int(input('Enter the number:'))
# sum=0
# for i in range(1,limit+1):
#     sum+=i
# print(sum)


# a=int(input('Enter the 1st number:'))
# b=int(input('Enter the second number:'))

# if (a>b):
#     min=a
# else:
#     min=b
# while(True):
#     if (min%a==0 and min %b==0):
#         print('LCM is :',min)
#         break
#     min=min+1



# def gcd(a,b):
#     if (b==0):
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(5,15))



# n=int(input('Enter the decimal number:'))
# print(bin(n),'Binary format')
# print(oct(n),'Octal format')
# print(hex(n),'Hex format')


# char=eval(input('Enter the character:'))
# print('The ASCII value of ',char,'is',ord(char))

# def recu_fabo(n):
#     if n<=1:
#         return n
#     else:
#         return (recu_fabo(n-1)+recu_fabo(n-2))
# print(recu_fabo(10))


# def bodymassindex(height, weight):
#     return round((weight/height**2),2)

# h=float(input('Enter the height in meter:'))
# w=float(input('Enter the weight in kg:'))

# bmi=bodymassindex(h,w)
# print('Your BMI is :',bmi)

# if bmi<=18.5:
#     print('You are underweigth')
# elif 18.5<bmi<=24.9:
#     print('you are normal weight')
# elif 24.9<bmi<=29.5:
#     print('you are over weight')
# else:
#     print('You are obese')


# import math
# num=int(input('Enter the number:'))    
# if num<=0:
#     print('Pls enter the positive  number')
# else:
#     result=math.log(num)
#     print('Logrithm number is :',result)


# def cube_sum_of_natural_number(n):
#     if n<=0:
#         return 0
#     else:
#         return sum([i**3 for i in range(1,n+1)])
# print(cube_sum_of_natural_number(7))


# arr = [1,2,3]
# total=0
# for i in arr:
#     total+=i
# print(total)

# arr = [10, 20, 30, 99]
# slarg=arr[0]
# for i in arr:
#     if i>slarg:
#         slarg=i
# print(slarg)


# arr = [1, 2, 3, 4, 5]
# def rotate(arr,n):
#     return arr[-n:]+arr[:-n]
# print(rotate(arr,3))


# def split_add(arr,k):
#     if k<=0 or k>=len(arr):
#         return arr
#     fst_part=arr[:k]
#     second_part=arr[k:]
#     return second_part+fst_part
# arr=[1,2,3,4,5,6]
# k=3
# res=split_add(arr,k)
# print(res)


# def add(mat1,mat2):
#     if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
#         return 'Matrix will be same dimension only'
#     res=[]
#     for i in range(len(mat1)):
#         row=[]
#         for j in range(len(mat1[0])):
#             row.append(mat1[i][j]+mat2[i][j])
#         res.append(row)
#     return res

# mat1 = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# mat2 = [
#  [9, 8, 7],
#  [6, 5, 4],
#  [3, 2, 1]
# ]
# result=add(mat1,mat2)
# for row in result:
#     print(row)

# if isinstance(res_mat,str):
#     print(res_mat)
# else:
#     print('sum of matrix elements is:')
#     for row in res_mat:
#         print(row)



# def multiply(mat1,mat2):
#     row1=len(mat1)
#     col1=len(mat1[0])
#     row2=len(mat2)
#     col2=len(mat2[0])

#     res=[[0 for i in range(col2)] for i in range(row1)]

#     for i in range(row1):
#         for j in range(col2):
#             for k in range(col1):
#                 res[i][j]+=mat1[i][k]*mat2[k][j]

#     return res

# mat1 = [[1, 2, 3],
#  [4, 5, 6]]
# mat2 = [[7, 8],
#  [9, 10],
#  [11, 12]]

 
# result=multiply(mat1,mat2)
# print(result)

        
        
# def transport_matrix(mat):
#     row,col=len(mat),len(mat[0])
#     res=[[0 for i in range(row)] for i in  range(col)]

#     for i in range(row):
#         for j in range(col):
#             res[j][i]=mat[i][j]
#     return res

# mat = [
#  [1, 2, 3],
#  [4, 5, 6]
# ]

# result=transport_matrix(mat)
# for row in result:
#     print(row)


# str = input("Enter a string: ")
# words=[i.capitalize() for i in str.split() ]
# words.sort()
# for i in words:
#     print(i)



# punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# str=input('Enter the string:')
# no_panch=''
# for i in str:
#     if i not in punct:
#         no_panch+=i
# print(no_panch)


# def find_n_largest_number(lst,n):
#     sorted_lst=sorted(lst,reverse=True)
#     largest_ele=sorted_lst[:n]
#     return largest_ele

# lst=[10,30,70,30,50,89,100]
# print(find_n_largest_number(lst,3))

        
# lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
# res=[i for i in lists if i]
# print(res)


# lst=[1,2,3,4,5]
# res=lst[:]
# print(res)



# def romove_char(str,i):
#     for i in str:
#             res=str[:i]+str[i+1:]
#             return res
# print(romove_char('hellow wWords',7))
    
    
# str= "piyush sharma"
# dchar=[]
# for i in str:
#     if str.count(i)>1:
#         dchar.append(i)
# print(set(dchar))


# x,y=map(int,input('Enter the two digit (x,y):').split(','))
# arr=[[i for j in range(y)] for i in range(x)]

# for i in range(x):
#     for j in range(y):
#         arr[i][j]=i*j


# for i in arr:
#     print(i)


# class Devision:
#     def __init__(self,n):
#         self.n=n

#     def divisible_by_seven(self):
#         for i in range(self.n+1):
#             if i%7==0:
#                 yield i


# d=Devision(56)
# print(list(d.divisible_by_seven()))


# class PySpider:
#     student='Rekha'
#     id_card=123
#     sub='python'
#     fees=20000
# # print(PySpider.student)
# # print(PySpider.student())
# p=PySpider
# print(p)
# p=PySpider()
# print(p)
    
    
    
# class Sample:
#     @classmethod
#     def add(self):
#         print()' I am a class method')
    
# Sample.add()
# S=Sample()
# print(S.add())


# class ClassName:
#     @staticmethod
#     def fun():
#         print('Hi jaya')
# ClassName.fun()


# ClassName.__init__(object)
# class Animal:
#     def __init__(self):
#         print('Welcome to  zoo  all of you..')
#     def sound(self):
#         print(f'Dogs says bowbow...')
# a=Animal()
# a.sound()

# Animal.__init__(a)


# class demo:
#     @staticmethod
#     def __init__(self):
#         print('Hi I am a static member of the demo')
    
#     def show(self):
#         print('I will show you static method')

# d=demo(123)
# d.show()



# class Addition:
#     def __init__(self):
#         n1=eval(input('Enter the number:'))
#         n2=eval(input('Enter the 2nd number:'))
#         if isinstance(n1,int) and isinstance(n2,int):
#             return n1+n2
#         else:
#             return 'number are not integers'
        
#     def add(self):
#         print('addition of numbers')

# a=Addition()



# class UCO:
#     def __init__(self):
#         bal=5000
#         ac_name='jaya'
#         acc_num=1234567
#         print(f'Dear Mr. {ac_name} ur account number is {acc_num} with balance is {bal}')

# u=UCO()
# u1=UCO()


# class SBI_bank:
#     def __init__(self,name,address, mob):
#         acc_name=name
#         acc_add=address
#         acc_mob=mob
#         print(f'Dear {acc_name} ur staying in {acc_add} ur number ends with xxxxx {acc_mob}')
# s=SBI_bank('Jaya','Patel Nager',123457909)
        
        
# arr=[7,4,5,2,3]
# n=len(arr)
# for i in range(n):
#     for j in range(i+1,n):
#         for k  in range(n):
#             if arr[i]+arr[j]==arr[k]:
#                 print(f'sum of {arr[i]} + {arr[j]} = {arr[k]}')
            # else:
            # print(f'sum of {arr[i]} + {arr[j]} =! {arr[k]}')

            

# s='hello world'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# most_comm=None
# max_count=0
# for i, j in d.items():
#     if j>max_count:
#         most_comm=i
#         max_count=j
# print(f'{most_comm} :  {max_count}')

# l=[1,2,3,4,5,6,7]
# for i in l:
#     l.remove(i)
# print(l)


# count=0
# n=int(input('Enter the number:'))

# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('prime number')

# else:
#     print('not prime number')



# n=int(input('Enter the number:'))
# temp=n
# rev=0
# while(n>0):
#     d=n%10
#     rev=rev+d*d*d
#     n=n/10
# print('it is armstrong number')



# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
# print(gcd(10,20))


# a=10
# b=20
# if a>b:
#     min=a
# else:
#     min=b
# while True:
#     if min%a==0 & min%b==0:
#         print(min)
#         break
#     min+=1

# def miss_number(arr):
#     n=len(arr)
#     total_sum=sum(arr)
#     ac_sum=(n*(n+1))//2
#     mis_number=ac_sum - total_sum
#     return mis_number
# print(1,2,3,4,6,8,9,10)


# a=[1,2,3,4,6,7,9]
# mis=[]
# for i in range(len(a)):
#     if i not in a:
#         mis.append(i)
# print(mis)


# arr = [3, 9, 1, 15, 6, 12]
# lar=0
# small=0
# for i in arr:
#     if i<small:
#         small=i
#     elif i>small:
#         lar=i
#     else:
#         None
# print(lar)


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum=10
# for i, j in enumerate(arr):
#     for k,l in enumerate(arr):
#         if j+l==10 or j-l==10 and j!=l:
#             print(i,k)
            
            
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum=7
# pair=[]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==sum:
#             print(arr[i],arr[j])
            
            
# def remove_duplicates_in_place(arr):
#     # Use set to store unique elements encountered so far
#     seen = set()

#     # Use list comprehension to construct a new list with only unique elements
#     # in the original order
#     arr[:] = [x for x in arr if not (x in seen or seen.add(x))]

# # Example usage:
# arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9, 2]
# remove_duplicates_in_place(arr)
# print("Array after removing duplicates:", arr)


# arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9, 2]
# res=set()
# var= [i for i in arr if not (i in res or  res.add(i) ) ]
# print(var)


# arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9, 2, 5]
# arr_set=set(arr)
# min_num=min(arr_set)
# max_num=max(arr_set)
# all_number_set=set(range(min_num,max_num+1))
# mis_num=sorted(all_number_set-arr_set)
# print(mis_num)


# def permulattion(s):
#     res=[]
#     for i,j in enumerate(s):
#         permu_of_rest=permulattion(s[:i]+s[i+1:])

#         for k in permu_of_rest:
#             res.append(j+k)
#     return res
# print(permulattion('abc'))


# with open(soruce_path, 'rb') as souces:
#     with open(destination, 'wb') as destination:
#         contant= souces.read()
#         destination.write(contant)
#         print('file is copy successfully')



# s='hello world'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# max_item=None
# max_count=0
# for i, j in d.items():
#     if j>max_count:
#         max_item=i
#         max_count=j
# print(f'{max_item} : {max_count}')


# str='aabaabaaabde'
# max_len=0
# n=len(str)

# for i in range(n):
#     for j in range(i+1,n+1):
#         substr=str[i:j]
#         if len(set(substr))==len(substr):
#             max_len=max(max_len, len(substr))
# print(max_len)


# str='aabaabaaabde'
# max_len=0
# n=len(str)
# for i in range(n):
#     for j in range(i+1,n+1):
#         substr=str[i:j]
#         if len(set(substr))==len(substr):
#             # max_len=max(max_len,len(substr))
#             max_len=max(max_len,len(substr))
# print(max_len)


# count=0
# n=int(input('Enter the number:'))        
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('it is prime number')
# else:
#     print('it is not prime number')
    
    
    
# count=0
# n=int(input('Enter the number:'))
# for i in range(1,n+1):
#     cn=i
#     count=0
#     for j in range(1,cn+1):
#         if cn%j==0:
#             count+=1
#     if count==2:
#         print(cn)


# var=input('Enter the number:')
# # var=str(n)
# if var==var[::-1]:
#     print('it is palindrome number')
# else:
#     print('it is not palindrome number')


# def fact(n):
#     f=1
#     i=1
#     while i<n:
#         f=f*i
#         i+=1
#     return f

# nlines=int(input('Enter the number of lines:'))
# for x in range(nlines):
#     for y in range(x+1):
#         print(fact(x)//(fact(y)*fact(x-y))," ",end='')
#     print()
        
        
# year=int(input('Enter the year:'))
# if (year%4==0 and year%100!=0 or year%400==0):
#     print('it is a leap year')
# else:
#     print('it is not a leap year')
    
    
# i=1
# sum=0
# n=int(input('Enter the number:'))
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print('it is perfact number')
# else:
#     print('it is not perfact number')


# sum=0
# n=int(input('Enter the number:'))
# # i=1
# for j in range(1,n+1):
#     if n%j==0:
#         sum+=j
#     j+=1
# if sum==n:
#     print('it is a perfact number')
# else:
#     print('it is not perfact number')
    
    
# sum=0
# i=1
# n=int(input('Enter thenumber:'))
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print('it is perfact number')
# else:
#     print('it is not perfact number')



# n=int(input('Enter the number:'))
# t=n
# rev=0
# while (n>0):
#     a=n%10
#     rev=rev+a*a*a
#     n=n//10
# if (rev==t):
#     print('Armstrong number')
# else:
#     print('it is not armstrong number')
    
    
    
# n=int(input('Enter the number:'))
# t=n
# r=0
# while(n>0):
#     a=n%10
#     r=r+a*a*a
#     n=n//10
# if (rev==t):
#     print('Armstrong number')
# else:
#     print('it is not armstrong number')


# str='hello world'
# vo=0
# cons=0
# for i in str:
#     if i in 'AEIOUaeiou':
#         vo+=1
#     elif i not in 'AEIOUaeiou' and i!=' ':
#         cons+=1
#     else:
#         None
# print(vo)
# print(cons)


# s='Hello world'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1

# print(d)
# max_len=None
# max_count=0

# for i,j in d.items():
#     if j>max_count:
#         max_len=i
#         max_count=j
# print(max_count)
# print(max_len)
    

# arr=[25,10, 30,12,20]
# sm=arr[0]
# for i in arr:
#     if i>sm:
#         sm=i
# print(sm)


# arr=[25,10,30,12,20]
# ln=arr[0]
# for i in arr:
#     if i>ln:
#         ln=i
# print(ln)


# arr=[25,10,30,12,20]
# sec_small=arr[0]
# for i in arr:
#     if i<sec_small:
#         sec_small=i
# print(sec_small)


# arr=[25,10,30,12,20]
# small=largest=float('inf')
# for i in arr:
#     if i<small:
#         small=i
#     elif i>small:
#         largest=i
# print(small)
# print(largest)
        
# arr=[20,30,10,13,18,16]
# max_num=max(arr)
# var=[a for i,a in enumerate(arr) if a>=max_num]
# print(var)


# arr=[20,10,30,15,25,20]
# arr.sort(reverse=True)
# print(arr[1], arr[-2])


# arr=[20,10,30,15,25,20]
# var=arr[0]
# for i in arr:
#     if i>var:
#         var=i
# print(var)


# Find Second Smallest and Second Largest Element in an array
# arr=[20,10,30,15,25,20]
# def second(arr):
#     m1=m2=float('inf')
#     for i in arr:
#         if i<=m1:
#             m1,m2=i,m1
#         elif i<m2:
#             m2=i
#     return m2
# print(second([20,10,30,15,25,20]))
            
# def second(arr):
#     m1=m2=float('inf')
#     for i in arr:
#         if i<=m1:
#             m1,m2=i,m1
#         elif i<m2:
#             m2=i
#     return m2
# print(second([20,10,30,15,25,20]))


# def second(arr):
#     m1=m2=float('inf')             # ! Wrong
#     for i in arr:
#         if i>=m2:
#             m1,m2=i,m2
#         elif i>m1:
#             m1=i
#     return m2
# print(second([20,10,30,15,25,20]))


# def table(n):
#     res=[]
#     for i in range(1,n+1):
#         res.append((n, 'X', i, '=', n*i))
        
#     return res

# print(table(10))

# def table(n):
#     for i in range(1,n+1,1):
#         for j in range(1,n+1,1):
#             print(i*j, end=' ')
#         print()
        
# table(2)


# def table(n):
#     t=''
#     for i in range(1,n+1):
#         t+=f'{n} X {i}= {n*i}\n'
#     return t
# print(table(10))


# import math
# first=math.inf
# second=math.inf
# arr = [10, 13, 17, 11, 34, 21]
# for i in range(0,len(arr)):
#     if arr[i]<first:
#         second=first
#         first=arr[i]
#     elif (arr[i]!=second and arr[i]<second):
#         second=arr[i]
# print(second)


# import math
# first=math.inf
# second=math.inf
# arr = [10, 13, 17, 11, 34, 21]              # ! o/p : inf
# for i in range(0,len(arr)):
#     if arr[i]>first:
#         second=first
#         first=arr[i]
#     elif (arr[i]!=second and arr[i]>second):
#         second=arr[i]
# print(second)


# def smallest(arr):
#     smallest=float('inf')
#     sec_small=float('inf')

#     largest=float('inf')
#     sec_largest=float('inf')

#     for i in arr:
#         if i<smallest:
#             sec_small=smallest
#             smallest=i
#         elif i!=smallest and i<sec_small:
#             sec_small=i
#     # return sec_small


    
#         if i>largest:
#             sec_largest=largest
#             largest=i

#         elif i!=largest and i>sec_largest:
#             sec_largest=i

#     return sec_largest,sec_small
    
# print(smallest([12, 4, 7, 1, 9, 15, 3, 11]))


# def number(arr):
#     small=float('inf')
#     sec_small=float('inf')

#     large=float('-inf')
#     sec_large=float('-inf')

#     for i in arr:
#         if i<small:
#             sec_small=small
#             small=i
#         elif i<sec_small and i!=small:
#             sec_small=i

#         if i>large:
#             sec_large=large
#             large=i
#         elif i>sec_large and i!=large:
#             sec_large=i
#     return sec_large, sec_small
# print(number([12, 4, 7, 1, 9, 15, 3, 11]))

# arr=[12, 4, 7, 1, 9, 15, 3, 11]
# rev=[]
# for i in arr:
#     rev=[i]+rev
# print(rev)


# arr=[12, 4, 7, 1, 9, 15, 3,4,4,4,3,1, 11]
# d={}
# for i in arr:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# most_comm=None
# most_count=0
# for i,j in d.items():
#     if j>most_count:
#         most_comm=i
#         most_count=j

# print(most_comm,most_count)
    
    
# def sorted_arr(arr):
#     mid=len(arr)//2
#     arr[:mid]=sorted(arr[:mid])

#     arr[mid:]=sorted(arr[mid:],reverse=True)

#     return  arr[:mid]+arr[mid:]
# print(sorted_arr([12, 4, 7, 1, 9, 15, 3,4,4,4,3,1, 11]))


# arr=[10,20,30,40,50]
# def rotate(arr,n):
#     return arr[-n:]+arr[:-n]
# print(rotate(arr,3))


# def median(arr):
#     arr.sort()
#     n=len(arr)
#     m=n//2
#     if n%2==0:
#         return (arr[m-1]+arr[m])/2
#     else:
#         arr[m]
# print(median([20,10,30,40,50,60]))


# arr=[10,20,30,10,30,40]
# l=[]
# d_l=[]
# for i in arr:
#     if i not in l:
#         l.append(i)
#     else:
#         d_l.append(i)
# print(l)
# print(d_l)


# arr=[10,20,30,40,50]
# # print(arr.insert(2,100))
# # print(var)

# arr.insert(2,1000)
# print(arr)


# def symetric_pair(arr):
#     result=[]
#     seen=set()
#     for i in arr:
#         rev_pair=(i[1],i[0])
#         if rev_pair in seen:
#             result.append(i)
#         else:
#             seen.add(i)
#     return result

# print(symetric_pair([(1, 2), (2, 1), (3, 4), (5, 6), (6, 5), (7, 8)]))


# def sym_pair(arr):
#     res=[]
#     seen=set()
#     for i in arr:
#         rev_pair=(i[1],i[0])
#         if rev_pair in seen:
#             reult.append(i)
#         else:
#             seen.add(i)
#     return result
# print(sym_pair([(1, 2), (2, 1), (3, 4), (5, 6), (6, 5), (7, 8)]))


# arr=[1,2,3,4,5,0]
# sum=1
# for i in range(len(arr)):
#     if arr[i]==0:
#         pass
#     else:
#         sum*=arr[i]
# print(sum)


# arr=[1,2,2,4,0,0,10]
# sum=1
# for i in range(len(arr)):
#     if arr[i]==0:
#         pass
#     else:
#         sum*=arr[i]
# print(sum)


# arr=[20, 15, 26, 2, 98, 6]
# for i,j in enumerate(arr):
    # print((i,j),end=' ')
     
    
# #  ? Sort Elements of an Array by Frequency 
# arr=[4, 4, 2, 8, 3, 3, 1, 1, 1, 8, 8, 8]
# from collections import  Counter
# def count_freq(arr):
#     ele_count=Counter(arr)
#     sorted_arr=sorted(arr,key=lambda x:(ele_count[x],x),reverse=True)
#     return sorted_arr

# print(count_freq(arr))


# arr=[10,20,30,30,30,40,40,10]
# from collections import Counter
# def count_freq(arr):
#     ele_count=Counter(arr)
#     sorted_arr=sorted(arr,key=lambda i:(ele_count[i],i),reverse=False)
#     return sorted_arr
# print(count_freq(arr))



# from collections import Counter

# arr=[4, 4, 2, 8, 3, 3, 1, 1, 1, 8, 8, 8]
# ele_count=Counter(arr)
# var=sorted(arr,key=lambda i:(ele_count[i],i),reverse=True)
# print(var)


# def find_index(arr,target):
#     try:
#         return arr.index(target)
#     except ValueError:
#         return -1
# print(find_index([1, 2, 3, 4, 5],3))


# def find_index(arr,ele):
#     return arr.index(ele)
# print(find_index([1, 2, 3, 4, 5],4))


# arr1= [1,3,4,5,2]
# arr2= [2,4,3,1,7,5,15]
# if set(arr1).issubset(set(arr2)):
#     print('It is subset of arr1')
# else:
#     print('it is not subset of arr1')

# arr1=[1,3,4,5,2]
# arr2= [2,4,3,1,7,5,15]



# def is_palindrome(num):
#       return str(num) == str(num)[::-1]

# def find_palindromes(lower, upper):
#   return [num for num in range(lower, upper + 1) if is_palindrome(num)]

# lower_limit = 100
# upper_limit = 999
# palindromes = find_palindromes(lower_limit, upper_limit)

# print(f"Palindrome numbers between {lower_limit} and {upper_limit} are: {palindromes}") if palindromes else print(f"No palindrome numbers found between {lower_limit} and {upper_limit}.")

# def palindrome(n):
#     return str(n)==str(n)[::-1]

# def find_palindromes(lower,upper):
#     return [n for n in range(lower,upper+1) if palindrome(n)]

# print(find_palindromes(10,400))


# def is_palindrome(num):
#     return str(num) == str(num)[::-1]

# palindromes = [num for num in range(100, 1000) if is_palindrome(num)]
# print(palindromes) if palindromes else print("No palindromes found in the range.")

# def is_palindrome(num):
#     return str(num)==str(num) [::-1]
# palindrome=[i for i in range(10,500) if is_palindrome(num)]       # ! Wrong
# print(palindrome)



# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# def palindrome(s,e):
#     l=[]
#     for i in range(s,e+1):
#         if is_palindrome(i):
#             l.append(i)
#     return l
# print(palindrome(100,500))


# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# def palindrome(s, e):
#     l = []
#     for i in range(s, e + 1):
#         if is_palindrome(i):
#             l.append(i)
#     return l

# print(palindrome(100, 500))




# def number(n):
#     n_str=str(n)
#     digit=[int(i) for i in n_str]
#     max_digit=int(max(digit))
#     min_digit=int(min(digit))

#     return max_digit, min_digit
# var=number(486215)
# print(var)


# s='hello world'
# len=0
# for i in s:
#     len+=1
# print(len)

# s='hello world'
# u='univese'
# r=''
# for i in s.split():
#     if i=='world':
#         r+=u
#     else:
#         r=i+' '
# print(r)


# s='hello world'
# l=[]
# str=''
# for i in s:
#     l+=[i]
# print(l)
        
        
# s='hello world'
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)
    
    
# def swap(str, s1=''):
    
#     for i in str:
#         if 'a'<=i<='z' and i!=' ':
#             s1+=chr(ord(i)-32)
#         else:
#             s1+=chr(ord(i)+32)
#     return ' '.join(s1.split('@'))
# print(swap('heLLo world'))
# print(swap('HELLO WORLD'))


# a=10
# b=20
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)


# sentence = 'hello world welcome to python programming hi there'

# d = {}
# for word in sentence.split():
#     if word[0] not in d:
#         d[word[0]] = [word]
# #
#     else:
#         d[word[0]] += [word]
# print(d)


# sentence = 'hello world welcome to python programming hi there'
# d={}
# for i in sentence.split():
#     if i[0] in d:
#         d[i[0]]+=[i]
#     else:
#         d[i[0]]=[i]
# print(d)
        


# sentence = 'hello world welcome to python programming hi there'
# from collections import  defaultdict
# d=defaultdict(list)
# for i in sentence.split():
#     d[i[0]]+=[i]
# print(d)
    
    
    
# l = [34, 'hello', 'apple', 56.7, 4546, 67.8,
# 'google', 45]

# def operation(lst,res=[]):
#     for i in lst:
#         if isinstance(i,str):
#             res.append(i)
#         elif isinstance(i,int):
#             res+=[int(str(i)[::-1])]
#         elif isinstance(i,float):
#             res+=[int(str(i)[::-1])]
#     return res
# print(operation(l))


# s = 'Life is full of surprises and miracles'
# l_word=''
# length=0
# for i in s.split():
#     if len(l_word)<len(i):
#         l_word=i
# print(l_word)

# s = 'Sony12India567pvt21ltd'
# sum=0
# for i in s:
#     if i.isdigit():
#         sum+=int(i)
# print(sum)


# import asyncio
# async def fetch_data():
#   print('start fetching data')     
#   await asyncio.sleep(2)
#   print('done fetching data')
#   return {'data': 'sample'}

# async def main():
#   print('start main')
#   data = await fetch_data()
#   print('Recieved data:', data)
#   print('end main')
# asyncio.run(main())



