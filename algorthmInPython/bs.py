def bs(data, search):
    if len(data)==1 and search==data[0]:
        return True
    if len(data)==1 and search!=data[0]:
        return False

    med=len(data)//2
    if search==data[med]:
        return True
    elif search<data[med]:
        return bs(data[:med],search)
    else:
        return bs(data[med:],search)

li =[i for i in range(1,101)]

print(bs(li, 9))
        
    
    