
# if one or more parameter exists, args takes it as tuple
def args_func(*args):
    print(args)

# also does the same but takes is as dict
def kwargs_func(**kwarg):
    for k,v in kwarg:
        print(k,v)
args_func('a','b','c')
args_func('1')
kwargs_func(n1=1,n2=2,n3=3)

lambda_example=lambda num:num*100

def multiples(x,y,func):
    print(x*y*func(1))
print(multiples(10,10,lambda_example))
