import pygame
from carlosgame import *
import random

pygame.init()  # inicializa pygame motor
screen = pygame.display.set_mode((1280, 720))  # establece tamaño pantalla
running = True
pantalla = [1280, 720]

width = screen.get_width()
height = screen.get_height()

# Crear GameObjects
game_objects_list = []

# Cargar personaje
player = Personaje("player", width / 2, height / 2)
# Añadir GameObject a la lista
game_objects_list.append(player)

# Añadir numero de rocas
for i in range(4):
    while True:
        rock = GameObject(f"rock{i}", random.randint(15, width - 15), random.randint(15, height - 15))
        # Comprobar si el nuevo GameObject colisiona con TODOS los anteriores
        collision = False
        for j in range(len(game_objects_list)):
            if game_objects_list[j].get_rect().colliderect(rock.get_rect()):
                collision = True
                break
        if collision:
            break
    game_objects_list.append(rock)

player2 = GameObject("Player2", width / 3, height / 3)

# Control de movimiento
playerMove = False
keypress = ""

# Bucle principal
while running:
    for event in pygame.event.get():
        
        # Tecla apretada
        if event.type == pygame.KEYDOWN:
            playerMove = True  # Establece que el jugador se mueve
            
            if event.unicode == "w":  # Movimiento arriba
                print("Subir player")
                keypress = "w"
                        
            if event.unicode == "d":  # Movimiento derecha
                print("Derecha player")
                keypress = "d"
                    
            if event.unicode == "a":  # Movimiento izquierda
                print("Izquierda player")
                keypress = "a"
                    
            if event.unicode == "s":  # Movimiento abajo
                print("Abajo player")
                keypress = "s"
        
        # Tecla levantada
        if event.type == pygame.KEYUP:
            playerMove = False  # Establece que el jugador se para
                
        if event.type == pygame.QUIT:
            running = False
    
    if playerMove:
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
        
        # Verificar colisiones
        for obj in game_objects_list:
            if obj != player and player.get_rect().colliderect(obj.get_rect()):
                print(f"Colisión con {obj.tag}")
            
    screen.fill([188, 170, 164])
    
    # Generar rocas
    for rock in game_objects_list:
        screen.blit(rock.get_imagen(), rock.get_rect())
    # Generar personaje
    screen.blit(player.get_imagen(), player.get_rect())
    screen.blit(player2.get_imagen(), player2.get_rect())
    
    pygame.display.flip()

pygame.quit()