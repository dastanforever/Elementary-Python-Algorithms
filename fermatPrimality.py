from random import sample

def check(a):
	s = sample(range(0,2**10),100)
	for x in s:
		if (x**(a-1) - 1) % a != 0:
			print 'Not prime!!'
			return
	print "Prime"
	return


def main():
	check(3149)

if __name__ == "__main__":
	main()