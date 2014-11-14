__author__ = 'Pranav Sharma'


def partition(A,start,end):
    i = start-1
    j = start
    pivot = A[end]
    while j < (end):
        if(A[j] < pivot):
            i += 1
            A[i],A[j] = A[j],A[i]
        j += 1
    A[i+1],A[end] = A[end],A[i+1]
    return i+1

def quicksort(A,start,end):
    if start<end:
        q = partition(A,start,end)
 #       print(q)
        quicksort(A,start,q-1)
        quicksort(A,q+1,end)

A = [12,11,4,324,12312,534,123,545,1324,123,2556]
#print A[2],len(A)
quicksort(A,0,len(A)-1)
print(A)