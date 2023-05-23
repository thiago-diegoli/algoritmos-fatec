def mdc(n1, n2):
    mdc1 = [i for i in range(1,n1+1) if n1 % i == 0][::-1]
    mdc2 = [i for i in range(1,n2+1) if n2 % i == 0][::-1]
    for i in max(mdc1,mdc2):
        if i in min(mdc1,mdc2):
            return i
    return 0

