import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Noktalardan Karmaşık Animasyon 🎨")
clock = pygame.time.Clock()
FPS = 60

BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)

# ---------------------- Nokta karakter ----------------------
class DotCharacter:
    def __init__(self, x, y, size=5):
        self.size = size
        self.pos = [(x+i*size*2, y+j*size*2) for i in range(3) for j in range(3)]
        self.dx = random.choice([-2,2])
        self.dy = random.choice([-2,2])

    def move(self):
        self.pos = [(x+self.dx, y+self.dy) for x,y in self.pos]
        # Ekran sınırı kontrolü
        if any(x<0 or x>WIDTH for x,y in self.pos):
            self.dx *= -1
        if any(y<0 or y>HEIGHT for x,y in self.pos):
            self.dy *= -1

    def draw(self, surface):
        for x,y in self.pos:
            pygame.draw.circle(surface, BLUE, (x,y), self.size)

# ---------------------- Rastgele "düşman" noktalar ----------------------
class MovingDot:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.size = random.randint(2,6)
        self.dx = random.choice([-3,-2,-1,1,2,3])
        self.dy = random.choice([-3,-2,-1,1,2,3])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x<0 or self.x>WIDTH:
            self.dx *= -1
        if self.y<0 or self.y>HEIGHT:
            self.dy *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.x,self.y), self.size)

# ---------------------- Oluştur ----------------------
player = DotCharacter(WIDTH//2, HEIGHT//2)
dots = [MovingDot() for _ in range(30)]
stars = [(random.randint(0,WIDTH), random.randint(0,HEIGHT)) for _ in range(50)]

# ---------------------- Döngü ----------------------
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------------- Hareket ----------------------
    player.move()
    for d in dots:
        d.move()

    # ---------------------- Çiz ----------------------
    screen.fill(BLACK)

    # Arka plan yıldızları
    for sx,sy in stars:
        pygame.draw.circle(screen, WHITE, (sx,sy), 2)

    player.draw(screen)
    for d in dots:
        d.draw(screen)

    pygame.display.flip()

pygame.quit()
