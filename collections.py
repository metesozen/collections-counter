# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
if __name__ == '__main__':
    x = int(input())
    sizes = input().split()
    sizes = list(map(int, sizes)) 
    n=int(input())
    attemptedsize=[]
    xi=[]
    for i in range(n):
        line=input().split()
        size,xi1=int(line[0]),int(line[1])
        attemptedsize.append(size)
        xi.append(xi1)
    sizelist=list(Counter(attemptedsize).keys())
    sizerepeatlist=list(Counter(attemptedsize).values())
    currentlist=list(Counter(sizes).keys())
    currentrepeats=list(Counter(sizes).values())
    #print(sizes)
    print(attemptedsize)
    print(xi)
    print(sizelist)
    print (sizerepeatlist)
    print(currentlist)
    print(currentrepeats)
    total=0.0
    for i in range(len(currentlist)):
        for j in range(len(sizelist)):
            if (currentlist[i]==sizelist[j]):
                if(currentrepeats[j]!=0):
                    total+=xi[j]
                    currentrepeats[j]-=1
    print(currentrepeats)
    print(total)
