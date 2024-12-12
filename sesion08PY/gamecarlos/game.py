import pygame
import carlosgame

pygame.init() # inicializa pygame motor
screen = pygame.display.set_mode((1280, 720))  # establcece tamaño pantalla
running = True

width = screen.get_width()
height = screen.get_height()

# Cargar personaje
player = carlosgame.GameObject("player", width/2, height/2)
player2 = carlosgame.GameObject("Player2", width/3, height/3)
playerMove = False
keypress = ""

# Bucle principal
while running:
    for event in pygame.event.get():
        
        # Tecla apretada
        if event.type == pygame.KEYDOWN:
        
            playerMove = True  # Establece que el jugador se mueve
            
            if event.unicode == "w":
                print("Subir player")
                keypress = "w"
                        
            if event.unicode == "d":
                print("Derecha player")
                keypress = "d"
                    
            if event.unicode == "a":
                print("Izquierda player")
                keypress = "a"
                    
            if event.unicode == "s":
                print("Abajo player")
                keypress = "s"
            
            if event.unicode == "wd" or event.unicode == "dw":
                keypress = "wd"
        
        # Tecla levantada
        if event.type == pygame.KEYUP:
            playerMove = False  # Establece que el jugador se para
                
        if event.type == pygame.QUIT:
            running = False
    
    if playerMove == True:
        if keypress == "w":
            if player.get_rect().top > 0:
                player.mover_arriba()
        elif keypress == "s":
            if player.get_rect().bottom < height:
                player.mover_abajo()
        elif keypress == "d":
            if player.get_rect().right < width:
                player.mover_derecha()
        elif keypress == "a":
            if player.get_rect().left > 0:
                    player.mover_izquierda()
            
            
    
    screen.fill([188,170,164])
    screen.blit(player.get_imagen(), player.get_rect())
    screen.blit(player2.get_imagen(), player2.get_rect())
    
    pygame.display.flip()


pygame.quit()