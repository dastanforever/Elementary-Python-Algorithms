def gcd(a,b):
	if b == 0:
		return a * 1;
	else:
		return gcd(b,a%b)

def checklc(a,b,c):
	if c%gcd(a,b) == 0:
		return True
	else:
		return False

def coefflinear(a,b,c):
	cura = 0
	curb = 0
	stepa = 0
	stepb = 0
	while cura != c and curb != c:
		if curb == 0:
			curb = b
			stepb += 1
			print '(' +str(cura) + ', ' + str(curb) +')'
		if curb + cura <= a and cura != c and curb != c:
			cura += curb
			stepa += 1
			curb = 0
			stepb += 1
			print '(' +str(cura) + ', ' + str(curb) +')'
		if curb + cura > a and cura != c and curb != c:
			temp = a-cura
			cura = a
			stepa += 1
			curb = curb - (temp)
			stepb += 1
			print '(' +str(cura) + ', ' + str(curb) +')'
		if cura == a and cura != c and curb != c:
			cura = 0
			stepa += 1
			print '(' +str(cura) + ', ' + str(curb) +')'
	return stepa,stepb
			


print 'Steps required - ' + str(coefflinear(5,3,5))