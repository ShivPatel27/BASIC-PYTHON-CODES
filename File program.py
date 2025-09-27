f=open("input.txt","r")
n=int(f.readline(10))
p=float(f.readline(1.5))
m=69
for i in range(m):
    n=n+p
f.close()
f1=open("output.txt","w")
f1.write(str(n))


