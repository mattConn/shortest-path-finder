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
				raise ValueError(f'At least one node in {nodes} is not in edge list')

	def allPaths(self, source, target):
		self.checkNodes((source,target))

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