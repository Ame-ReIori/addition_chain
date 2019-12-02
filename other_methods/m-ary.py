
def ac(k,n):
    chain = [0]*100000
    kk = 2**k
    for i in range(0,kk-1):
        chain.append(i+1)
    ns = bin(n)[2:]
    
    length = len(ns)
    pad = (k-(length%k))%k
    padding = "0"*pad
    ns = padding + ns
    w = len(ns)//k
    m = [0]*w
    for i in range(0,w):
        m[w-1-i] = int(ns[k*i:k*(i+1)],2)
    r = kk - 2
    chain[r] = m[w-1]
    s = [0]*kk
    for i in range(w-2,-1,-1):
        z=m[i]
        count=0
        while(z!=0):
            if(z%2==1):
                break
            z//=2
            count+=1
        
        for j in range(0,k-count):
            r=r+1
            chain[r] = chain[r-1]*2
            
        if(m[i]!=0):
            r=r+1
            chain[r]=chain[r-1]+z
            s[z]=1
        
        for j in range(0,count):
            r=r+1
            chain[r] = chain[r-1]*2
    
    chain = list(set(chain))
    chain.sort()
    chain = chain[1:]
    length = len(chain)-1
    #print(length,chain)
    return length,chain

if __name__ == "__main__":
    length,chain = ac(3,15)
    print(length)
    print(chain)