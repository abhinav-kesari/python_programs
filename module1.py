arr =[]
while True:
    x=int(input())
    if x ==-1:
        break
    else:
        arr.append(x)

for i in range(len(arr)):
    if arr[i]%10==8 and arr[i]%9==0:
        arr[i]=-7
    elif arr[i]%10==8:
        arr[i]=-6
    else:
        arr[i]=-3
for i in arr:
    print(i)
