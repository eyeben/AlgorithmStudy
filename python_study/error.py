name={
    'kim':1,
    'park':2,
    'choi':3
}

# try:
#     a='kim'
#     b=name[a]
#     print('{} is number {}'.format(a,b))
# except:
#     print("error occured")
# else:
#     print("no errors")
# finally:
#     print("whatever")


try:
    c='kim'
    d=name[c]
    if c=='park':
        print('%s is number %d'%(c,d))
    else:
        raise ValueError
except ValueError as er:
    print("%s has occured"%(str(er)))
except Exception as f:
    print(f)
else:
    print("no errors")
finally:
    print("always print")




