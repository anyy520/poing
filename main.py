import pygame  # Importa a biblioteca pygame para criar o jogo.
import sys     # Importa sys para encerrar o programa.

# Inicializa o pygame
pygame.init()

# **Configurações da Tela**
SCREEN_WIDTH = 800  # Largura da janela do jogo.
SCREEN_HEIGHT = 600  # Altura da janela do jogo.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Cria a janela do jogo.
pygame.display.set_caption("Pong com Imagens")  # Define o título da janela.

# **Cores**
WHITE = (255, 255, 255)  # Cor branca (RGB).
BLACK = (0, 0, 0)        # Cor preta (RGB).

# **Configurações das Raquetes**
original_paddle_image = pygame.image.load("paddle.png")  # Carrega a imagem da raquete.
paddle_width, paddle_height = 20, 100  # Define o tamanho da raquete.
paddle_image = pygame.transform.scale(original_paddle_image, (paddle_width, paddle_height))  # Redimensiona a raquete.
paddle_speed = 6  # Velocidade de movimento das raquetes.

# **Configurações da Bola**
original_ball_image = pygame.image.load("ball.png")  # Carrega a imagem da bola.
ball_width, ball_height = 20, 20  # Define o tamanho da bola.
ball_image = pygame.transform.scale(original_ball_image, (ball_width, ball_height))  # Redimensiona a bola.
ball_speed = [4, 4]  # Velocidade da bola (horizontal, vertical).

# **Retângulos para Raquetes e Bola**
# Define posições iniciais para as raquetes e a bola.
player1 = pygame.Rect(10, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)  # Raquete esquerda.
player2 = pygame.Rect(SCREEN_WIDTH - paddle_width - 10, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)  # Raquete direita.
ball = pygame.Rect(SCREEN_WIDTH // 2 - ball_width // 2, SCREEN_HEIGHT // 2 - ball_height // 2, ball_width, ball_height)  # Bola no centro.

# **Pontuações**
score1 = 0  # Pontuação do jogador 1.
score2 = 0  # Pontuação do jogador 2.
font = pygame.font.Font(None, 36)  # Fonte para exibir as pontuações.

# **Relógio para Controle de FPS**
clock = pygame.time.Clock()

# **Função para Desenhar os Elementos na Tela**
def draw():
    screen.fill(BLACK)  # Preenche a tela com preto.
    screen.blit(paddle_image, player1)  # Desenha a raquete do jogador 1.
    screen.blit(paddle_image, player2)  # Desenha a raquete do jogador 2.
    screen.blit(ball_image, ball)  # Desenha a bola.
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))  # Linha divisória.

    # Exibe as pontuações.
    score_text = font.render(f"{score1}   {score2}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()  # Atualiza a tela.

# **Função para Mover as Raquetes**
def move_paddle(keys, paddle, up_key, down_key):
    if keys[up_key] and paddle.top > 0:  # Se a tecla "cima" for pressionada e a raquete não estiver no topo.
        paddle.y -= paddle_speed  # Move a raquete para cima.
    if keys[down_key] and paddle.bottom < SCREEN_HEIGHT:  # Se a tecla "baixo" for pressionada e a raquete não estiver no fundo.
        paddle.y += paddle_speed  # Move a raquete para baixo.

# **Função para Resetar a Bola**
def reset_ball():
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Coloca a bola no centro.
    ball_speed[0] *= -1  # Inverte a direção horizontal.

# **Loop Principal do Jogo**
while True:
    # Captura eventos do teclado e do sistema.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se clicar no botão de fechar a janela.
            pygame.quit()  # Encerra o pygame.
            sys.exit()  # Fecha o programa.

    # Movimento da bola.
    ball.x += ball_speed[0]  # Move a bola na direção horizontal.
    ball.y += ball_speed[1]  # Move a bola na direção vertical.

    # Colisão com as paredes.
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:  # Se a bola tocar o topo ou o fundo.
        ball_speed[1] = -ball_speed[1]  # Inverte a direção vertical.

    # Colisão com as raquetes.
    if ball.colliderect(player1) or ball.colliderect(player2):  # Se a bola colidir com uma raquete.
        ball_speed[0] = -ball_speed[0]  # Inverte a direção horizontal.

    # Pontuação.
    if ball.left <= 0:  # Se a bola sair pela esquerda.
        score2 += 1  # O jogador 2 marca ponto.
        reset_ball()  # Reseta a bola.
    if ball.right >= SCREEN_WIDTH:  # Se a bola sair pela direita.
        score1 += 1  # O jogador 1 marca ponto.
        reset_ball()  # Reseta a bola.

    # Movimentação das raquetes.
    keys = pygame.key.get_pressed()  # Captura as teclas pressionadas.
    move_paddle(keys, player1, pygame.K_w, pygame.K_s)  # Movimenta a raquete do jogador 1 (W e S).
    move_paddle(keys, player2, pygame.K_UP, pygame.K_DOWN)  # Movimenta a raquete do jogador 2 (Setas Cima e Baixo).

    # Desenha os elementos na tela.
    draw()

    # Controle de FPS (60 quadros por segundo).
    clock.tick(60)


