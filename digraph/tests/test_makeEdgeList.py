import digraph as dg

connections =  '''NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt'''

def test_connections():
	edgeList = dg.makeEdgeList(connections,' -> ')
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