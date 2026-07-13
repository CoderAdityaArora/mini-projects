import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
SPEED = 10

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)


def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))


def message(text, color, x, y):
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))


def game():
    x = WIDTH // 2
    y = HEIGHT // 2

    dx = 0
    dy = 0

    snake = [[x, y]]
    length = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = BLOCK_SIZE

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        if head in snake[:-1]:
            running = False

        if x == food_x and y == food_y:
            length += 1
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
        draw_snake(snake)

        message(f"Score: {length - 1}", WHITE, 10, 10)

        pygame.display.update()
        clock.tick(SPEED)

    screen.fill(BLACK)
    message("Game Over!", RED, WIDTH // 2 - 70, HEIGHT // 2 - 20)
    message(f"Final Score: {length - 1}", WHITE, WIDTH // 2 - 70, HEIGHT // 2 + 10)
    pygame.display.update()
    pygame.time.wait(3000)


game()
pygame.quit()
