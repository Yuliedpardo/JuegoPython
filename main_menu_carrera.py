import pygame
import sys
from Carrera import iniciar_carrera
from instrucciones import start_instrucciones

pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 400
PANTALLA = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú")

# Cargar la imagen de fondo
fondo = pygame.image.load("images/menu_carrera.jpg")
fondo = pygame.transform.scale(fondo, (ancho, alto))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

PANTALLA.fill(NEGRO)

# Opciones del menú
menu_options = ["Jugar", "Instrucciones", "Salir"]

# Función para mostrar el menú
def show_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(len(menu_options)):
                    text = font.render(menu_options[i], True, NEGRO)
                    text_rect = text.get_rect(center=(ancho // 2, alto // 2 - len(menu_options) * text.get_height() // 2 + i * 50))
                    if text_rect.collidepoint(mouse_pos):
                        if i == 0: # Juego Carreras
                            iniciar_carrera()
                        elif i == 1: # Intsrucciones
                            start_instrucciones()
                        elif i == 2:
                            pygame.quit()
                            sys.exit()

        # Dibuja el fondo
        PANTALLA.blit(fondo, (0, 0))

        # Dibuja las opciones del menú
        for i in range(len(menu_options)):
            text = font.render(menu_options[i], True, NEGRO)
            posicion_y = alto // 2 - len(menu_options) * text.get_height() // 2 + i * 50
            PANTALLA.blit(text, (ancho // 2 - text.get_width() // 2, posicion_y))

        pygame.display.update()

# Mantener el Juego en Ejecucion
show_menu()
