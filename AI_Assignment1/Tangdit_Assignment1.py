#My github id is: ntangdit
class Stack:
	size=0
	capacity= 20
	data = [20]
	def __init__(self):
		self.data= [] 
	def push(self, integer):
		if self.size >= self.capacity:
			self.capacity *=2
			nwArray = [self.capacity]
			for i in self.data:
				nwArray[i]=self.data[i]
			del self.data[:]
			self.data=nwArray
		self.data.append(integer)
		self.size+= +1
	def pop(self):
		#x= get(self.data[self.size])
		self.size = self.size - 1
		return self.data.pop(self.size)
	def checksize(self):
		return self.size

class Binary_Tree:
	class Node:
		integerKey=0
		left, right, parent= 0,0,0
	root= Node()
	def find(self, current, value):
		result= 0
		if current.left != 0:
			result = self.find(self, current.left, value)
		elif current.integerKey is value:
			return current
		elif result == 0 and current.right != 0:
			result = find(self, current.right,value)
		return result
	def add(self, value, parentValue):
		found= self.find(self, self.root, parentValue)
		if found:
			if not found.left:
				found.left=self.Node()
				found.left.integerKey=value
				found.left.parent=found
				return
			elif not found.right:
				found.right= self.Node()
				found.right.integerKey= value
				found.right.parent=found
				return
			else:
				print "Parent has two children, node not added"
		elif not found:
			print "Parent not found"
	def delete(self, value):
		found= self.find(self, self.root, value)
		if found:
			if found.left or found.right:
				print "Node not deleted, has children"
			else:
				found.parent= 0
				del found
		else:
			print "Node not found"
	def print1(self):
		if not root:
			return
		print self.root
		self.print1(self.left)
		self.print1(self.right)

class Graph:
	gls={}
	def __init__(self):
		gls= {}
	def addVertex(self,value):
		exist= self.gls.get(value)
		if not exist:
			self.gls[value]=None
		else:
			print "Vertex already exists"

	def addEdge(self,value1,value2):
		ex1= value1 in self.gls
		ex2= value2 in self.gls
		hatePythonSyntax= ex1 and ex2
		#print value1, value2, ex1, ex2, hatePythonSyntax
		if not hatePythonSyntax:
			print "One or more vertices not found."
		else :
			self.gls[value1]=value2
			self.gls[value2]=value1
	
	def findVertex(self,value):
		ex= self.gls.get(value)
		if ex:
			print self.gls[value]
		else: 
			print "Could not find vertex."
			
