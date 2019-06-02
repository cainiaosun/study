m=5
n=7
for i in range(1,m):
    for j in range(1,n):
        if i==1 or i==m-1 or j==1 or j==n-1:
            print '*',
        else:
            print " ",
    print '\n'
