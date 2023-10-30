import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Persecución")

# Configuración de la fuente para mostrar la puntuación
font = pygame.font.Font(None, 36)

# Clases para el jugador (ratón) y el agente (gato)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("raton.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        
        # Limitar al jugador a los bordes de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height

class Agent(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("gato.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, player_rect):
        if player_rect.x > self.rect.x:
            self.rect.x += 1
        elif player_rect.x < self.rect.x:
            self.rect.x -= 1
        if player_rect.y > self.rect.y:
            self.rect.y += 1
        elif player_rect.y < self.rect.y:
            self.rect.y -= 1

        # Limitar al agente a los bordes de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height

# Inicialización de los personajes
player = Player()
agent = Agent(100, 100)

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(agent)

# Configuración del temporizador para la puntuación
score = 0
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Bucle del juego
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            score += 1

    # Actualizar sprites
    player.update()
    agent.update(player.rect)

    # Comprobar si el agente (gato) ha atrapado al jugador (ratón)
    if pygame.sprite.spritecollideany(player, [agent]):
        print("¡Atrapado! Puntuación final:", score)
        running = False

    # Dibujar todo en la pantalla
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    # Mostrar la puntuación
    score_text = font.render("Puntuacionn: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Capar la tasa de frames a 60
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()