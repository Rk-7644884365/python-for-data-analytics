# bubble sort implementation
# import numpy as np
# a=np.array([4,5,6,8,3])
# for i in range (len(a)):
    # for j in range(0,len(a)-i-1):
        # if a[j]>a[j+1]:
            # a[j],a[j+1]=a[j+1],a[j]
# print(a)

# def bubble_sort(arr):
    # n = len(arr)
    # for i in range(n):
        # for j in range(0, n-i-1):
            # if arr[j] > arr[j+1]:
                # arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr
# print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# selection sort implementation
# import numpy as np
# a=np.array([4,5,3,6,7,2,4,7])
# for i in range(len(a)):
    # min_indx=i
    # for j in range(i+1,len(a)):
        # if a[j]>a[min_indx]:
            # min_indx=j
    # a[i],a[min_indx]=a[min_indx],a[i]
# print(a)



def selection(*arr):
    arr=list(arr)
    for i in range (len(arr)):
       indx=i
       for j in range(i+1,len(arr)):
           if (arr[j]<arr[indx]):
               indx=j
           arr[indx],arr[i]=arr[i],arr[indx]
    return arr
print(selection(7,5,6,7,4,5,3,4,5))