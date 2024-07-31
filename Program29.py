def factorial(num):
    if (num==1 or n==0):
        return 1
    else:
        fact = factorial(num-1)*num
        return fact
n = int(input("Enter a number:"))
ans=factorial(n)
print(ans)