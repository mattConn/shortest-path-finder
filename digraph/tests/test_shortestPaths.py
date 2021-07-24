import digraph as dg

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

g = dg.DiGraph(connections, ' -> ')
simple = dg.DiGraph(simpleGraphString, ' -> ')
cycle = dg.DiGraph(cycleGraphString, ' -> ')

def test_hasPaths():
	want = [
		['NY', 'Iceland', 'London', 'Egypt'],
		['NY', 'Maine', 'London', 'Egypt']
	]

	assert g.shortestPaths('NY','Egypt') == want

def test_noPaths():
	want = None

	assert g.shortestPaths('Amsterdam','London') == want

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

	pathCollections = [
		simple.shortestPaths('A','E'),
		simple.shortestPaths('A','D')
	]

	assert pathCollections == want

def test_cycleString():
	want = [
		['B','C','D','E']
	]

	assert cycle.shortestPaths('B','E') == want

def test_badSourceTarget():
	result = [
		# bad source
		g.shortestPaths('Tokyo','Amsterdam'),
		# bad target
		g.shortestPaths('NY','LA'),
		# bad source and target
		g.shortestPaths('Tokyo','LA'),
	]

	want = [None] * len(result) 

	assert want == result