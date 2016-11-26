numCalls = 0
def fib(n): # fibbonacci without memoisation
    global numCalls
    numCalls += 1
    print ('fib called with', n)
    if n <= 1: return n
    else: return fib(n-1) + fib(n-2)


def fib1(n): # fibbonacci with memoisation
    memo = {0:0, 1:1}
    return fastFib(n, memo)

 
def fastFib(n, memo):
    global numCalls
    numCalls += 1
    print ('fib1 called with', n)
    if not n in memo:
            memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]


a = [1,3,2,4,5]
b = [1,5,2,0,6]
c = list(map(min,a,b))
print (c)


