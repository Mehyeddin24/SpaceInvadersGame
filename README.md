# Space Invaders

Space Invaders is an action based spaceship game where you have shoot 30 enemies!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```

## Usage

```python
import pygame

# create the window with given values
screen = pygame.display.set_mode((800, 600))

# name of the window
pygame.display.set_caption("Space Invaders")

# print the image on the screen
bulletImage = pygame.image.load("bullet.png")

# change the font of the text / size 
font = pygame.font.Font('mehyeddinistfont.ttf', 50)
```

## Why Pygame?

Why do we use pygame instead of other gaming engines? The answer is simple, because other gaming engines make you a worse developer than the people who made these basic and simple games.
