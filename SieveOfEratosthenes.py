def main():
	li = [1] * 103
	for x in range(2,len(li)):
		if li[x] == 1:
			print x
			y = x * x
			while y < len(li):
				li[y] = 0
				y += x
	print li


if __name__ == '__main__':
	main()