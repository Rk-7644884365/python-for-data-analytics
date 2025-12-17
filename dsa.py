# # bubble sort implementation
# # import numpy as np
# # a=np.array([4,5,6,8,3])
# # for i in range (len(a)):
#     # for j in range(0,len(a)-i-1):
#         # if a[j]>a[j+1]:
#             # a[j],a[j+1]=a[j+1],a[j]
# # print(a)

# # def bubble_sort(arr):
#     # n = len(arr)
#     # for i in range(n):
#         # for j in range(0, n-i-1):
#             # if arr[j] > arr[j+1]:
#                 # arr[j], arr[j+1] = arr[j+1], arr[j]
#     # return arr
# # print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# # selection sort implementation
# # import numpy as np
# # a=np.array([4,5,3,6,7,2,4,7])
# # for i in range(len(a)):
#     # min_indx=i
#     # for j in range(i+1,len(a)):
#         # if a[j]>a[min_indx]:
#             # min_indx=j
#     # a[i],a[min_indx]=a[min_indx],a[i]
# # print(a)



# # def selection(*arr):
#     # arr=list(arr)
#     # for i in range (len(arr)):
#     #    indx=i
#     #    for j in range(i+1,len(arr)):
#         #    if (arr[j]<arr[indx]):
#             #    indx=j
#         #    arr[indx],arr[i]=arr[i],arr[indx]
#     # return arr
# # print(selection(7,5,6,7,4,5,3,4,5))

# # 
# # a=5
# # b=0
# # try :
#     # print("resoure opened")
#     # print(a/b)
#     # print("resoure closed")
# # 
# # except Exception  as e:
#     # print("u chan no div by 0" , e)
# # finally:
#     # 
# # 
#     # print("hello")

# # 
# #
# # a=10
# # b=2
# # try:
#     # print("resource opened")
#     # print(a/b)
#     # print("resource closed")
#     # b=int(input("enter b"))
# # 
# # except ZeroDivisionError as e:
#     # print("u can not div by 0", e)
# # except ValueError as e:
#     # print("value error", e )
# # except Exception as e:
#     # print("some other error", e)
# # finally:
#     # print("hello") 

# # 
# from time import sleep
# from threading import *
# class hello(Thread):
#     def run(self):

#         for i in  range(5):
#            print("hello")
#            sleep(1)


# class hi(Thread):
#     def run(self):

#         for i in  range(5):
#            print("hi")
#            sleep(1)
# t1=hello()

# t2=hi()


# t1.start()
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()




# a=10
# b=2
# try:
    # print(a/b)
    # b=int(input("enter the number:"))
# except ZeroDivisionError as e:
    # print("errorhfff")
# except ValueError as e: 
    # print("errpe ")
# except Exception as e:
    # print("c jansk")
# finally:
    # print("hello")



from time import sleep
from threading import Thread
class hi(Thread):
    def run(self):
        for i in range(10):
            print("hello")
            sleep(1)
class hello(Thread):
    def run(self):
        for i in range(6):
            print('my')
            sleep(1)
t1=hi()
t2=hello()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
