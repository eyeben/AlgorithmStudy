# print
print("{} and {}".format("alpha", "beta"))
print("%s and %s"%("alpha", "beta"))
print("alpha", "beta", sep=" and ")

# list
list_a=[i for i in range (10) if i%2==0]
list_b=[i for i in range (10) if i%2!=0]

list_a[0:1]=[-4,-2]
print(list_a)

list_a.extend(list_b)
print(list_a)

# tuple
tuple_a=(0,)
tuple_b=(4, 5, 6)

print(tuple_a+tuple_b)
print(tuple_b.index(5))

# set
set_a=set([2, 4, 6, 8, 10])
set_b=set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])

print(set_a.union(set_b))
print(set_a & set_b)
print(set_a.intersection(set_b))
print(set_b.difference(set_a) )
print(set_b-set_a)

tmp=list(set_a)

# dict
dic={
    "name":"park",
    "sex":"M",
    "phone":"000"
}

for k,v in dic.items():
    print(k,"is",v,)