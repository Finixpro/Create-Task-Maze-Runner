import pygame
import random
import math

# initiates the program
from pygame import Color


pygame.init()

dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Maze Runner')
clock = pygame.time.Clock()
dt = 0

# Cardinal directions
cardinal_directions = ["north", "east", "south", "west"]

# chooses background color
bg_color: Color = pygame.Color(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))

# Defines the position of the player when starting the program
player_pos = pygame.Vector2(dis.get_width() / 2, dis.get_height() / 2)

# Makes the start end endpoint for the map segment
def start_end_point():
    screen_size = pygame.Vector2(dis.get_width(), dis.get_height())

    start_point = pygame.Vector2()
    end_point = pygame.Vector2()

    x = random.choice([1, 2])
    print(x)

    color_start = "blue"
    color_end = "red"

    size_circle = 20

    if x == 1:
        start_point.x = random.choice([0, screen_size.x])
        start_point.y = random.randrange(int(screen_size.y))

        if start_point.x == 0:
            x = random.choice([1, 3])
            if x == 1:
                end_point.x = 800
                end_point.y = random.randrange(int(screen_size.y))

            elif x == 2:
                end_point.x = random.randrange(int(screen_size.x))
                end_point.y = 0

            else:
                end_point.x = random.randrange(int(screen_size.x))
                end_point.y = 600

        else:
            x = random.choice([1, 3])
            if x == 1:
                end_point.x = 0
                end_point.y = random.randrange(int(screen_size.y))

            elif x == 2:
                end_point.x = random.randrange(int(screen_size.x))
                end_point.y = 0

            else:
                end_point.x = random.randrange(int(screen_size.x))
                end_point.y = 600

    else:
        start_point.x = random.randrange(int(screen_size.x))
        start_point.y = random.choice([0, screen_size.y])
        pygame.draw.circle(dis, "red", start_point, 20)

        if start_point.y == 0:
            x = random.choice([1, 3])
            if x == 1:
                end_point.x = random.randrange(int(screen_size.x))
                end_point.y = 600

            elif x == 2:
                end_point.x = 0
                end_point.y = random.randrange(int(screen_size.y))

            else:
                end_point.x = 800
                end_point.y = random.randrange(int(screen_size.y))

        else:
            x = random.choice([1, 3])
            if x == 1:
                end_point.x = random.randrange(int(screen_size.x))
                end_point.y = 0

            elif x == 2:
                end_point.x = 0
                end_point.y = random.randrange(int(screen_size.y))

            else:
                end_point.x = 800
                end_point.y = random.randrange(int(screen_size.y))
    print(start_point)
    print(end_point)
    return start_point, end_point

# This is where the command is called for making of the map
val = start_end_point()

start_point = val[0]
end_point = val[1]


def line_maker(start_pos, end_pos):
    distance = math.dist(start_pos, end_pos)
    print(distance)
    direction_start = ""
    direction_end = ""
    pos = pygame.Vector2()

    if start_pos[0] == 0:
        direction_start = cardinal_directions[3]
    elif start_pos[0] == 800:
        direction_start = cardinal_directions[1]
    elif start_pos[1] == 0:
        direction_start = cardinal_directions[0]
    elif start_pos[1] == 600:
        direction_start = cardinal_directions[2]

    if end_pos[0] == 0:
        direction_end = cardinal_directions[3]
    elif end_pos[0] == 800:
        direction_end = cardinal_directions[1]
    elif end_pos[1] == 0:
        direction_end = cardinal_directions[0]
    elif end_pos[1] == 600:
        direction_end = cardinal_directions[2]

    if direction_start == "north":

        if direction_end == "east":
            pos.x = start_pos[0] - end_pos[0]
            pos.y = start_pos[1] - end_pos[1]
        elif direction_end == "south":
            pos.x = start_pos[0] - end_pos[0]
            pos.y = 600
        elif direction_end == "west":
            pos.x = end_pos[0] - start_pos[0]
            pos.y = start_pos[1] - end_pos[1]

    elif direction_start == "east":

        if direction_end == "south":
            pos.x = start_pos[0] - end_pos[0]
            pos.y = start_pos[1] - end_pos[1]
        elif direction_end == "west":
            pos.x = 800
            pos.y = start_pos[1] - end_pos[1]
        elif direction_end == "north":
            pos.x = end_pos[0] - start_pos[0]
            pos.y = start_pos[1] - end_pos[1]

    elif direction_start == "south":

        if direction_end == "west":
            pos.x = end_pos[0] - start_pos[0]
            pos.y = start_pos[1] - end_pos[1]
        elif direction_end == "north":
            pos.x = end_pos[0] - start_pos[0]
            pos.y = 0
        elif direction_end == "east":
            pos.x = end_pos[0] - start_pos[0]
            pos.y = end_pos[1] - start_pos[1]

    elif direction_start == "west":

        if direction_end == "north":
            pos.x = end_pos[0] - start_pos[0]
            pos.y = end_pos[1] - start_pos[1]
        elif direction_end == "east":
            pos.x = 0
            pos.y = end_pos[1] - start_pos[1]
        elif direction_end == "south":
            pos.x = start_pos[0] - end_pos[0]
            pos.y = end_pos[1] - start_pos[1]

    print(direction_start)
    print(direction_end)
    print("here is middle point")
    print(pos)
    return(pos)

val = line_maker(start_point, end_point)




# This is were the code gets run while playing
game_over = False
while not game_over:
    # option to quit the game at anytime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # fills in background
    dis.fill(bg_color)

    # draws start and end point
    pygame.draw.circle(dis, "red", start_point, 20)
    pygame.draw.circle(dis, "blue", end_point, 20)

    # draws line connecting start to end
    pygame.draw.line(dis,"white",start_point, end_point)

    pygame.draw.circle(dis,"pink", val, 20)
    # Adds the Cardinal directions to the game
    if True:
        # North
        font = pygame.font.Font(None, 30)
        text = font.render("north", True, (10, 10, 10))
        text_pos = text.get_rect(centerx=dis.get_width() / 2, y=10)
        dis.blit(text, text_pos)
        # East
        font = pygame.font.Font(None, 30)
        text = font.render("East", True, (10, 10, 10))
        text_pos = text.get_rect(x=750, centery=dis.get_height() / 2)
        dis.blit(text, text_pos)
        # South
        font = pygame.font.Font(None, 30)
        text = font.render("south", True, (10, 10, 10))
        text_pos = text.get_rect(centerx=dis.get_width() / 2, y=580)
        dis.blit(text, text_pos)
        # West
        font = pygame.font.Font(None, 30)
        text = font.render("West", True, (10, 10, 10))
        text_pos = text.get_rect(x=10, centery=dis.get_height() / 2)
        dis.blit(text, text_pos)


    # The figure of the character
    pygame.draw.circle(dis, "green", player_pos, 20)

    # Makes the character move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # function for if the player touches the wall

    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
quit()
