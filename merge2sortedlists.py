def merge(A,p,q,r):
	B = []
	a = p
	b = q
	c = r - p + 1
	for x in range(c):
		if A[a] < A[b]:
			B.append(A[a])
			a += 1
			if a == q:
				break
		else:
			B.append(A[b])
			b += 1
			if b == c - 1:
				break
	if b < c:
		while b != c - 1:
			B.append(A[b])
			b += 1
	if a < c:
		while a != q:
			B.append(A[a])
			a += 1
	return B

def mergesort(A,p,r):
	if p < r:
		q = ((p + r)//2)
		mergesort(A,p,q)
		mergesort(A,q+1,r)
		A = merge(A,p,q,r)
	if p == 0 and r == 9:
		print A
	

def main():
	a = [3,4,5,6,7,1,2,8,9,10]
	print mergesort(a,0,len(a)-1)
	print a

if __name__ == '__main__':
	main()
