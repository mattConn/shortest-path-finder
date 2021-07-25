# Shortest Path Finder

Dictionary-based graph functions for finding paths. For Axoni test.

## Running
To test using pytest:
- all functions, run `make test`
- graph construction from edge list string, run `make tgraph`
- finding all paths between two nodes, run `make paths`
- finding shortest paths between two nodes, run `make shortest`

To remove all instances of `__pycache__`, run `make cache`.

## Graph Module Functions 
### fromEdgeList
Reads edge list string and returns graph dictionary. If edge delimeter is not present in all lines of string, `fromEdgeList` returns an empty dictionary.

### allPaths
Returns all paths from `source` to `target` in specified graph, in the form of a list of lists. If `source` and or `target` are not in graph, returns `None`. If there are no paths from `source` to `target` in graph, returns `None`.

### shortestPaths
Returns shortests paths in `paths` in the form of a list of lists. If `paths` equals `None`, returns `None`. This function does not depend on `allPaths` or any graph dictionary.