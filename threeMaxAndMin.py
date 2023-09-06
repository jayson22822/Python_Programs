n=int(input())
arr=[int(input()) for i in range(n)]
odd=[]
for all in arr:
    if all % 2 == 1:
        odd.append(all)
odd.sort()
print(odd[0:3])
odd.reverse()
print(odd[0:3])