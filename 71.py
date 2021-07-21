def S_trianle(a,b,c):
    p = (a+b+c)/2
    s = pow(p*(p-a)*(p-b)*(p-c), 1/2)
    return s
print(S_trianle(a,b,c))

if __name__ == '__main__':
    S_trianle(a,b,c)
