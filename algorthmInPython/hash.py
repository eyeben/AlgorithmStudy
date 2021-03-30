hash_table=list([0 for i in range(10)])
def get_key(data):
    return hash(data)
def hash_func(key):
    return key%5
def save_data(data,value):
    hash_address= hash_func(get_key(data))
    hash_table[hash_address]=value
def read_data(data):
    hash_address=hash_func(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Dave'))