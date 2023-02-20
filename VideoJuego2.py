import pygame

# Inicializar Pygame
pygame.init()

# Establecer las dimensiones de la pantalla
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Cargar las imágenes del personaje
player_image_right = pygame.image.load('player/Idle/pam1.png')
player_image_left = pygame.image.load('player/Idle/pam2.png')
player_rect = player_image_right.get_rect()
player_rect = player_image_left.get_rect()


# Cargar la imagen del fondo
background_image = pygame.image.load('player/Idle/fam4.jpg')
background_rect = background_image.get_rect()
background_width, background_height = background_image.get_size()

# Establecer el tiempo inicial
start_time = pygame.time.get_ticks()

# Centrar la imagen del fondo
background_x = SCREEN_WIDTH // 2 - background_width // 2
background_y = SCREEN_HEIGHT // 2 - background_height // 2


# Definir la posición y el tamaño del personaje
player_width, player_height = player_image_right.get_size()
player_x = SCREEN_WIDTH / 2 - player_width / 2
player_y = SCREEN_HEIGHT - player_height

# Definir la velocidad y la gravedad del personaje
player_speed = 0.4
player_gravity = 0.10
player_velocity = 0

# Definir la dirección inicial del personaje
player_direction = 'right'

# Establecer el movimiento vertical del jugador
player_y_momentum = 0

# Crear una lista de plataformas
platforms = [
    pygame.Rect(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),
    pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 80, 100, 20),
    pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 160, 200, 20),
    pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 240, 100, 20)
]

# Bucle principal del juego
running = True
while running:

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calcular el tiempo transcurrido
    elapsed_time = pygame.time.get_ticks() - start_time

    # Calcular el índice del cuadro actual en la animación
    frame_index = (elapsed_time // 100) % background_rect.width

    # Manejar entradas del teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
        player_direction = 'left'
    if keys[pygame.K_d]:
        player_x += player_speed
        player_direction = 'right'

    # Aplicar gravedad al personaje
    player_y_momentum += 0.2
    player_velocity += player_gravity
    player_y += player_velocity

     # Detectar colisiones con las plataformas
    for platform in platforms:
        if player_rect.colliderect(platform):
            player_y_momentum = 0
            player_rect.bottom = platform.top
    
    

    # Comprobar si el personaje ha tocado el suelo
    if player_y >= SCREEN_HEIGHT - player_height:
        player_y = SCREEN_HEIGHT - player_height
        player_velocity = 0

    # Comprobar si el jugador ha saltado
    if keys[pygame.K_SPACE] and player_y == SCREEN_HEIGHT - player_height:
        player_velocity = -10

    # Recortar la imagen de fondo para obtener el cuadro actual
    current_frame = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    current_frame.blit(background_image, (0, 0), (frame_index, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    # Dibujar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar las plataformas
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 0), platform)

    screen.blit(background_image, (background_x, background_y))
    if player_direction == 'right':
        screen.blit(player_image_right, (player_x, player_y))
    else:
        screen.blit(player_image_left, (player_x, player_y))
    pygame.display.update()

# Salir de Pygame
pygame.quit()
