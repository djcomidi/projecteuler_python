#!/usr/bin/env python

from AStar import a_star

matrix = []
with open('Problem081_matrix.txt') as in_file:
	for line in in_file.readlines():
		matrix.append( map( int, line[:-1].split(',') ) )
ROWS, COLS = len(matrix), len(matrix[0])

graph = a_star(matrix)
graph.set_directions(goLeft=False,goUp=False)
print graph.shortest_path()
# ~4s
