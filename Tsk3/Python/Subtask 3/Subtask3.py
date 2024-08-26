n = int(input("Enter a val:"))

if(n%2 == 0):
    n-=1
k= (n+1)-2
for i in range(1,n+1,2):
    k-= 1
    print(" "*k,"*"*i)
for i in range(n-2,0,-2):
    k+= 1
    print(" "*k,"*"*i)