'''
The text in draw_text(text) should be string or bites.
If a message has numerical characters,
than it should be converted to a string
 str(message)
 For pygame.draw check :
 https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
'''
import pygame
import os
import datetime

# Define some colors


def draw_text(text):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Times New Roman', 50, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    text_new = font.render(text, True, RED)
    return text_new

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

# Set the WIDTH and the HEIGHT for the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = '20,50'
WIDTH = 1200
HEIGHT = 700
size = ( WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Template for Pygame Programs')

LETTER_BOX = (50, 550)
WIDTH_LETTER_BOX = 50
HEIGHT_LETTER_BOX = 50

LETTERS = [['A','B','C','D','E','F','G','H','I','J','K','L','M'],
           ['N','O','P','Q','R','S','T','U','V','W', 'X', 'Y','Z']]
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(2):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(13):
        grid[row].append(0)  # Append a cell
# Loop until the user clicks the close button
done = False
# Use how fast the screen updates
clock = pygame.time.Clock()



#--------------Main Program Loop -------------
while not done:
    #---Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] >= 50 and pos[0]<= 700 and pos[1] >= 550 and pos[1] <= 650 :

                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // WIDTH_LETTER_BOX - 1
                row = pos[1] // HEIGHT_LETTER_BOX - 11
                # # Set that location to one
                # grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column, 'letter is ', LETTERS[row][column])

    # Game Logic should go here
    something = datetime.datetime.now()
    something.strftime("%Y-%m-%d  %H:%M:%S")



    # Screen clearing goes here

    #Here we clear the screen to white. Don't put other drawing commands
    #  above this , or they will be erased with this command

    #If you want a background image, replace this clear with
    # blit' ing the background image.
    screen.fill(WHITE)

    #--------Drawing code should go here
    rect1 = pygame.draw.rect(screen, YELLOW, [200,200, 400, 100],5)
    rect2 = pygame.draw.rect(screen, RED, [50, 550, 650,100],1)



    #---------Update thje screen with what we have drawn
    # ---------Put the image of the text on the screen at 250 x250

    screen.blit(draw_text(str(something)), [250, 250])
    # screen.blit(draw_text('ABCDEFGHIJKLM'), [50, 550])
    # screen.blit(draw_text('NOPQRSTUVWXYZ'), [50,600])
    for row in range(2):
        for column in range(13):
            screen.blit(draw_text(LETTERS[row][column]),[ 50 +50*column, 550 + 50*row])
    pygame.display.flip()

    #------Limit 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()