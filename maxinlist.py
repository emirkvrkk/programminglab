mylist=[4,-3,2,5,-4,1,4,6,-7]
mylist2=[2,-5,4,-7,5,3,4,12]
sums=[]
def maxinlist(alist):
    for i in range(0,len(alist)):
        for j in range(len(alist),0,-1):
            sums.append(sum(alist[i:j]))
    return(max(sums))
print(maxinlist(mylist))
print(maxinlist(mylist2)) 


