#write a code to find factorial of a number
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return factorial(n-1)*n

n=int(input("Enter your number: "))
result=factorial(n)
print(result)