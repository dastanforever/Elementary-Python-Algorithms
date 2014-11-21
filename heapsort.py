def getparent(i):
	return i//2
	#return (int((bin(i)[2:-1]),2))

def getleft(i):
	return (int((bin(i)[2:] + '0'),2) + 1)
	#return 2*i + 1

def getright(i):
	return (int(bin(i)[2:] + '1',2) + 1)
	#return 2*i + 2

def heapit(li,i,hsize):
	#print 1
	left = getleft(i)
	#print left
	right = getright(i)
	#print right
	largest = i
	if left < hsize and li[left] > li[i]:
		largest = left
	if right < hsize and li[right] > li[largest]:
		largest = right
	if largest != i:
		li[i],li[largest] = li[largest],li[i]
		#print largest
		heapit(li,largest,hsize)


def buildheap(li,hsize):
	i = hsize
	while i > -1:
		heapit(li,i,hsize)
		i -= 1

def main():
	li = [4,1,3,2,16,9,10,14,8,7]
	heapsize = len(li)

	#print heapsize
	
	i = heapsize;
	buildheap(li,heapsize)
	while i > 1:
		li[heapsize-1],li[0] = li[0],li[heapsize-1]
		i -= 1
		heapsize -= 1
		heapit(li,0,heapsize)
	print li

if(__name__ == '__main__'):
	main()