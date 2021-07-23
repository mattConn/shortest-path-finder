import digraph as dg

connections =  '''
NY -> Iceland -> London -> Berlin
NY -> Maine -> London
Berlin -> Paris -> Amsterdam
Paris -> London -> Egypt
'''

g = dg.DiGraph(connections, ' -> ')

def test_path():
	result = [] 

	sourceTarget = [
		('NY','Egypt'),
		('NY','Berlin'),
		('London','Amsterdam'),
		('Berlin','Amsterdam'),
	]

	for s in sourceTarget:
		source, target = s
		result.append(g.hasPath(source, target))

	assert result == [True] * len(sourceTarget)

def test_noPath():
	result = [] 

	sourceTarget = [
		('Amsterdam','London'),
		('Berlin','Iceland'),
		('Maine','Iceland'),
		('London','Maine'),
	]

	for s in sourceTarget:
		source, target = s
		result.append(g.hasPath(source, target))

	assert result == [False] * len(sourceTarget)

def test_badSourceTarget():
	result = [] 

	sourceTarget = [
		('Tokyo','London'), # bad source
		('Amsterdam','LA'), # bad target
		('Tokyo','LA'), # bad source and target
	]

	for s in sourceTarget:
		source, target = s
		result.append(g.hasPath(source, target))

	assert result == [False] * len(sourceTarget)