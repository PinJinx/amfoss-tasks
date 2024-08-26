import os
script_dir = os.path.dirname(os.path.abspath(__file__))
f2=open(os.path.join(script_dir,"output.txt"),"w")
f=open(os.path.join(script_dir,"input.txt"),"r")
s = f.read()
f2.write(s)
f2.close