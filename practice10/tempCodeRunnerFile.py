    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))       
 
    pygame.draw.rect(game_window, orange,
                     pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))