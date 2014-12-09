from collections import defaultdict


class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		super(Graph, self).__init__()
		self.vertex = dict()
		self.edge = defaultdict(list)

	def addedge(self,e1,e2,w):
		if (not e1 in self.vertex) or (not e2 in self.vertex):
			print 'No vertex found : ' + str(e1) + ',' + str(e2)
			return
		else:
			self.edge[w].append([e1,e2])
			self.vertex[e1] += 1
			self.vertex[e2] += 1

	def addvertex(self,n,e = 0):
		self.vertex[n] = e

	def printdata(self):
		print self.vertex
		print self.edge

	def checkvertex(self,a):
		if a in self.vertex:
			print 'exists'
		else:
			print 'Nopes'

	def printvertex(self):
		for x in self.vertex:
			print x

	def printedges(self):
		for x in self.edge:
			print self.edge[x]

def main():
	g = Graph()
	g.addvertex(2)
	g.addvertex(3)
	g.addvertex(4)
	g.addvertex(5)
	g.addvertex(7)
	#g.checkvertex(2)
	g.addedge(2,3,10)
	g.addedge(3,4,10)
	g.addedge(7,4,12)
	g.printdata()
	#g.printvertex()
	g.printedges()


if __name__ == "__main__":
	main()