def qsort(li):
    if len(li)<=1:
        return li
    piv=li[0]
    left=[li[i] for i in range(1,len(li)) if li[i]<piv]
    right=[li[i] for i in range(1,len(li)) if li[i]>=piv]
    return qsort(left)+[piv]+qsort(right)


li=[4,76,2,6,8,234,54,45,5767,43]

print(qsort(li))
        