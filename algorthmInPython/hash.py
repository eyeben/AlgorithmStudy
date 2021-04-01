# hash_table=list([0 for i in range(8)])
# def get_key(data):
#     return hash(data)
# def hash_func(key):
#     return key%5

# def save_data(data,value):
#     serial=get_key(data)
#     hash_address= hash_func(serial)
#     if hash_table[hash_address]==0:
#         hash_table[hash_address]=[[serial,value]]
#     else:
#         for i in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][i][0]==serial:
#                 hash_table[hash_address][i][1]=value
#                 return
#         hash_table[hash_address].append([serial, value])

# def read_data(data):
#     serial=get_key(data)
#     hash_address=hash_func(serial)
#     for i in range(len(hash_table[hash_address])):
#         if hash_table[hash_address][i][0]==serial:
#             return hash_table[hash_address][i][1]
#     return None

# save_data('Dd', '1201023010')
# save_data('Data', '3301023010')
# print(read_data('Dd'))
# print(hash_table)

hash_table=list([0 for i in range(8)])
def get_key(data):
    return hash(data)
def hash_func(key):
    return key%5
def save_data(data, value):
    serial=get_key(data)
    hash_address=hash_func(serial)
    if hash_table[hash_address]==0:
        hash_table[hash_address]=[[serial,value]]
    else:
        for i in range(hash_address,len(hash_table)):
            if hash_table[i]==0:
                hash_table[i]=[[serial, value]]
                return
            elif hash_table[i][0]==serial:
                hash_table[i][1]=value
        
def read_data(data):