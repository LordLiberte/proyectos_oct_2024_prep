import pygame
import carlosgame

pygame.init() # inicializa pygame motor
screen = pygame.display.set_mode((100,100))  # establcece tamaño pantalla
running = True

width = screen.get_width()
height = screen.get_height()

# Cargar personaje
player = carlosgame.GameObject("player", width/2, height/2)
player2 = carlosgame.GameObject("Player2", width/3, height/3)

# Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == "w":
                print("Subir player")
                if player.get_rect().top > 0:
                    player.mover_arriba()
                        
            if event.unicode == "d":
                print("Derecha player")
                if player.get_rect().right < width:
                    player.mover_derecha()
                    
            if event.unicode == "a":
                print("Izquierda player")
                if player.get_rect().left > 0:
                    player.mover_izquierda()
                    
            if event.unicode == "s":
                print("Abajo player")
                if player.get_rect().bottom < height:
                    player.mover_abajo()
                
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill([188,170,164])
    screen.blit(player.get_imagen(), player.get_rect())
    screen.blit(player2.get_imagen(), player2.get_rect())
    
    pygame.display.flip()


pygame.quit()