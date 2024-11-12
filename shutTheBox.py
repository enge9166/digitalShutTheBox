import pygame
import sys
from dice import roll_dice, valid_combinations

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shut the Box")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define font
font = pygame.font.Font(None, 74)

# Define the numbers
numbers = list(range(1, 10))
shut_numbers = []

# Roll the dice
dice1, dice2 = roll_dice()
dice_total = dice1 + dice2
current_sum = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i, num in enumerate(numbers):
                if 50 + i * 80 < x < 130 + i * 80 and 250 < y < 330:
                    # Check if the number can be part of a valid combination
                    valid_combos = valid_combinations(numbers, dice_total)
                    for combo in valid_combos:
                        if num in combo and current_sum + num <= dice_total:
                            current_sum += num
                            shut_numbers.append(num)
                            numbers.remove(num)
                            break
            # Check if the current sum matches the dice total
            if current_sum == dice_total:
                # Reset the dice roll and current sum
                dice1, dice2 = roll_dice()
                dice_total = dice1 + dice2
                current_sum = 0

    # Clear the screen
    window.fill(WHITE)

    # Draw the numbers
    for i, num in enumerate(numbers):
        pygame.draw.rect(window, GREEN, (50 + i * 80, 250, 80, 80))
        text = font.render(str(num), True, BLACK)
        window.blit(text, (60 + i * 80, 260))

    # Draw the shut numbers
    for i, num in enumerate(shut_numbers):
        text = font.render(str(num), True, BLACK)
        window.blit(text, (60 + i * 80, 360))

    # Draw the dice
    dice_text = font.render(f"Dice: {dice1} + {dice2} = {dice_total}", True, BLACK)
    window.blit(dice_text, (50, 50))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
