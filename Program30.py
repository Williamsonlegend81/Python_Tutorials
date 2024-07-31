def Fibonacci(n):
    if (n==1 or n==2):
        if(n==1):
            return 0
        else:
            return 1
    else:
        FibNm1 = Fibonacci(n-1)
        FibNm2 = Fibonacci(n-2)
        FibN = FibNm1 + FibNm2
        return FibN

h = int(input("Enter a number:"))
for i in range(1,h):
    ans = Fibonacci(i)
    print(ans,end=", ")