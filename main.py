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
time = 0
# Cardinal directions
cardinal_directions = ["north", "east", "south", "west"]

# Random color generator
bg_color: Color = pygame.Color(random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))

# Makes the start end endpoint for the map segment
start_point = pygame.Vector2()
end_point = pygame.Vector2()

def start_end_point():
    screen_size = pygame.Vector2(dis.get_width(), dis.get_height())


    x = random.choice([1, 2])

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
start_end_point()

# Defines the position of the player when starting the program
player = pygame.image.load("artboard-1.png")
player = pygame.transform.scale(player,(40, 40))
player_pos = pygame.Vector2(start_point.x, start_point.y)


# configures where the end object collision detector should be
end_rect = pygame.Rect(end_point.x - 20, end_point.y - 20, 40, 40)
color_end_box = "green"

# the algorithm to make the maze
rectangles_in_game_pre = []
rectangles_in_game = []
def Maze_algo():
    rect_amount = 1
    pos = pygame.Vector2()
    x = 0
    y = 0
    for i in range(15):
        pos.y = y
        for i in range(20):
            rand_boolean = random.choice((True, False))
            if rand_boolean == True:
                pos.x = x
                val = pygame.Rect(pos.x, pos.y, 80, 80)
                rectangles_in_game_pre.append(val)
                x += 160
            else:
                x += 80

        x = 0
        y += 80
    for x in rectangles_in_game_pre:
        z = random.choice((True, False))
        if z == True:
            rectangles_in_game.append(x)
        else:
            pass



Maze_algo()

def game_Finished():
    dis.fill((0, 0, 0))
    Font = pygame.font.Font(None, 30)
    game_over_text = font.render("GAME FINISHED", True, (200, 200, 200))
    game_time_text = font.render(f"Time taken to finished Maze Runner {int(time/60)} Seconds ", True, (200, 200, 200))
    game_rerun_text = font.render("press SPACE to try again", True, (200, 200, 200))
    dis.blit(game_over_text, (dis.get_width() / 2 - (game_over_text.get_width()/2), dis.get_height() / 2 - 40))
    dis.blit(game_time_text, (dis.get_width() / 2 - (game_time_text.get_width()/2), dis.get_height() / 2))
    dis.blit(game_rerun_text, (dis.get_width() / 2 - (game_rerun_text.get_width()/2), dis.get_height() / 2 + 60))

def reset_game():
    start_end_point()
    # configures where the end object collision detector should be
    end_rect.x = end_point.x - 20
    end_rect.y = end_point.y - 20
    player_pos.x = start_point.x
    player_pos.y = start_point.y
    print(player_pos)

# This is were the code gets run while playing
game_over = False
while not game_over:
    # option to quit the game at anytime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # fills in background
    dis.fill((255,255,255))

    # The figure of the character
    dis.blit(player, player_pos)
    player_hitbox = pygame.Rect(player_pos.x, player_pos.y, 40, 40)
    pygame.draw.rect(dis, "red", player_hitbox, 2)

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

    # draws start and end point
    pygame.draw.circle(dis, "red", start_point, 20)
    pygame.draw.circle(dis, "blue", end_point, 20)

    # draws the maze
    for x in range(len(rectangles_in_game)):
        rect_maze = rectangles_in_game[x]
        pygame.draw.rect(dis, bg_color, rect_maze, 1)

    """
               if (player_hitbox.top - x.bottom) < 0:
                   W = 0
                   #player_pos.y = x.bottom
                   print("bottom")
               elif (x.top - player_hitbox.bottom) < 0:
                   S = 0
                   #player_pos.y = x.top - 40
                   print("top")
               elif (x.left - player_hitbox.right) < 0:
                   A = 0
                   #player_pos.x = x.left
                   print("left")
               elif (player_hitbox.left - x.right) < 0:
                   D = 0
                   #player_pos.x = x.right - 40
                   print("right")
               """
    # checks if the player is colliding with player
    W = 200
    S = 200
    A = 200
    D = 200
    for x in rectangles_in_game:
        if player_hitbox.clipline(x.leftbottom, x.rightbottom):
            W = 0
            #player_pos.y = x.bottom
            print("bottom")
        elif player_hitbox.clipline(x.lefttop, x.righttop):
            S = 0
            #player_pos.y = x.top - 40
            print("top")
        elif player_hitbox.clipline(x.lefttop, x.leftbottom):
            A = 0
            #player_pos.x = x.left
            print("left")
        elif player_hitbox.clipline(x.righttop, x.rightbottom):
            D = 0
            #player_pos.x = x.right - 40
            print("right")

    # Makes the character move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= W * dt
    if keys[pygame.K_s]:
        player_pos.y += S * dt
    if keys[pygame.K_a]:
        player_pos.x -= A * dt
    if keys[pygame.K_d]:
        player_pos.x += D * dt
    """    
    print(W)
    print(S)
    print(A)
    print(D)
    """
        # function for if the player touches the wall
        # check if the Player has gone off the screen
    if player_pos[0] < 0:
        player_pos[0] = 0
    if player_pos[0] + player.get_width() > dis.get_width():
        player_pos[0] = dis.get_width() - player.get_width()
    if player_pos[1] < 0:
        player_pos[1] = 0
    if player_pos[1] + player.get_height() > dis.get_height():
        player_pos[1] = dis.get_height() - player.get_height()

    # Checks if you have reached the finish line
    pygame.draw.rect(dis, color_end_box, end_rect, 4)
    if player_hitbox.colliderect(end_rect):
        game_Finished()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("pressed")
            time = 0
            reset_game()
    else:
        # adds time counter to the game
        time += 1

    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
quit()
