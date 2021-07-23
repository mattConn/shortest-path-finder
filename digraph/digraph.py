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

# depth-first search
def dfs(edgeList, visited, source, target):
	if len(visited) == len(edgeList):
		return False

	result = False

	for n in edgeList[source]:
		if n in visited:
			continue

		if n == target:
			return True

		visited.add(n)

		result = dfs(edgeList, visited, n, target)
		if result == True:
			break

	return result


# Directed graph
class DiGraph:
	def __init__(self, edgeListString, delim=' '):
		self.edgeList = makeEdgeList(edgeListString, delim)


	def hasPath(self, source, target):
		if source not in self.edgeList or target not in self.edgeList:
			return False
		visited = set()

		return dfs(self.edgeList, visited, source, target)

