import pygame
import time
import random
 
snake_speed = 10
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black  = pygame.Color(0,   0,   0)
white  = pygame.Color(255, 255, 255)
red    = pygame.Color(255,  0,   0)
green  = pygame.Color(0,  200,   0)
yellow = pygame.Color(255, 215,  0)
orange = pygame.Color(255, 140,  0)
 
# Level thresholds and speeds: (score_needed, snake_speed)
levels = [
    (0,   10),
    (30,  14),
    (70,  18),
    (120, 23),
    (180, 28),
]
 
# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90,  50],
              [80,  50],
              [70,  50]]
 
# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction
 
# initial score and level
score         = 0
current_level = 0
 
 
# generating fruit position that doesn't overlap with the snake body
def new_fruit_position(snake_body):
    while True:
        x = random.randrange(1, (window_x // 10) - 1) * 10
        y = random.randrange(1, (window_y // 10) - 1) * 10
        if [x, y] not in snake_body:
            return [x, y]
 
 
# returns the level index the player is currently on based on score
def get_level(score):
    level = 0
    for i, (threshold, _) in enumerate(levels):
        if score >= threshold:
            level = i
    return level
 
 
# displaying score and level on screen
def show_hud(score, level):
    font       = pygame.font.SysFont('times new roman', 20)
    score_surf = font.render('Score : ' + str(score), True, white)
    level_surf = font.render('Level : ' + str(level + 1), True, yellow)
    level_rect = level_surf.get_rect()
    level_rect.topright = (window_x - 8, 4)
    game_window.blit(score_surf, (8, 4))
    game_window.blit(level_surf, level_rect)

# briefly shows a level-up banner so the player notices the level change
def show_level_up(level):
    font = pygame.font.SysFont('times new roman', 42)
    surf = font.render('  Level ' + str(level + 1) + '!  ', True, black, yellow)
    rect = surf.get_rect(center=(window_x // 2, window_y // 2))
    game_window.blit(surf, rect)  # blits 
    pygame.display.flip() # shows
    time.sleep(0.1) # pauses

# game over function
def game_over():
    my_font          = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect   = game_over_surface.get_rect()
 
    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)
 
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
 
    # after 2 seconds we will quit the program
    time.sleep(5)
 
    # deactivating pygame library
    pygame.quit()
 
    # quit the program
    quit()
 
 
# first fruit spawned at a safe position (not on the snake)
fruit_position = new_fruit_position(snake_body)
fruit_spawn    = True
 
 
# Main Function
while True:
 
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # If two keys pressed simultaneously
    # we don't want snake to move into two directions simultaneously
    if change_to == 'UP'    and direction != 'DOWN':  direction = 'UP'
    if change_to == 'DOWN'  and direction != 'UP':    direction = 'DOWN'
    if change_to == 'LEFT'  and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':  direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':    snake_position[1] -= 10
    if direction == 'DOWN':  snake_position[1] += 10
    if direction == 'LEFT':  snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruit and snake collide then score will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score      += 10
        fruit_spawn = False
    else:
        snake_body.pop()
 
    # spawn new fruit at a position that doesn't overlap the snake body
    if not fruit_spawn:
        fruit_position = new_fruit_position(snake_body)
        fruit_spawn    = True
 
    # check if score crossed a level threshold and update speed accordingly
    new_level = get_level(score)
    if new_level != current_level:
        current_level = new_level
        snake_speed   = levels[current_level][1]
        show_level_up(current_level)
 
    game_window.fill(black)
 
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))       
 
    pygame.draw.rect(game_window, orange,
                     pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score and level continuously
    show_hud(score, current_level)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second / Refresh Rate
    fps.tick(snake_speed)