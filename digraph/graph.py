# Reads edge list string with specified delimeter and returns dictionary
def fromEdgeList(edgeList, delim=' '):
	graph = dict()	

	lines = edgeList.split('\n')
	for line in lines:
		if len(line) == 0: continue

		nodes = line.split(delim)
		for i in range(len(nodes)):
			if nodes[i] not in graph:
				graph[nodes[i]] = []

			if i+1 == len(nodes): break

			graph[nodes[i]].append(nodes[i+1])

	return graph 

def allPaths(graph, source, target):
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

	descend(visited, paths, path, graph.edgeList, source, target)
	
	return paths or None

def shortestPaths(graph, source, target):
	paths = graph.allPaths(source, target)

	if paths == None: return None

	paths.sort(key = len)

	minLengths = filter(lambda x: len(x) == len(paths[0]), paths)

	return [path for path in minLengths]
