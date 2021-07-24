import graph

connections =  '''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

def test_connections():
	edgeList = graph.fromEdgeList(connections,' -> ')
	want = {
		'NY': ['Iceland','Maine'],
		'Iceland': ['London'],
		'London': ['Berlin','Egypt'],
		'Berlin': ['Paris'],
		'Maine': ['London'],
		'Paris': ['Amsterdam','London'],
		'Amsterdam': [],
		'Egypt': []
	}

	assert edgeList == want

def test_empty():
	assert graph.fromEdgeList('', ' -> ') == dict()

def test_badEdgeList():
	assert graph.fromEdgeList('foo bar baz', ' -> ') == dict()

def test_badDelimiter():
	assert graph.fromEdgeList(connections, ' => ') == dict()