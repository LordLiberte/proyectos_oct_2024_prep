import pygame
import carlosgame

pygame.init() # inicializa pygame motor
screen = pygame.display.set_mode((1280,720))  # establcece tamaño pantalla
running = True

width = screen.get_width()
height = screen.get_height()

# Cargar personaje
player = carlosgame.GameObject("player", width/2, height/2)

# Bucle principal
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == "w":
                print("Subir player")
                player.mover_arriba()
                        
            if event.unicode == "d":
                print("Derecha player")
                player.mover_derecha()
                    
            if event.unicode == "a":
                print("Izquierda player")
                player.mover_izquierda()
                    
            if event.unicode == "s":
                print("Abajo player")
                player.mover_abajo()
                
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill([188,170,164])
    screen.blit(player.get_imagen(), player.get_rect())
    
    pygame.display.flip()


pygame.quit()