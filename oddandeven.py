def sort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]



n = int(input())
lst=[int(input()) for i in range(n)]
arr1=[]
arr2=[]
for i in lst:   
    if i % 2 == 0:
        arr1.append(i)
    elif i % 2 == 1:
        arr2.append(i)
    else:
        pass
sort(arr1)
sort(arr2)
arr=arr1 + arr2
print(arr)