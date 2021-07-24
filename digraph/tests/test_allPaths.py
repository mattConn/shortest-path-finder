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