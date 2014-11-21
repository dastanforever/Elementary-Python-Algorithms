import heapsort
#def getparent(i):
	#return (int((bin(i)[2:-1]),2))

def maximum(li):
	return li[0]

def extractmax(li,hsize):
	li[0],li[hsize-1] =  li[hsize-1],li[0]
	hsize -= 1
	return hsize,li[hsize + 1]

def increasekey(li,key,index):
	if(li[index] > key):
		print "Error!!!!"
	else:
		li[index] = key
		while index > -1:
			#print heapsort.getparent(index)
			if li[heapsort.getparent(index)] < li[index]:
				#print index
				li[index],li[heapsort.getparent(index)] = li[heapsort.getparent(index)],li[index]
			index = heapsort.getparent(index)

def insert(li,key):
	li.append(0)
	increasekey(li,key,len(li)-1)

def main():
	lis = []
	insert(lis,18)
	insert(lis,21)
	insert(lis,2)
	insert(lis,1)
	insert(lis,12)
	#heapsort.buildheap(lis,len(lis)-1)
	#heapsize = len(lis)
	#i = heapsize
	#while i > 1:
		#lis[heapsize-1],lis[0] = lis[0],lis[heapsize-1]
		#i -= 1
		#heapsize -= 1
		#heapsort.heapit(lis,0,heapsize)
	print lis


if __name__ == '__main__':
	main()