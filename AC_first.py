#coding=gbk
import math

MAX=10000
l=0
ll=0
lll=999999

t=0
tl=0
a=[0]*MAX
aa=[0]*MAX
addnumBound = 2 ** 10

def dfs(cur,n) :
    global  deep,annum,ani,anj,ok
    if (cur == deep) :
        if (annum[cur] == n) :
            ok = 1
        return
    
    for i in range( cur,-1,-1) :
        if (annum[cur] + annum[i] <= n) :
            sum = annum[i] + annum[cur]
            for k in range (cur + 1,deep):
                sum *= 2
            if (sum < n) :
                continue
            annum[cur + 1] = annum[i] + annum[cur]
            ani[cur + 1] = i
            anj[cur + 1] = cur
            dfs(cur + 1,n)
            if (ok):
                return
def search(n) :
    global  deep,annum,ani,anj,ok
    N=10000
    deep = 0
    ani = [0]*N
    anj = [0]*N
    annum = [0]*N
    annum[0] = 1
    ok = 0
    n1 = n 
    count1 = 0
    deep = 5
    while (n1 != 0) :
        if (n1 % 2 == 1) :
            count1=count1+1
        n1 = n1>>1
    deep = math.ceil(math.floor(math.log(n,2)) + math.log(count1,2) - 2.13)
    while (1) :
        #print(deep)
        dfs(0,n)
        if (ok) :
            break
        deep=deep+1
    return annum[0:deep+1]

def ac(n):
    lll = 999999
    aa = []
    ns = bin(n)[2:]
    ones = ns.split('0')
    oneMax = 0
    for one in ones:
        if(len(one)>oneMax):
            oneMax = len(one)
    if(oneMax > (len(ns)//2)):
        oneMax = len(ns)//2
    addnumMax = 2 ** oneMax
    
    for addnum in range(1,addnumMax,2):
        addnumStr = bin(addnum)[2:]
        if(ns.count(addnumStr)>=1):
            length,chain = acWithAddnum(n,addnum)
            if(length<lll):
                lll = length
                aa = chain
    return lll,aa

def acWithAddnum(n,addnum):
    pre(n,addnum)
    main(n)
    branch(n,addnum)
    return lll,aa[0:lll+1]
    
def pre(n,addnum):
    global l,ll,lll,a,aa,t,tl
    a=[0]*MAX
    aa=[0]*MAX
    a[0]=1
    l=0
    ll=0
    lll=999999
    
    if(n<addnum):
        lll=MAX
        aa[0]=1
        return
    
    while(1):
        a[l + 1]=a[l]+a[l]
        if(a[l+1]>=addnum):
            break
        l+=1
    t=a[l+1]
    
    if(addnum>addnumBound):
        length,chain = ac(addnum)
        l=length
        a[0:l]=chain
        tl=l
        return
    
    arr=a[0:l+1]
    arr1=search(addnum)
    for item in arr1:
        arr.append(item)
    arr=list(set(arr))
    arr.sort()
    a[0:len(arr)]=arr
    l=len(arr)-1
    tl=l
    return

def main(n):
    global l,ll,lll,a,aa,t,tl
    if(t<n):
        a[l+1]=t
        l+=1
        while(1):
            a[l + 1]=a[l]+a[l]
            if(a[l+1]>=n):
                break
            l+=1
    for i in range(l-1,-1,-1):
        a[l+1]=a[l]+a[i]
        if(a[l+1]<=n):
            l+=1
    lll=l
    aa[0:lll+1]=a[0:lll+1]
    return

def branch(n,addnum):
    global l,ll,lll,a,aa
    
    if(t<n):
        l=tl
        a[l+1]=t
        l+=1
        while(1):
            ll=l+1
            a[ll]=a[l]+addnum
            while(1):
                a[ll + 1]=a[ll]+a[ll]
                if(a[ll+1]>=n):
                    break
                ll+=1
            if(a[ll+1]==n and (ll+1)<lll):
                lll=ll+1
                for i in range(0,lll+1):
                    aa[i]=a[i]
            for i in range(ll-1,-1,-1):
                a[ll+1]=a[ll]+a[i]
                if(a[ll+1]<n):
                    ll+=1
                if(a[ll+1]==n and (ll+1)<lll):
                    lll=ll+1
                    for i in range(0,lll+1):
                        aa[i]=a[i]
                    break
            a[l+1]=a[l]*2
            l+=1
            a[l + 1]=a[l]+a[l]
            if(a[l+1]>=n):
                break
        if(a[l+1]==n and (l+1)<lll):
            lll=l+1
            for i in range(0,lll+1):
                aa[i]=a[i]
        
    return
    
def acprint(length,chain):
    print("链长为",length)
    for i in range(0,len(chain)):
        print(chain[i]," ",end="")
    print("")
    return

if __name__ == "__main__":
    n=int(input())
    length,chain=ac(n)
    acprint(length, chain)
    
    
