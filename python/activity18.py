def hello(n):
    return n * (n+1) / 2




def fun(n):   # loop method 
    sum = 0 
    for i in range(1,n+1): 
        sum = sum + 1
    return sum


def fun1(n): #nested loop method 
    sum = 0 
    for i in range (1, n+1):
        for j in range (i,i+1):
            sum += 1
    return sum 


