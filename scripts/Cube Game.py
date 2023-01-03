import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

WIDTH = 800
HEIGHT = 600

Player_Color = (255, 255, 255)
Player_Size = 50
Player_Pos = [WIDTH / 2, 500]

Enemy_Color = (255, 0, 0)
Enemy_Size = 50
Enemy_Pos = [random.randint(0, WIDTH), 0]
Enemy_Speed = 1
Enemy_List_Size = 10
Enemy_Delay = 0.05
Enemy_List = [Enemy_Pos]

game_over = False
game_fps = 60
game_score = 0
game_score_color = (255, 255, 255)
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 35)

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < Enemy_List_Size and delay < Enemy_Delay:
        x_pos = random.randint(0, WIDTH - Enemy_Size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for Enemy_Pos in enemy_list:
        pygame.draw.rect(screen, (Enemy_Color), (Enemy_Pos[0], Enemy_Pos[1], Enemy_Size, Enemy_Size))
    
def update_enemies(enemy_list, score, enemy_speed):
    for idx, Enemy_Pos in enumerate(enemy_list):
        if Enemy_Pos[1] >= 0 and Enemy_Pos[1] < HEIGHT:
            Enemy_Pos[1] += Enemy_Speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for Enemy_Pos in enemy_list:
        if(detect_collision(Enemy_Pos, player_pos)):
            return True
    return False

def detect_collision(Player_Pos, Enemy_Pos):
    p_x = Player_Pos[0]
    p_y = Player_Pos[1]

    e_x = Enemy_Pos[0]
    e_y = Enemy_Pos[1]

    if (e_x >= p_x and e_x < (p_x + Player_Size)) or (p_x >= e_x and p_x < (e_x + Enemy_Size)):
        if (e_y >= p_y and e_y < (p_y + Player_Size)) or (p_y >= e_y and p_y < (e_y + Enemy_Size)):
            return True
    return False

while not game_over:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = Player_Pos[0]
            y = Player_Pos[1]

            if event.key == pygame.K_a:
                x -= 50
            elif event.key == pygame.K_d:
                x += 50

            Player_Pos = [x, y]

    screen.fill((0, 0, 0))

    drop_enemies(Enemy_List)
    
    game_score = update_enemies(Enemy_List, game_score, Enemy_Speed)
    
    if game_score == 0:
        Enemy_Speed = 1
        Enemy_List_Size = 1
    else:
        Enemy_Speed = game_score / 20 + 1
        Enemy_List_Size = game_score / 2 + 1
    
    score_text = "Score: " + str(game_score)
    score_label = font.render(score_text, 1, game_score_color)
    screen.blit(score_label, (WIDTH - 250, HEIGHT - 40))

    diff_text = "Difficulty: " + str(Enemy_Speed)
    diff_label = font.render(diff_text, 1, game_score_color)
    screen.blit(diff_label, (WIDTH - 800, HEIGHT - 40))

    amount_text = "Amount: " + str(Enemy_List_Size)
    amount_label = font.render(amount_text, 1, game_score_color)
    screen.blit(amount_label, (WIDTH - 800, HEIGHT - 75))
    
    if collision_check(Enemy_List, Player_Pos):
        game_over = True
    
    draw_enemies(Enemy_List)

    pygame.draw.rect(screen, (Enemy_Color), (Enemy_Pos[0], Enemy_Pos[1], Enemy_Size, Enemy_Size))
    pygame.draw.rect(screen, (Player_Color), (Player_Pos[0], Player_Pos[1], Player_Size, Player_Size))
    
    clock.tick(game_fps)
    pygame.RESIZABLE = True
    
    pygame.display.update()