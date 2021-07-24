import graph as g

connections =  '''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

cg = g.Graph(connections, ' -> ')

def test_hasPaths():
	want = [
		['NY', 'Iceland', 'London', 'Egypt'],
		['NY', 'Maine', 'London', 'Egypt']
	]

	assert cg.allPaths('NY','Egypt') == want

def test_noPaths():
	want = None

	assert cg.allPaths('Amsterdam','London') == want

def test_badSourceTarget():
	result = [
		# bad source
		cg.allPaths('Tokyo','Amsterdam'),
		# bad target
		cg.allPaths('NY','LA'),
		# bad source and target
		cg.allPaths('Tokyo','LA'),
	]

	want = [None] * len(result) 

	assert want == result