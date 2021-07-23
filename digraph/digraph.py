# Reads edge list string with specified delimeter and returns dictionary
def makeEdgeList(edgeListString, delim=' '):
	edgeList = dict()	

	lines = edgeListString.split('\n')
	for line in lines:
		nodes = line.split(delim)
		for i in range(len(nodes)):
			if nodes[i] not in edgeList:
				edgeList[nodes[i]] = []

			if i+1 == len(nodes): break

			edgeList[nodes[i]].append(nodes[i+1])

	return edgeList

# Directed graph
class DiGraph:

	def __init__(edgeListString, delim=' '):
		edgeList = makeEdgeList(edgeListString, delim)