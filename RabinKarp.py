# base for roller hashbase = 109
hashbase = 109

def makerollerhash(a,hashres):	#length of string passed = m + 1
	hashres -= (hashbase ** (len(a) - 2)) * ord(a[0])
	hashres *= hashbase
	hashres += ord(a[len(a) - 1])
	return hashres

def mainhash(a):
	hashres = 0
	for x in range(0,len(a)):
		hashres += (hashbase ** x) * ord(a[len(a) - x - 1])
	return hashres

def rabinfind(a,pattern):
	phash = mainhash(pattern)
	shash = mainhash(a[0:len(pattern)])
	for x in range(0,len(a) - len(pattern) + 1):
		if phash == shash:
			if a[x:x+len(pattern)] == pattern:
				return 1
		shash = makerollerhash(a[x:x + len(pattern) + 1],shash)
	return 0
		

def main():
	#a = str(raw_input())
	#pattern = str(raw_input())
	res = rabinfind('pattern','er')
	if res == 1:
		print 'found'
	else:
		print 'notfound'

if __name__ == '__main__':
	main()