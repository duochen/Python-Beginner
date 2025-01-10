import pygame
import random

# Initialize PyGame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
FONT = pygame.font.Font(None, 40)
LETTER_FONT = pygame.font.Font(None, 60)

# Game variables
word_list = ["PYTHON", "PYGAME", "DEVELOPER", "CODING", "COMPUTER"]
word = random.choice(word_list)
guessed = []
max_attempts = 6
attempts = 0

# Button dimensions
RADIUS = 20
gap = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + gap) * 13) / 2)
starty = 450

for i in range(26):
    x = startx + gap * 2 + ((RADIUS * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + RADIUS * 2))
    letters.append([x, y, chr(65 + i), True])

# Load images
images = []
for i in range(max_attempts + 1):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# Draw the game
def draw():
    screen.fill(WHITE)

    # Draw title
    title_text = FONT.render("Hangman Game", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_text = LETTER_FONT.render(display_word, True, BLACK)
    screen.blit(word_text, (400 - word_text.get_width() // 2, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, BLUE, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, BLACK)
            screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    # Draw hangman
    screen.blit(images[attempts], (150, 100))
    pygame.display.update()

# Display message
def display_message(message):
    pygame.time.delay(1000)
    screen.fill(WHITE)
    text = FONT.render(message, True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global attempts
    run = True

    while run:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = ((x - m_x) ** 2 + (y - m_y) ** 2) ** 0.5
                        if distance < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                attempts += 1

        # Check for win or lose
        won = all([letter in guessed for letter in word])
        if won:
            display_message("You Won!")
            break

        if attempts == max_attempts:
            display_message(f"You Lost! The word was {word}.")
            break

    pygame.quit()

if __name__ == "__main__":
    main()
