class fib:
    def On_list(num):
        fibs=[0,1]
        a=0
        b=1
        c=0
        if num==0:
            return [0]
        elif num==1:
            return [0,1]

        for i in range(3,num+1):
            c=a+b
            a=b
            b=c
            fibs.append(c)
        return fibs

    def Just_num(num):
        a=0
        b=1
        c=0
        if num==0:
            return 0
        elif num==1:
            return 1
        for i in range(3,num+1):
            c=a+b
            a=b
            b=c
        return c