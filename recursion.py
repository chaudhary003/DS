# factorial of nth number using factorial
 def factorial(n):
     if n==0:
         return 1
    else:
        return n*factorial(n-1)
# binary search for a targeted element using recursion
 def binary_search(list,target,low,high):
     if low> high:
         return False
    else:
        mid=(low+high)//2
        if target==list[mid]:
            return True
        elif target<list[mid]:
            return binary_search(list,target,low,mid-1)
        else:
            return binary_search(list,target,mid+1,high)
# finding nth term of fibonacci series
 def fibonacci(n):
     if n<=1:
         return 1
     else:
        return fibonacci(n-2)+fibonacci(n-1)
# sum of sum of first n number of a list
def linear_sum(list,n):
    if n==0:
        return 0
    else:
        return linear_sum(list,n-1)+list[n-1]
#reverse of element in a list using recursion
def reverse(list,start,stop):
    if start<stop-1:
        list[start],list[stop-1]=list[stop-1],list[start]
        reverse(list,start+1,stop-1)
#return power using recursion
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
