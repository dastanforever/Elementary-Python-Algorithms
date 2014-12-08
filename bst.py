class bstree(object):
	"""docstring for bstree"""
	def __init__(self, arg = None):
		super(bstree, self).__init__()
		self.data = arg
		self.left = None
		self.right = None

root = bstree()
temp = bstree()
		
def insert():
	print "Enter Data : "
	data = int(raw_input())
	if root.data == None:
		root.data = data
	else:
		node = bstree(data)
		temp  = root
		while temp != None:
			if temp.data > data:
				if temp.left != None:
					temp = temp.left
				else:
					temp2 = bstree()
					temp2.data = data
					temp.left = temp2
					break
			elif temp.data < data:
				if temp.right != None:
					temp = temp.right
				else:
					temp2 = bstree()
					temp2.data = data
					temp.right = temp2
					break

def inorder(temp):
	if temp == None:
		return
	else:
		inorder(temp.left)
		print temp.data
		inorder(temp.right)

def preorder(temp):
	if temp == None:
		return
	else:
		print temp.data
		preorder(temp.left)
		preorder(temp.right)

#def inordersuccessor(temp):
#	if temp == None and found == 0:
#		return
#	else:
#		inordersuccessor(temp.left)
#		found = 1
#		return temp
#		inordersuccessor(temp.right)


#def delete(temp,data):
#	if(temp.data == data):
#		return
#	elif temp.data > data:
#		if temp.left != None:
#			delete(temp.left,data)
#			temp2 = inordersuccessor(temp.left)
#			temp.left = temp2
#		else:
#			print "Not Found!!!!"
#	elif temp.data < data:
#		if temp.right != None:
#			delete(temp.right,data)
#			temp2 = inordersuccessor(temp.right)
#			temp.right = temp2
#		else:

def main():
	flag= 0
	while flag == 0:
		print "1.Enter\n2.PreOrder\n3.PostOrder\n4.InOrder\n5.Delete\n6.Exit"
		ch = int(raw_input())
		if ch == 1:
			insert()
		elif ch == 2:
			preorder()
		elif ch == 3:
			postorder()
		elif ch == 4:
			inorder(root)
		elif ch == 5:
			data = int(raw_input())
			delete(root,data)
		else:
			flag = 1



if __name__ == "__main__":
	main()