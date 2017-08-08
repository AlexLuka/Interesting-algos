# Here I implemented a dijkstra's algorithm that finds a path through a maze.
# The entrance to a maze is always in top left corner and the exit is in bottom
# right corner. Maze may or may not have a solution.
# algorithm1 - dijkstra's algorithm, no additional conditions
#
#
#
#
#
#
import itertools


def print_maze(maze):
    for i in range(len(maze)):
        print '\t',
        for j in range(len(maze[0])):
            print '{:3d} '.format(maze[i][j]),
        print


def dijkstra_algorithm1(maze):
    h, w = len(maze), len(maze[0])

    # generate a list of unvisited nodes
    unvisited = [(i, j) for i, j in itertools.product(range(h), range(w))]

    # Create a distance map for a given maze. Assign a distance value for each node
    # equal to h*w+1 - the value that is larger that the longest possible distance.
    distance_map = [[(h*w+1) for _ in range(w)] for _ in range(h)]
    distance_map[0][0] = 0      # Entry point

    while len(unvisited) > 0:
        # current node
        cn = unvisited[0]

        # set the current node with the smallest distance among unvisited nodes
        for un in unvisited:
            if distance_map[un[0]][un[1]] < distance_map[cn[0]][cn[1]]:
                cn = un

        #
        for un in unvisited:
            # If nearest neighbour
            if abs(cn[0] - un[0]) + abs(cn[1] - un[1]) == 1:
                if maze[un[0]][un[1]] == 0:
                    distance_map[un[0]][un[1]] = distance_map[cn[0]][cn[1]] + 1

        # remove the current node, since it have been visited
        unvisited.remove(cn)

    if distance_map[h-1][w-1] > h*w:
        print 'Maze has no exit'
    else:
        print 'The length of the shortest path is {}'.format(distance_map[h-1][w-1])

    return distance_map


def test_dijkstra_algorithm1():

    print('Maze 1:')
    print_maze(dijkstra_algorithm1([[0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0]
                                    ]))

    print('Maze 2:')
    print_maze(dijkstra_algorithm1([[0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 0, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0]
                                    ]))

    print('Maze 3:')
    print_maze(dijkstra_algorithm1([[0, 0, 1, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 1, 1, 0],
                                    [1, 1, 1, 1, 1, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 1],
                                    [0, 1, 1, 1, 1, 1, 1],
                                    [0, 1, 0, 0, 0, 0, 0],
                                    [0, 1, 0, 1, 0, 1, 0],
                                    [0, 0, 0, 1, 0, 1, 0]
                                    ]))

    print('Maze 4:')
    print_maze(dijkstra_algorithm1([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ]))

    print('Maze 5:')
    print_maze(dijkstra_algorithm1([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                                    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                                    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                                    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                                    [0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                                    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                                    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
                                    ]))


if __name__ == '__main__':
    test_dijkstra_algorithm1()
