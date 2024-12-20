import pygame
import numpy as np
import sounddevice as sd
import queue
import threading
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT = SCREEN_HEIGHT - 50
T_REX_SIZE = 50
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 40
OBSTACLE_COLOR = (200, 50, 50)
FPS = 60

# Initialize pygame
pygame.init()

# Sound processing variables
audio_queue = queue.Queue()
volume_threshold = 0.00001
jump_scaling = 200

# Start microphone input
def audio_callback(indata, frames, time, status):
    """Callback for sounddevice to collect audio data."""
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())

# TRex class as a rectangle
class TRex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initial_y = y
        self.jump_velocity = 0
        self.gravity = 2
        self.is_jumping = False
        self.width = T_REX_SIZE
        self.height = T_REX_SIZE

    def update(self):
        if self.is_jumping:
            self.y -= self.jump_velocity
            self.jump_velocity -= self.gravity
            if self.y >= self.initial_y:
                self.y = self.initial_y
                self.is_jumping = False

    def jump(self, volume):
        if not self.is_jumping:
            self.jump_velocity = int(volume * jump_scaling)
            self.is_jumping = True
            print(f"Jump triggered with volume: {volume:.4f}, velocity: {self.jump_velocity}")

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y - self.height, self.width, self.height))

# Obstacle class as rectangles
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.speed = 5

    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH + random.randint(100, 300)

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y - self.height, self.width, self.height))

# Scoring System
class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

# Main game loop
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("T-Rex Jump Game")
    clock = pygame.time.Clock()

    # Initialize game objects
    trex = TRex(100, GROUND_HEIGHT)
    obstacles = [Obstacle(SCREEN_WIDTH + i * 300, GROUND_HEIGHT) for i in range(3)]
    score = Score()

    # Start audio input thread
    def process_audio():
        moving_average = []
        window_size = 10
        while True:
            try:
                data = audio_queue.get(timeout=0.1)
                volume_norm = np.sqrt(np.mean(data**2))
                moving_average.append(volume_norm)
                if len(moving_average) > window_size:
                    moving_average.pop(0)
                avg_volume = np.mean(moving_average)
                if avg_volume > volume_threshold:
                    trex.jump(avg_volume)
            except queue.Empty:
                continue

    audio_thread = threading.Thread(target=process_audio, daemon=True)
    audio_thread.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    trex.jump(1)

        # Update game objects
        trex.update()
        for obstacle in obstacles:
            obstacle.update()
        score.update()

        # Collision detection
        collision = False
        for obstacle in obstacles:
            if pygame.Rect(obstacle.x, obstacle.y - obstacle.height, obstacle.width, obstacle.height).colliderect(
                pygame.Rect(trex.x, trex.y - trex.height, trex.width, trex.height)
            ):
                collision = True
                break

        if collision:
            print("Game Over!")
            running = False

        # Render game objects
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (SCREEN_WIDTH, GROUND_HEIGHT), 2)
        trex.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        score.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Entry point
if __name__ == "__main__":
    try:
        with sd.InputStream(callback=audio_callback, channels=1, samplerate=44100):
            game_loop()
    except Exception as e:
        print(f"Error: {e}")