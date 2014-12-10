class avlnode(object):
	"""docstring for avlnode"""
	def __init__(self, arg = None):
		super(avlnode, self).__init__()
		self.left = None
		self.right = None
		self.data = arg
		self.height = 0

class avltree(object):
	"""docstring for avltree"""
	def __init__(self, arg = None):
		super(avltree, self).__init__()
		self.root = None
		

def setheight(node):
	if node.left != None and node.right != None:
		node.height = max(node.left.height,node.right.height) + 1
	elif node.left == None and node.right == None:
		node.height = 0
	elif node.left != None and node.right == None:
		node.height = node.left.height + 1
	else:
		node.height = node.right.height + 1

def bfaccal(node):
	if node.left != None and node.right != None:
		return (node.left.height - node.right.height)
	elif node.left == None and node.right == None:
		return 0
	elif node.left != None and node.right == None:
		return (node.left.height +1)
	else:
		return (-1 + (-1)*node.right.height)


def llcase(node):
	a = node.left
	print "rotation data Main node ll- " + str(node.data)
	if node.left.right != None:
		node.left,node.left.right = node.left.right,node
	else:
		node.left.right,node.left = node,None
	return a

def lrcase(node):
	a = node.left.right
	print "rotation data Main node lr-" + str(node.data)
	if node.left.right.left != None:
		node.left,node.left.right = node.left.right,node.left.right.left
	else:
		node.left,node.left.right = node.left.right,None
	llcase(node)
	return a

def rrcase(node):
	a = node.right
	print "rotation data Main node rr- " + str(node.data)
	if node.right.left != None:
		node.left,node.right.left = node.right.left,node
	else:
		node.left,node.right.left = None,node
	return a

def rlcase(node):
	a = node.right.left
	print "rotation data Main node rl- " + str(node.data)
	if node.right.left.right != None:
		node.right.left,node.right = node.right.left.right,node.right.left
	else:
		node.right.left,node.right = None,node.right.left
	rrcase(node)
	return a

def lcase(node,data):
	if data < node.left.data:
		return llcase(node)
	else:
		return lrcase(node)

def rcase(node,data):
	if(data < node.right.data):
		return rlcase(node)
	else:
		return rrcase(node)

def inorderheight(root):
	if root == None:
		return
	else:	
		inorderheight(root.left)
		print str(root.data) + "-" + str(root.height)
		inorderheight(root.right)

def newnode(data):
	node = avlnode(data)
	return node

def makeavl(node,data):
	if bfaccal(node) >= -1 and bfaccal(node) <= 1:
		print "bf" + str(node.data) + "-" + str(bfaccal(node))
		return node
	elif bfaccal(node) > 1:
		print "bf" + str(node.data) + "-" + str(bfaccal(node))
		return lcase(node,data)
	else:
		print "bf" + str(node.data) + "-" + str(bfaccal(node))
		return rcase(node,data)

def insert(node,data):
	if node == None:
		return newnode(data)
	elif node.data > data:
		if node.left == None:
			node.left = insert(node.left,data)
			setheight(node)
			#inorderheight(node)
			node = makeavl(node,data)
		else:
			insert(node.left,data)
			setheight(node)
			#inorderheight(node)
			node = makeavl(node,data)
	elif node.data < data:
		if node.right == None:
			node.right = insert(node.right,data)
			setheight(node)
			#inorderheight(node)
			node = makeavl(node,data)
		else:
			insert(node.right,data)
			setheight(node)
			#inorderheight(node)
			node = makeavl(node,data)


def inorder(root):
	if root == None:
		return
	else:
		inorder(root.left)
		print root.data
		inorder(root.right)

def preorder(root):
	if root == None:
		return
	else:
		print root.data
		preorder(root.left)
		preorder(root.right)

def main():
	tree = avltree()
	flag = 1
	while flag == 1:
		print "\n1.Insert\n2.Inorder\n3.Preorder\n4.Inorder height\n5.Exit"
		c = int(raw_input())
		if c == 1:
			print "Enter data : "
			d = int(raw_input())
			if tree.root == None:
				tree.root = insert(tree.root,d)
			else:
				insert(tree.root,d)
		elif c == 2:
			print "Inorder"
			inorder(tree.root)
		elif c == 3:
			print "Preorder\m"
			preorder(tree.root)
		elif c == 4:
			print 'Height'
			inorderheight(tree.root)
		elif c == 5:
			flag = 0

if __name__ == "__main__":
	main()