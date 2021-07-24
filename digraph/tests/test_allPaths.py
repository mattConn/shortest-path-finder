import digraph as dg

connections =  '''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

g = dg.DiGraph(connections, ' -> ')

def test_hasPaths():
	want = [
		['NY', 'Iceland', 'London', 'Egypt'],
		['NY', 'Maine', 'London', 'Egypt']
	]

	assert g.allPaths('NY','Egypt') == want

def test_noPaths():
	want = None

	assert g.allPaths('Amsterdam','London') == want

def test_badSourceTarget():
	result = [
		# bad source
		g.allPaths('Tokyo','Amsterdam'),
		# bad target
		g.allPaths('NY','LA'),
		# bad source and target
		g.allPaths('Tokyo','LA'),
	]

	want = [None] * len(result) 

	assert want == result