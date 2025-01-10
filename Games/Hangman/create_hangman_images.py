# pip install pillow
from PIL import Image, ImageDraw

def create_hangman_images():
    width, height = 300, 400
    for i in range(7):
        img = Image.new("RGB", (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw the gallows
        draw.line((50, 350, 250, 350), fill=(0, 0, 0), width=5)  # Base
        draw.line((150, 350, 150, 50), fill=(0, 0, 0), width=5)  # Pole
        draw.line((150, 50, 200, 50), fill=(0, 0, 0), width=5)   # Top
        draw.line((200, 50, 200, 100), fill=(0, 0, 0), width=5)  # Rope

        # Draw parts of the hangman based on the stage
        if i > 0:  # Head
            draw.ellipse((175, 100, 225, 150), outline=(255, 0, 0), width=5)
        if i > 1:  # Body
            draw.line((200, 150, 200, 250), fill=(255, 0, 0), width=5)
        if i > 2:  # Left Arm
            draw.line((200, 180, 170, 220), fill=(255, 0, 0), width=5)
        if i > 3:  # Right Arm
            draw.line((200, 180, 230, 220), fill=(255, 0, 0), width=5)
        if i > 4:  # Left Leg
            draw.line((200, 250, 170, 320), fill=(255, 0, 0), width=5)
        if i > 5:  # Right Leg
            draw.line((200, 250, 230, 320), fill=(255, 0, 0), width=5)

        img.save(f"hangman{i}.png")

create_hangman_images()
