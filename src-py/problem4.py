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
    if len(maze[0][0]) == 1:
        for i in range(len(maze)):
            print '\t',
            for j in range(len(maze[0])):
                print '{:3d} '.format(maze[i][j]),
            print

    elif len(maze[0][0]) == 2:
        for i in range(len(maze)):
            print '\t',
            for j in range(len(maze[0])):
                print '({:3d}, {:3d})'.format(maze[i][j][0], maze[i][j][1]),
            print

"""
    Algorithm 1. Standard algorithm with no additional conditions
"""


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


"""
    Algorithm 2:
    Dijkstra algorithm with additional condition: we can remove one wall on the path
"""


def dijkstra_algorithm2(maze):
    # maze's size
    h, w = len(maze), len(maze[0])

    # list of unvisited nodes
    unvisited = [(i, j) for i, j in itertools.product(range(h), range(w))]

    # assign the maximum distance equal to h*w+1
    distance_map = [[[h * w + 1, h * w + 1] for _ in range(w)] for _ in range(h)]
    distance_map[0][0] = [0, 0]         # entry point

    # print_maze(distance_map)

    # iterate over the number of wall removals
    # k = 0 => cannot remove a wall
    # k = 1 => can remove one wall
    for k in range(2):
        unvisited_copy = list(unvisited)

        while len(unvisited_copy) > 0:
            # pick the current node
            cn = unvisited_copy[0]

            # our choice is not optimal, therefore
            # let's find the more appropriate current node
            for un in unvisited_copy:
                if distance_map[un[0]][un[1]][k] < distance_map[cn[0]][cn[1]][k]:
                    cn = un

            # now update the distances for nearest neighbours
            # of current node
            for un in unvisited_copy:
                # check if nearest neighbour (distance = 1)
                if abs(cn[0] - un[0]) + abs(cn[1] - un[1]) == 1:
                    # if we cannot remove walls
                    # let's find the path without wall removal
                    if k == 0:
                        # if path
                        if maze[un[0]][un[1]] == 0:
                            # if the shortest path to a neighbour is greater
                            # than the possible path from the current node
                            if distance_map[un[0]][un[1]][0] > distance_map[cn[0]][cn[1]][0] + 1:
                                # update both w/out and with wall removal distances
                                distance_map[un[0]][un[1]][0] = distance_map[cn[0]][cn[1]][0] + 1
                                distance_map[un[0]][un[1]][1] = distance_map[cn[0]][cn[1]][1] + 1
                    # if we can break one wall
                    else:
                        # if path
                        if maze[un[0]][un[1]] == 0:
                            if distance_map[un[0]][un[1]][1] > distance_map[cn[0]][cn[1]][1] + 1:
                                distance_map[un[0]][un[1]][1] = distance_map[cn[0]][cn[1]][1] + 1
                        # if there is a wall
                        else:
                            # if we haven't broken a wall yet
                            if distance_map[cn[0]][cn[1]][0] < h * w + 1:
                                # take the shortest path without breaking a wall and break the first wall
                                distance_map[un[0]][un[1]][1] = distance_map[cn[0]][cn[1]][0] + 1

            # now current node is visited and we can remove it from the unvisited list
            unvisited_copy.remove(cn)

    if distance_map[h-1][w-1][-1] > h*w:
        print 'Maze has no exit'
    else:
        print 'The length of the shortest path is {}'.format(distance_map[h-1][w-1][-1])

    return distance_map


def test_dijkstra_algorithm2():

    print('Maze 1: ')
    print_maze(dijkstra_algorithm2([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

    #
    print('Maze 2: ')


if __name__ == '__main__':
    # test_dijkstra_algorithm1()

    test_dijkstra_algorithm2()
