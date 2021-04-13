original=[98,4,7,3,2,8,34,6,9,245,78,34,1]
li=list(original)

for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)
li=list(original)

for i in range(len(li)-1):
    idx=i
    for j in range(i+1,len(li)):
        if li[idx]>li[j]:
            idx=j
    li[i],li[idx]=li[idx],li[i]
        
print(li)
li=list(original)

for i in range(len(li)-1):
    for j in range(i+1,0,-1):
        if li[j]<li[j-1]:
            li[j-1],li[j]=li[j],li[j-1]
        else:
            break

print(li)