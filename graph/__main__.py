import sys

def main(args):
	if len(args) == 0:
		print('Missing arguments.')
		return

	if '-f' not in args:
		print('Specify a graph file with -f flag.')
		return

main(sys.argv[1:])