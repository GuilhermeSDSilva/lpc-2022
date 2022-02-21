import pygame

pygame.init()

size = (700, 700)

player_x = 350
player_y = 670

ball_x = 350
ball_y = 670
tela = pygame.display.set_mode(size)

#movimentos da bola
player_move_direita = False
player_move_esquerda = False


# direão da bola
para_direita = True
para_cima = True
d =  para_direita
c = para_cima


velocidadex = 0.6
velocidadey = 1
# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, "white", "black")
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
victory_text = victory_font .render('VICTORY', True, "white", "black")
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (350, 350)

# texto derrota
lose_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
lose_text = lose_font .render('LOSE', True, "white", "black")
lose_text_rect = score_text.get_rect()
lose_text_rect.center = (350, 350)

vitoria = 0


#valores dos blocos
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0


while True:
    tela.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_move_direita = True
            if event.key == pygame.K_a:
                player_move_esquerda = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_move_direita = False
            if event.key == pygame.K_a:
                player_move_esquerda = False

    if vitoria != 10 :

        #blocos
        bloco4 = pygame.draw.rect(tela,"white",(40+x4,10,80,10))
        bloco2 = pygame.draw.rect(tela,"white",(200+x2,10,80,10))
        bloco3 = pygame.draw.rect(tela,"white",(400+x3,10,80,10))
        bloco1 = pygame.draw.rect(tela,"white",(330+x1,60,80,10))
        bloco5 = pygame.draw.rect(tela,"white",(70+x5,40,80,10))
        bloco6 = pygame.draw.rect(tela,"white",(180+x6,40,80,10))
        bloco7 = pygame.draw.rect(tela,"white",(300+x7,40,80,10))
        bloco8 = pygame.draw.rect(tela,"white",(60+x8,60,80,10))
        bloco9 = pygame.draw.rect(tela,"white",(600+x9,50,80,10))
        bloco10 = pygame.draw.rect(tela,"white",(550+x10,30,80,10))


        
        player = pygame.draw.rect(tela,"red",(player_x,player_y,50,10))
        ball = pygame.draw.rect(tela,"blue",(ball_x,ball_y, 20, 20))

        # parederes
        wall_up = pygame.draw.rect(tela,"green",(0,0,700,10))
        wall_down = pygame.draw.rect(tela,"green",(0,690,700,10))
        wall_right = pygame.draw.rect(tela,"green",(690,0,10,700))
        wall_left = pygame.draw.rect(tela,"green",(0,0,10,700))

        # Direão da bola direita e esquerda
        if para_direita == True:
            ball_x += velocidadex
        elif para_direita == False:
            ball_x -= velocidadex

        # Direão da bola cima e baixo
        if para_cima == True:
            ball_y -= velocidadey
        elif para_cima == False:
            ball_y += velocidadey
    

        #colisão com a parede direita e esquerda
        if ball.colliderect(wall_right):
            para_direita = False
        elif ball.colliderect(wall_left):
            para_direita = True

        #colisão com a parede cime e baixo
        if ball.colliderect(wall_up):
            para_cima = False
        elif ball.colliderect(player):
            para_cima = True

        #movimento da raquete
        if player_move_direita == True:
            player_x +=1
        else:
            player_x +=0
        if player_move_esquerda == True:
            player_x -=1
        else:
            player_x -=0

        # colisão com os blocos
        if ball.colliderect(bloco1):
            para_cima = not(c)
            
            vitoria +=1
            x1 = x1+1000
            
        elif ball.colliderect(bloco2):
            para_cima = not(c)
            
            vitoria +=1
            x2 += 1000
        elif ball.colliderect(bloco3):
            para_cima = not(c)
            
            vitoria +=1
            x3 += 1000
        elif ball.colliderect(bloco4):
            para_cima = not(c)
            
            vitoria +=1
            x4 += 1000
        elif ball.colliderect(bloco5):
            para_cima = not(c)
            
            vitoria +=1
            x5 += 1000
        elif ball.colliderect(bloco6):
            para_cima = not(c)
            
            vitoria +=1
            x6 += 1000
        elif ball.colliderect(bloco7):
            para_cima = not(c)
            
            vitoria +=1
            x7 += 1000
        elif ball.colliderect(bloco8):
            para_cima = not(c)
            
            vitoria +=1
            x8 += 1000
        elif ball.colliderect(bloco9):
            para_cima = not(c)
            
            vitoria +=1
            x9 += 1000
        elif ball.colliderect(bloco10):
            para_cima = not(c)
            
            vitoria +=1
            x10 += 1000

    else:
        # drawing victory
        tela.fill("black")
        
        tela.blit(victory_text, victory_text_rect)
        pygame.time.wait(10)
        
    if ball_y > 700:
        # desenhar derrota
        tela.fill("black")
        tela.blit(lose_text, lose_text_rect)
        pygame.time.wait(10)
        
    pygame.display.update()
    pygame.display.flip()
       
pygame.quit()
