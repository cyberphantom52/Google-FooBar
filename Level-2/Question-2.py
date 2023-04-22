"""
Don't Get Volunteered!
======================
As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!
To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
"""
def solution(src, dest):
    # Your code here
    if src == dest:
        return 0
    
    visited = [False] * 64
    visited[src] = True
    
    queue = [(src, 0)]
    
    while queue:
        pos, moves = queue.pop(0)
        
        if pos == dest:
            return moves
        
        for move in possible_moves(pos):
            if not visited[move]:
                visited[move] = True
                queue.append((move, moves + 1))
   
    return -1

def possible_moves(pos):
    # Convert pos to row and column
    row, column = pos // 8, pos % 8
    
    moves = \
        [
            pos + 8 * x + y for (x, y) in
            [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
            if 0 <= row + x < 8 and 0 <= column + y < 8
        ]
    
    return moves

print(solution(0, 63)) # 3
