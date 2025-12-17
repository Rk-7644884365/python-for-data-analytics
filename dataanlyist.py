# computer / mechine  only understand binary language
# Python is a high level programming language
# Python is a interpreted language
# Python is a object oriented programming language

# character
# digit =0 to 9
# alphabet=A TO Z ,a to z
# special character = ! @ # $ % ^ & * ( ) _ + - = { } [ ] | \ : ; " ' < > , . ? / space4
# whitespace character = space, tab, newline

# data type in python
# 1.integer (int)=3,5,,6,8 interger only carray digit charters it is accept only  wholw number
# 2.float=3.5,6.7,8.9 it carray digit and decimal point, it must be accept only digit charater
# 3.string (str)='a','abc',"hello" it carray alphabet,digit,special character, it is accept within quote single or
# double
# singe quates used for single line string and "" also used for single line string
    # ''' ''' used for multi line string
    # """ """ used for multi line string
# 4.boolean (bool)=True,False it carray two value only true and false

# variables in python
# varibale is container to store data
# a=10  # a is variable name ,10 is value assigned to variable
# identifier rules in python
# 1.identifier name must start with alphabet (a to z ,A to Z) or underscore(_)
# ir does not start with digit (0 to 9) and space
# key word can not be used as identifier
# 3.identifier name can not contain special character except underscore(_)

# comment
# single line comment start with # multi line comment start with ''' ''' or """ """

# a='''bqhABHJWSBJHS
# ASJKDNJKWS''' multiline string
# '''KJASNKJDS JSAKBDJES JDBSDDJBES JEBDSDD
# SDHADXUJEBSZK
# EBDSKJD
# ''' MULTILINE COMMENT


# type casting in python
# converting one data type to another data type is called type casting

# integer to float
# a=10
# a=float(a)
# print(a)
# print(type(a))

# a=10
# a=20.5
# print(a)

# float to integer
# a=20.5
# a=int(a)
# print(a)

# string to integer
# a='100'
# a=int(a)
# print(a)

# INT TO STRING4
# a=50
# a=str(a)
# print(type(a)) # type function is used to know the data type of variable

# string to float
# a='495.65'
# a=float(a)
# print(a)

# float to string
# a=67.89 
# a=str(a)
# print(a)

###### undersatd by print function ######
# print function is used to display output on the screen
# print('hello world') # string output
# print(100) # integer output
# print(45.67) # float output
# print(True) # boolean output

# a=10
# print('a')
# print(a)


# oprator in python
# arithmetic oprator # + - * / % // **
#comparision oprator # == != > < >= <=
# assignment oprator # = += -= *= /= %= //= **=
# logical oprator # and or not
# bitwise oprator #& | ^ ~ << >>
# membership oprator # in not in
# identity oprator # is is not


# ArithmeticError
#addition oprator +
# a=10
# b=20
# print(a+b)
# print(a-b)  # subtraction oprator -
# print(a*b)# multiplication oprator *
# print(a/b)# division oprator /
# print(a%b)# modulus oprator % # remander
# print(a//b)# floor division oprator // floor value
# print(a**4)# exponentiation oprator **

# comparision oprator /relational oprator
# a=10
# b=20
# print(a==b) # equal to oprator
# print(a!=b) # not equal to oprator
# print(a>b) # greater than oprator
# print(a<b) # less than oprator
# print(a>=b) # greater than equal to oprator
# print(a<=b) # less than equal to oprator\

# assignment oprator
# a=10
# print(a) # assignment oprator =
# a+=1 # a=a+1
# print(a)
# a-=1 # a=a-1
# print(a)
# a*=2 # a=a*2
# print(a)
# a/=2 # a=a/2
# print(a)
# a%=3 # a=a%2
# print(a)
# a//=2 # a=a//2
# print(a)
# a**=2 # a=a**2
# print(a)


#logical operator
# and 
# T T=True
# T F=False
# F T=False
# F F=False
# a=10
# b=20
# print(a>5 and b>15) # True and True =True
# print(a>5 and b<15) # True and False =False
# print(a<5 and b>15)     # False and True =False
# print(a<5 and b<15) # False and False =False

# or
# T T=True
# T F=True
# F T=True
# F F=False
# a=12
# b=25
# print(a>10 or b>20) # True or True =True
# print(a>10 or b<20) # True or False =True
# print(a<10 or b>20)    # False or True =True
# print(a<10 or b<20) # False or False =False
# 
# not
# T=False
# F=True
# a=15
# print(not(a>10)) # not True =False
# print(not(a<10)) # not False =True


# bitwise oprator
# and =&
# or =|
# xor=^
# not=~
# left shift=<<
# right shift=>>
# a=10 # binary=1010
# b=4  # binary=0100
# print(a&b) # and oprator 0000=0
# print(a|b) # or oprator 1110=14
# print(a^b)# xor oprator 1110=14
# print(~a) # not oprator -(n+1) =-11
# print(a<<2) # left shift oprator 101000=40
# print(a>>2) # right shift oprator 0010=2

# membership oprator
#in
# a=[10,20,30,40,50]
# print(20 in a) # True
# print(60 in a) # False
# not in
# print(20 not in a) # False
# print(60 not in a) # True

# identity oprator
#is
# a='mohit'
# print(a is 'mohit')
# print(a is not 'mohit')


# input function in python
# input function is used to take input from user
# a=int(input('this is my first user input')) # input function always take input as string
# print(a)

# String 
# a='hello world'
# print(a)
# print(type(a))
# string is buit in data type in python
# string is a sequence of characters
# string is immutable

# ' ',"" it represent single line string
# ''' ''' , """ """ it represent multi line string

# a='hello' # single line string
# b="asjdn" # single line string
# c='''hskbdkjes
# hdsjcnekds
# fhsdoifhne
# hrdoicn
# ''' # multi line string
# d="""kasbdk
# dsnlejksn
# idsn"""    # multi line string

# a='hello world'
# a[2]='x'    # string is immutable it can not be changed
# print(a)

# fuction in python
# len # len function is used to find the length of string
# a='hello world'
# print(len(a))
# count # count function is used to count the number of occurrences of a substring in a string
# a='hello world'
# print(a.count('o'))
# find # find function is used to find the index of first occurrence of a substring in a string
# a='hello world'
# print(a.find('o'))
# print(a.rfind('l')) # rfind function is used to find the index of last occurrence of a substring in a string

# all buit in data type are contable 
# index
# a='my name is ravi kumar'
# forword indexing start with Zero 
# and reversed start with -1
# 
# print(a.index('m')) # first occurance of m
# print(a.rindex('m')) # last occurance of m

# a="my name is ravi kumar"
# print(a[3])
# print(a[-1])

# sclicing
# using for finding the subset 
# a="my name is ravi kumar"
# print(len(a))
# print(a[start:end:step]) 
# print(a[3:7:1])
# starting  defualt 0
# ending defluat is len 

# defualt step is 1
# print(a[:8:2])
# print(a[2::1])

# print(a[2:5])

########## reverse sciling
a="my name is ravi kumar"
# print(a[-1:-5:-1])
# print(a[-5:-1:-1])
# default reverse indexing -1
# default statinng take -1
# default ending take -(len of string +1 )
print(a[::-1])


