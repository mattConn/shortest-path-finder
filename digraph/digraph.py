# Reads edge list string with specified delimeter and returns dictionary
def makeEdgeList(edgeListString, delim=' '):
	edgeList = dict()	

	lines = edgeListString.split('\n')
	for line in lines:
		if len(line) == 0: continue

		nodes = line.split(delim)
		for i in range(len(nodes)):
			if nodes[i] not in edgeList:
				edgeList[nodes[i]] = []

			if i+1 == len(nodes): break

			edgeList[nodes[i]].append(nodes[i+1])

	return edgeList

# Directed graph
class DiGraph:
	def __init__(self, edgeListString, delim=' '):
		self.edgeList = makeEdgeList(edgeListString, delim)

	def checkNodes(self, nodes):
		for n in nodes:
			if n not in self.edgeList:
				return False 
		return True

	def allPaths(self, source, target):
		if not self.checkNodes((source,target)):
			return None

		def descend(visited, paths, path, edgeList, source, target):
			visited.add(source)
			path.append(source)
			
			if source == target:
				paths.append(path.copy())
			else:
				for n in edgeList[source]:
					if n in visited: continue
					descend(visited, paths, path, edgeList, n, target)

			path.pop()
			visited.remove(source)

		visited = set()
		path = []
		paths = []

		descend(visited, paths, path, self.edgeList, source, target)
		
		return paths or None

	def shortestPaths(self, source, target):
		paths = self.allPaths(source, target)

		if paths == None: return None

		paths.sort(key = len)

		minLengths = filter(lambda x: len(x) == len(paths[0]), paths)

		return [path for path in minLengths]
