import graph

connections =  '''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

cg = graph.fromEdgeList(connections, ' -> ')

def test_hasPaths():
	want = [
		['NY', 'Iceland', 'London', 'Egypt'],
		['NY', 'Maine', 'London', 'Egypt']
	]

	assert graph.allPaths(cg,'NY','Egypt') == want

def test_noPaths():
	want = None

	assert graph.allPaths(cg,'Amsterdam','London') == want

def test_badSourceTarget():
	result = [
		# bad source
		graph.allPaths(cg,'Tokyo','Amsterdam'),
		# bad target
		graph.allPaths(cg,'NY','LA'),
		# bad source and target
		graph.allPaths(cg,'Tokyo','LA'),
	]

	want = [None] * len(result) 

	assert want == result