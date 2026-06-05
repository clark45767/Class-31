#Program to find factorial of any number using recursion
def fac(t):
    #When t is 1 or 0, return 1
    if( t==1 or t==0):
        return 1
    #Factorial of n = n*n=1*n-2...1
    return t*fac(t-1)
t = int(input("Enter your number : "))
print ("Factorial of", t, "is : ",fac(t))