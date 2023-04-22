"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.



[
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
]

"""
def possible_moves(map, row, column):
    moves = \
        [
            (r, c) for (r, c) in
            [(row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]
            if (0 <= r < len(map)) and (0 <= c < len(map[0])) and (map[r][c] == 0)
        ]
    
    return moves

def min_path_len(map):
    visited = [[False for i in range(len(map[0]))] for j in range(len(map))]
    visited[0][0] = True
    
    queue = [((0, 0), 1)]
    
    while queue:
        (row, col), moves = queue.pop(0)
        
        if (row, col) == (len(map) - 1, len(map[0]) - 1):
            return moves

        for (r, c) in possible_moves(map, row, col):
            if not visited[r][c] and map[r][c] == 0:
                visited[r][c] = True
                queue.append(((r, c), moves + 1))
   
    # Return an arbitrary large number if there is no path
    # Its better to return a large number here since we are calculating the minimum
    # so we don't want to use a small value such as -1 here in case of an
    # invalid path
    return 100

def solution(map):
    # Your code here
    path_len = min_path_len(map)
    
    # If the path_len is the same as the map size, then there is no wall to remove
    if path_len == len(map) + len(map[0]) - 1:
        return path_len

    for row in range(0, len(map)):
        for col in range(0, len(map[0])):
            if map[row][col] == 1:
                map[row][col] = 0
                path_len = min(path_len, min_path_len(map))
                map[row][col] = 1
    return path_len


##############################################################################################
map1 = \
[
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
]

map2 = \
[
    [0, 1, 1, 0], 
    [0, 0, 0, 1], 
    [1, 1, 0, 0], 
    [1, 1, 1, 0]
]

map_test = \
[
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0]
]

# print(solution(map_test))
# print(solution(map1))
# print(solution(map2))
print(min_path_len(map1))