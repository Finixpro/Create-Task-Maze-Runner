import pygame
import math

# set up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# define points A and B
point_a = (100, 100)
point_b = (700, 500)

# define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# calculate the distance between point A and point B
distance = math.sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)

# initialize the line start point and direction
line_start = point_a
line_direction = RIGHT

# define the turning points
turning_points = [(400, 100), (400, 400), (700, 400), (700, 200), (100, 200), (100, 500)]

# loop until the line reaches point B
while line_start != point_b:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # move the line
    line_end = (line_start[0] + line_direction[0], line_start[1] + line_direction[1])

    # draw the line
    pygame.draw.line(screen, WHITE, line_start, line_end)

    # update the display
    pygame.display.flip()

    # wait for a short time to slow down the animation
    pygame.time.wait(50)

    # determine the next direction to move in
    if line_start in turning_points:
        index = turning_points.index(line_start)
        next_index = (index + 1) % len(turning_points)
        next_point = turning_points[next_index]
        if next_point[0] > line_start[0]:
            line_direction = RIGHT
        elif next_point[0] < line_start[0]:
            line_direction = LEFT
        elif next_point[1] > line_start[1]:
            line_direction = DOWN
        elif next_point[1] < line_start[1]:
            line_direction = UP
    else:
        if line_direction == RIGHT:
            if line_end[0] >= point_b[0]:
                line_direction = DOWN
        elif line_direction == DOWN:
            if line_end[1] >= point_b[1]:
                line_direction = LEFT
        elif line_direction == LEFT:
            if line_end[0] <= point_b[0]:
                line_direction = UP
        elif line_direction == UP:
            if line_end[1] <= point_b[1]:
                line_direction = RIGHT

    # update the line start point
    line_start = line_end

# loop until the user quits
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # update the display
    pygame.display.flip()

    # wait for a short time to slow down the animation
    pygame.time.wait(50)

    # tick the clock
    clock.tick(60)

