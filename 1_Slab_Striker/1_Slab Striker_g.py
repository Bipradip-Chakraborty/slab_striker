#Inroduction to Slab Striker:

print('To Play the game press the enter button....')

import pygame
import random

#=================================================================================================================

#Initializing the game:
pygame.init()
width = 500
height = 500
gamewin = pygame.display.set_mode((width , height))
pygame.display.set_caption('Slab Striker')

font = pygame.font.SysFont(None, 44)

def t_siz(text, color, x, y):
    score_t = font.render(text, True, color)
    gamewin.blit(score_t, [x, y])


#New windows for greeting:
def welcome():
    exit_game = False
    while not exit_game:
        gamewin.fill((255, 228, 196))
        t_siz('** Welcome to Slab Striker **', (255, 0, 0), 50, 200)
        t_siz('-- Press Space Bar To Play --', (0, 0, 255), 50, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()



#================================================================================================================

def gameloop():
    #Player_set:
    wi = 0
    player_x = 40
    player_y = 25
    player_siz = 12
    player_siz2 = 35


    #Line:
    line_x = 0
    line_y = 30
    linesiz = 25
    linesiz2 = 600

#================================================================================================================

    #Enemy_set:
    enemy_x = 450
    enemy_y = random.randint(30, 485)
    enemy_siz = 15
    velocity_x = 0
    velocity_y = 0
    velocity = 6

    #score:
    score = 0

    font = pygame.font.SysFont(None, 33)

    def t_siz(text, color, x, y):
        score_t = font.render(text, True, color)
        gamewin.blit(score_t, [x, y])

    #time:
    clock = pygame.time.Clock()

    #Read the high score:
    with open('1.1_Slab Striker_ghiscore') as f:
        highscore = f.read()



#============================================================================================================

    #GameLoop:
    game_over = False
    running = True

    while running :
        if game_over:
            gamewin.fill((0, 0, 0))
            t_siz('Game Over! Press enter to continue.', (255, 0,0), 50, 200)

            #Display the high score:
            with open('1.1_Slab Striker_ghiscore', 'w') as d:
                d.write(str(highscore))

            #Close the game easily:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -velocity
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = velocity
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        velocity_y = 0

            player_y += velocity_y

            if player_y < 30:
                player_y = 30

            if player_y > 465:
                player_y = 465



            enemy_x -= 5

            if enemy_x< 25:
                enemy_x = 500
                enemy_y = random.randint(30, 485)
                wi += 10

            if wi==80:
                game_over = True

#=================================================================================================================

            #Check for any collision:
            if enemy_y > player_y and enemy_y < (player_y+ 35) and (player_x + 10 ) == enemy_x :
                score += 10
                enemy_x = 500
                enemy_y = random.randint(30, 485)


            if enemy_y == player_y and (player_x + 10 ) == enemy_x :
                score+= 10
                enemy_x = 500
                enemy_y = random.randint(30, 485)

            if enemy_y == (enemy_y+35) and (player_x + 10 ) == enemy_x :
                score += 10
                enemy_x = 500
                enemy_y = random.randint(30, 485)
            #Show the highscore:
            if score> int(highscore):
                highscore = score

            #Write the score as if there is no end occures...
            with open('1.1_Slab Striker_ghiscore', 'w') as d:
                d.write(str(highscore))

#===================================================================================================================
            # player_y += velocity_y

            gamewin.fill((0, 255, 0))

            t_siz('score: ' + str(score)+ '  Hi-Score: '+ str(highscore), (255, 0, 0), 4, 4)

            pygame.draw.rect(gamewin, (0, 0, 0), [player_x , player_y , player_siz, player_siz2])
            pygame.draw.rect(gamewin, (255, 0, 0), [enemy_x, enemy_y, enemy_siz, enemy_siz])
            pygame.draw.rect(gamewin, (0, 0, 255), [line_x, line_y , linesiz, linesiz2])
            pygame.draw.rect(gamewin, (255, 0, 0), [410, 4, 80, 15])
            pygame.draw.rect(gamewin, (0, 0, 255), [410, 4, wi, 15])
            pygame.draw.rect(gamewin, (0, 0, 0), [0, 25, 500, 2])

        pygame.display.update()
        clock.tick(60)

    print('Thanks for playing this game.')
    pygame.quit()
    quit()


welcome()
gameloop()