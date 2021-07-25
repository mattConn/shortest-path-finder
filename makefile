testRunner = python -m pytest
testFlag = -k

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
	rm -r __pycache__; rm -r graph/__pycache__; rm -r graph/tests/__pycache__