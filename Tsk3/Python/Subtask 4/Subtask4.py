import os
script_dir = os.path.dirname(os.path.abspath(__file__))
f2=open(os.path.join(script_dir,"output.txt"),"w")
f=open(os.path.join(script_dir,"input.txt"),"r")
n = int(f.read())
if(n%2 == 0):
    n-=1
k= (n+1)-2
for i in range(1,n+1,2):
    k-= 1
    f2.write(" "*k+"*"*i)
    f2.write("\n")
for i in range(n-2,0,-2):
    k+= 1
    f2.write(" "*k+"*"*i)
    f2.write("\n")
f2.close()