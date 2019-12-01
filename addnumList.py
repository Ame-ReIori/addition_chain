
def getAddnumList(n,addnumBound):
    
    addnumList = []
    ns = bin(n)[2:]
    ones = ns.split('0')
    oneMax = 0
    for one in ones:
        if(len(one)>oneMax):
            oneMax = len(one)
    if(oneMax > (len(ns)//2)):
        oneMax = len(ns)//2
    addnumMax = 2 ** oneMax
    
    if(addnumMax > addnumBound):
        addnumMax = addnumBound
    
    for addnum in range(1,addnumMax,2):
        addnumList.append(addnum)
        
    return addnumList

def getAddnumOddList(addnumBound):
    addnumList = []
    for addnum in range(1,addnumBound,2):
        addnumList.append(addnum)
    return addnumList

if __name__ == "__main__":
    print(getAddnumList(2**9 - 1,2**10))
    print(getAddnumList(2**100 - 1,2**10))
    
    
    print(getAddnumOddList(2**10))