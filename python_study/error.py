name={
    'kim':1,
    'park':2,
    'choi':3
}

try:
    a='kim'
    b=name[a]
    print('{} is number {}'.format(a,b))
except:
    print("error occured")
else:
    print("no errors")
finally:
    print("whatever")



