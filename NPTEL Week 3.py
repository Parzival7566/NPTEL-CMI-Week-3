#NPTEL Python week 3
"""
Inductive Statements define one or more base cases and inevitably give rise to recursion
"""
#Factorial Using Recursion
def factorial(n):
    if n==0:
        return 1
    else :
        return (n*factorial(n-1))
print(factorial(1000))

#Multiplication using recursion
def multiplication(m,n):
    if n==1:
        return m
    else:
        return(m+multiplication(m, n-1))
print(multiplication(9, 3))

#length of list using recursion
def listlen(l):
    if l==[]:
        return 0
    else:
        return(1+listlen(l[1:]))
print(listlen([3,5,3,2,5,7,6,4]))

#Binary search
def bsearch(l,v,s,e):
    #searching v in l(s:e)
    if s==e:
        print("Element not in list")
    mid=(s+e)//2
    if v==l[mid]:
        print(v,' found in list at position ',mid+1)
    elif v<l[mid]:
        bsearch(l,v,s,mid)
    else:
        bsearch(l,v,mid+1,e)

a=eval(input("Enter a list : "))
b=eval(input("Enter element to search in list : "))
list.sort(a)
print("The sorted list is : ",a)
bsearch(a,b,0,len(a))

#selection sort
def ssort(l):
    for i in range(len(l)):
        minpos=i
        for j in range(i,len(l)):
            if l[j]<l[minpos]:
                minpos=j
        (l[i],l[minpos])=(l[minpos],l[i])
    print(l)
ssort([3,6,5,8,7])


#insertion sort
def isort(l):
    for i in range (len(l)):
        pos=i
        while pos>0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos-=1
    print(l)
isort([3,6,5,8,7])


#recursive insertion sort
def InsertionSort(seq):
    isort(seq,len(seq))
    print(seq)

def isort(seq,k): 
    if k > 1:
        isort(seq,k-1)
        insert(seq,k-1)

def insert(seq,k): 
    pos = k
    while pos > 0 and seq[pos] < seq[pos-1]:
        (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
        pos = pos-1
        
InsertionSort([3,6,5,8,7])
