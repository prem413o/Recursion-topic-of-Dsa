#write a code to find the sum of natural number by recursion
def sum_of_natural_number(n):
    if(n==1 or n==0):
        return n
    else:
        return sum_of_natural_number(n-1) + n


n=int(input("Enter your number of terms: "))
result=sum_of_natural_number(n)
print(result)