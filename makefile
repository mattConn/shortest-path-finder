testRunner = python -m pytest
testFlag = -k
cacheDirs = graph graph/tests

# test graph construction
tgraph:
	$(testRunner) $(testFlag) fromEdgeList

# test finding of all paths
paths:
	$(testRunner) $(testFlag) allPaths 

# test finding shortest path 
shortest:
	$(testRunner) $(testFlag) shortestPaths 

# run all tests
test: tgraph paths shortest

# clear pycache
cache:
	for dir in $(cacheDirs); do rm -r $$dir/__pycache__; done