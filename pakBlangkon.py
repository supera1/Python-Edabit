import math

def visible_trees(n, x, y, positions):
    angle_dist = {}

    for px, py in positions:
        # Calculate angle using atan2 which considers full circle (360 degrees)
        angle = math.atan2(py - y, px - x)
        # Calculate Euclidean distance from Pak Blangkon to the tree
        dist = math.sqrt((px - x) ** 2 + (py - y) ** 2)
        
        # If the angle already exists, keep the closer tree
        if angle in angle_dist:
            if angle_dist[angle] > dist:
                angle_dist[angle] = dist
        else:
            angle_dist[angle] = dist
    
    # The number of unique angles represents the visible trees
    return len(angle_dist)

n = 8
x, y = 4, 2
positions = [
    (1, 5), (2, 1), (2, 4), (3, 3),
    (6, 3), (6, 6), (7, 7), (10, 5)
]

print(visible_trees(n, x, y, positions))