# letter="mototm"
# def check(letter):
#     if len(letter)<=1:
#         return True
#     if letter[-1]!=letter[0]:
#         return False
#     return check(letter[1:-1])
# print(check(letter))
# #-------------------------------------------------------
# num=3

# def cal(num):
#     if num==1:
#         return
#     if num%2==0:
#         print(num//2)
#         cal(num//2)
#     else:
#         print(num*3+1)
#         cal(num*3+1)

# def cal2(num):
#     print(num)
#     if num==1:
#         return 1
#     if num%2==1:
#         return(cal2(3*num+1))
#     else:
#         return(cal2(num//2))
    
# print(cal2(num))
# #-------------------------------------------------------

def cnt(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    return cnt(n-1)+cnt(n-2)+cnt(n-3)

print(cnt(10))
    