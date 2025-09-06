import pygame
#Password checker
def passwordCheck(password):
    index = int(0)
    strength = 0

    for x in password:
        asciiValue = ord(password[index])
        index+=1
        if asciiValue == 32:
            print("Spaces are not allowed")
        elif 97 <= asciiValue <123:
            strength+=1
        elif 65<= asciiValue <91:
            strength +=1.5
        elif 48 <= asciiValue < 58:
            strength +=2
        else:
            strength +=3
    return strength
#GUI element

#Window parameters
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Password strength checker")

#text paramaters
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Password strength checker", True, "white")
textRect = text.get_rect()
textRect.center = (640,100)

passwordTxt = font.render("Password:", True, "white")
passwordTxtRect = passwordTxt.get_rect()
passwordTxtRect.midright = (450, 360)

usrPassword = ''
inputRect = pygame.Rect(475,340,140,32)
colour = "white"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                usrPassword = usrPassword[:-1]
            else:
                usrPassword += event.unicode


    screen.fill("grey")
    screen.blit(text, textRect)
    screen.blit(passwordTxt,passwordTxtRect)
    pygame.draw.rect(screen, colour, inputRect)
    textSurface = font.render(usrPassword, True, (0,0,0))
    screen.blit(textSurface, inputRect)
    inputRect.w = max(100, textSurface.get_width()+10)
    strength = passwordCheck(usrPassword)

    if strength == 0:
        colour = "white"
    elif strength < 6:
        colour = (247, 97, 84)
    elif 6 <= strength <11:
        colour =(247, 160, 84)
    else:
        colour = (133, 249, 109)

    pygame.display.flip()

    clock.tick(60)

