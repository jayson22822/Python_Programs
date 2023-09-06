def direction(arr,first,second):
# clockwise or anti clockwise
    idx_first = arr.index(first)
    idx_second = arr.index(second)
    
    if (idx_first + 1) % len(arr) == idx_second:
        print("Clockwise")
    elif (idx_first - 1) % len(arr) == idx_second:
        print("Anti-clockwise")
    else:
        return "Invalid input"
        
def clockwise(first,g):
    # no of gifts
    arr1=[]
    arr2=[]
    a = arr.index(first)
    while(g >= 1):
        g = g - 1
        if (a >= n):
            a = a % n
        if(arr[a] in arr1):
            i = arr1.index(arr[a])
            arr2[i] = arr2[i] + 1
            b = a
            a = a + 1
        elif(arr[a] not in arr1):
            arr1.append(arr[a])
            arr2.append(1)
            b = a 
            a = a + 1 
            
    for i in range(n):
        if(arr2[i] == max(arr2)):
            print(arr1[i],"-",arr2[i])
    print(arr[b])

def Anticlockwise(first,g):
    # no of gifts
    arr1=[]
    arr2=[]
    a = arr.index(first)
    while(g >= 1):
        g = g - 1
        if (a <= 0):
            a = a % n
        if(arr[a] in arr1):
            i = arr1.index(arr[a])
            arr2[i] = arr2[i] + 1
            b = a
            a = a - 1
        elif(arr[a] not in arr1):
            arr1.append(arr[a])
            arr2.append(1)
            b = a 
            a = a - 1
            
    for i in range(n):
        if(arr2[i] == max(arr2)):
            print(arr1[i],"-",arr2[i])
    print(arr[b])

n=int(input())
arr=[]
for i in range(n):
    a= input()
    arr.append(a)
g=int(input())
first=input()
second=input()
if (direction(arr,first,second) == "Clockwise"):
    clockwise(first,g)
else:
    Anticlockwise(first,g)



            
