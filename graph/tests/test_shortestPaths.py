import graph

connections =  '''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

simpleGraphString = '''
A -> B
A -> C

B -> C
B -> D

C -> D
C -> E

D -> E
'''

cycleGraphString = '''
A -> B
B -> C
C -> D
D -> E
E -> A
'''

cg = graph.fromEdgeList(connections, ' -> ')
simple = graph.fromEdgeList(simpleGraphString, ' -> ')
cycle = graph.fromEdgeList(cycleGraphString, ' -> ')

def test_hasPaths():
	want = [
		['NY', 'Iceland', 'London', 'Egypt'],
		['NY', 'Maine', 'London', 'Egypt']
	]

	paths = graph.allPaths(cg,'NY','Egypt')
	assert graph.shortestPaths(paths) == want

def test_noPaths():
	want = None

	paths = graph.allPaths(cg,'Amsterdam','London')
	assert graph.shortestPaths(paths) == want

def test_morePaths():
	want = [
		# A to E
		[['A','C','E']],

		# A to D
		[
			['A','B','D'],
			['A','C','D']
		]
	]

	paths = [
		graph.allPaths(simple,'A','E'),
		graph.allPaths(simple,'A','D')
	]

	assert [graph.shortestPaths(path) for path in paths] == want


def test_cycleString():
	want = [
		['B','C','D','E']
	]

	paths = graph.allPaths(cycle,'B','E')
	assert graph.shortestPaths(paths) == want

def test_badSourceTarget():
	paths = [
		# bad source
		graph.allPaths(cg,'Tokyo','Amsterdam'),
		# bad target
		graph.allPaths(cg,'NY','LA'),
		# bad source and target
		graph.allPaths(cg,'Tokyo','LA'),
	]

	want = [None] * len(paths) 

	assert [graph.shortestPaths(path) for path in paths] == want

def test_noPathsLiteral():
	assert graph.shortestPaths(None) == None

def test_emptyPathsLiteral():
	assert graph.shortestPaths([]) == [] 

def test_allPathsEqualLen():
	paths = [
		['a','b','c'],
		['d','e','f'],
		['g','h','i']
	]

	assert graph.shortestPaths(paths) == paths 