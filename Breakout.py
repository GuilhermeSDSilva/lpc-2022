import pygame
import random
pygame.init()


def inicio():
    pygame.mixer.music.load('collision.mp3')
    colisao = pygame.mixer.Sound("collision2.mp3")

    # construir tela
    size = (700, 700)
    tela = pygame.display.set_mode(size)
    pygame.display.set_caption('Breakout')

    # posições da raquete
    player_x = 350
    player_y = 670

    # posições da bola
    ball_x = 350
    ball_y = 670

    cor = ["abc", "yellow", "blue", "green", "orange", "red"]

    # movimentos da bola
    player_move_direita = False
    player_move_esquerda = False

    # direão da bola
    para_direita = True
    para_cima = True
    d = para_direita
    c = para_cima

    # velocidades das direções da bola
    velocidadex = random.uniform(0.6, 1.2)
    velocidadey = 1

    # texto de pontução
    score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
    score_text = score_font.render('00 x 00', True, "white", "black")
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (680, 50)

    # texto de vitoria
    victory_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
    victory_text = victory_font .render('VICTORY', True, "white", "black")
    victory_text_rect = score_text.get_rect()
    victory_text_rect.center = (350, 350)

    # texto derrota
    lose_font = pygame.font.Font('assets/PressStart2P.ttf', 50)
    lose_text = lose_font .render('LOSE', True, "white", "black")
    lose_text_rect = score_text.get_rect()
    lose_text_rect.center = (350, 350)

    # texto retomar
    return_font = pygame.font.Font('assets/PressStart2P.ttf', 15)
    return_text = return_font .render('Pressione z para Retornar',
                                      True, "white", "black")
    return_text_rect = score_text.get_rect()
    return_text_rect.center = (350, 350)

    vitoria = 0

    # valores dos blocos
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
    x11 = 0
    x12 = 0
    x13 = 0
    x14 = 0
    x15 = 0

    while True:
        tela.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player_move_direita = True
                if event.key == pygame.K_a:
                    player_move_esquerda = True
                if event.key == pygame.K_z:
                    colisao.play()
                    inicio()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player_move_direita = False
                if event.key == pygame.K_a:
                    player_move_esquerda = False

        if vitoria != 2:

            # blocos
            bloco4 = pygame.draw.rect(tela, "red", (50+x4, 10, 80, 10))
            bloco2 = pygame.draw.rect(tela, "red", (250+x2, 10, 80, 10))
            bloco3 = pygame.draw.rect(tela, "red", (450+x3, 10, 80, 10))
            bloco1 = pygame.draw.rect(tela, "orange", (140+x1, 30, 80, 10))
            bloco5 = pygame.draw.rect(tela, "orange", (340+x5, 30, 80, 10))
            bloco6 = pygame.draw.rect(tela, "orange", (540+x6, 30, 80, 10))
            bloco7 = pygame.draw.rect(tela, "green", (50+x7, 50, 80, 10))
            bloco8 = pygame.draw.rect(tela, "green", (250+x8, 50, 80, 10))
            bloco9 = pygame.draw.rect(tela, "green", (450+x9, 50, 80, 10))
            bloco10 = pygame.draw.rect(tela, "blue", (140+x10, 70, 80, 10))
            bloco11 = pygame.draw.rect(tela, "blue", (340+x11, 70, 80, 10))
            bloco12 = pygame.draw.rect(tela, "blue", (540+x12, 70, 80, 10))
            bloco13 = pygame.draw.rect(tela, "yellow", (50+x13, 90, 80, 10))
            bloco14 = pygame.draw.rect(tela, "yellow", (250+x14, 90, 80, 10))
            bloco15 = pygame.draw.rect(tela, "yellow", (450+x15, 90, 80, 10))

            # desenhar raquete
            player = pygame.draw.rect(tela, "red",
                                      (player_x, player_y, 70, 10))

            # dsenhar bola
            ball = pygame.draw.rect(tela, "blue", (ball_x, ball_y, 20, 20))

            # parederes
            wall_up = pygame.draw.rect(tela, "green", (0, 0, 700, 10))
            wall_down = pygame.draw.rect(tela, "green", (0, 690, 700, 10))
            wall_right = pygame.draw.rect(tela, "green", (690, 0, 10, 700))
            wall_left = pygame.draw.rect(tela, "green", (0, 0, 10, 700))

            # Direão da bola direita e esquerda
            if para_direita is True:
                ball_x += velocidadex
            elif para_direita is not True:
                ball_x -= velocidadex

            # Direão da bola cima e baixo
            if para_cima is True:
                ball_y -= velocidadey
            elif para_cima is not True:
                ball_y += velocidadey

            # colisão com a parede direita e esquerda
            if ball.colliderect(wall_right):
                para_direita = False
            elif ball.colliderect(wall_left):
                para_direita = True

            # colisão com a parede cime e baixo
            if ball.colliderect(wall_up):
                para_cima = False
            elif ball.colliderect(player):
                para_cima = True

            # bola aumenta a velocidade quando bate na raquete
            if ball.colliderect(player):

                velocidadey += 0.01

            # movimento da raquete
            if player_move_direita is True:
                player_x += 1
            else:
                player_x += 0
            if player_move_esquerda is True:
                player_x -= 1
            else:
                player_x -= 0

            # colisão com os blocos
            if ball.colliderect(bloco1):
                para_cima = not(c)
                vitoria += 1
                x1 = x1 + 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco2):
                para_cima = not(c)
                vitoria += 1
                x2 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco3):
                para_cima = not(c)
                vitoria += 1
                x3 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco4):
                para_cima = not(c)
                vitoria += 1
                x4 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco5):
                para_cima = not(c)
                vitoria += 1
                x5 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco6):
                para_cima = not(c)
                vitoria += 1
                x6 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco7):
                para_cima = not(c)
                vitoria += 1
                x7 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco8):
                para_cima = not(c)
                vitoria += 1
                x8 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco9):
                para_cima = not(c)
                vitoria += 1
                x9 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco10):
                para_cima = not(c)
                vitoria += 1
                x10 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco11):
                para_cima = not(c)
                vitoria += 1
                x11 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco12):
                para_cima = not(c)
                vitoria += 1
                x12 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco13):
                para_cima = not(c)
                vitoria += 1
                x13 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco14):
                para_cima = not(c)
                vitoria += 1
                x14 += 1000
                pygame.mixer.music.play()
            elif ball.colliderect(bloco15):
                para_cima = not(c)
                vitoria += 1
                x15 += 1000
                pygame.mixer.music.play()

        else:
            tela.blit(victory_text, victory_text_rect)

        if ball_y > 700:
            # desenhar derrota
            tela.fill("black")
            tela.blit(return_text, return_text_rect)

        pygame.display.update()
        pygame.display.flip()
inicio()
pygame.quit()
