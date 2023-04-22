"""
Bringing a Gun to a Trainer Fight
=================================

Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you grabbed a beam 
weapon from an abandoned storeroom while you were running through the station, so you have a chance to fight your 
way out. But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect 
off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also
know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam 
hits either you or the bunny trainer, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, trainer_position, distance) that gives an array of 2 integers 
of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 
integers of the trainer's x and y coordinates in the room, and returns an integer of the number of distinct 
directions that you can fire to hit the elite trainer, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite trainer are both 
positioned on the integer lattice at different distinct positions (x, y) inside the room 
such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming 
harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite trainer were positioned in a room with dimensions [3, 2], your_position [1, 1], 
trainer_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the 
elite trainer (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], 
and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, 
the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite trainer 
with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting 
the elite trainer with a total shot distance of sqrt(5).

Test cases
==========
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
"""
import math

def reflect_position(dimensions, position, reflection):
    def reflect(axis):
        if reflection[axis] % 2 == 0:
            return reflection[axis] * dimensions[axis] + position[axis]
        else:
            return (reflection[axis] + 1) * dimensions[axis] - position[axis]
        
    # 0 - x, 1 - y
    return [reflect(0), reflect(1)]

def distance_from_self_squared(src, dest):
    return (src[0] - dest[0]) ** 2 + (src[1] - dest[1]) ** 2

def get_angle(src, dest):
    return math.atan2(dest[1] - src[1], dest[0] - src[0])

def solution(dimensions, your_position, trainer_position, distance):
    #Your code here
    
    # Reflected positions are stored in the form [[our_reflected_position],[trainer_reflected_position]]
    reflected_positions = []
    
    # Get the maximum number of reflections for the first quadrant
    max_x = -((your_position[0] + distance) // -dimensions[0])
    max_y = -((your_position[1] + distance) // -dimensions[1])
    
    # Get all the reflected positions for the first quadrant
    for x in range(max_x):
        for y in range(max_y):
            reflection = [x, y]
            reflected_positions.append(reflect_position(dimensions, your_position, reflection) + ['p'])
            reflected_positions.append(reflect_position(dimensions, trainer_position, reflection) + ['t'])
    
    # Extend the reflected positions to the other quadrants
    q = []
    for position in reflected_positions:
        q.append([position[0], position[1], position[2]])
        q.append([-position[0], position[1], position[2]])
        q.append([-position[0], -position[1], position[2]])
        q.append([position[0], -position[1], position[2]])
    
    # Filter out the reflected positions that are out of range or have the same direction
    target = {}
    for position in q:
        reflected_position = [position[0], position[1]]
        direction = get_angle(your_position, reflected_position)
        squared_length = distance_from_self_squared(your_position, reflected_position)
        
        # Dont include the position that is out of range
        if not (distance * distance >= squared_length > 0):
            continue
        
        # Filter out the positions that have the same direction
        if (direction not in target or distance * distance < target[direction][1]):
            target[direction] = [position, squared_length]
        
    # Count the number of targets
    count = 0
    for direction in list(target.keys()):
        if target[direction][0][2] == 't':
            count += 1

    return count
    
print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
