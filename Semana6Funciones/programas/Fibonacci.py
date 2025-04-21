def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

'''
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
'''

def esPrimo(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return False
    return True

