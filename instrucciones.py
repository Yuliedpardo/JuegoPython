import pygame
import sys

# Inicializar Pygame
pygame.init()

def start_instrucciones():

    # Configuración de la pantalla
    screen_width = 800
    screen_height = 600
    PANTALLA = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Juego de Arcade')

    # Colores
    NEGRO = (0, 0, 0)

    # Cargar la imagen de fondo
    fondo = pygame.image.load("images/menu_carrera.jpg")
    fondo = pygame.transform.scale(fondo, (800, 600))

    # Función para mostrar la pantalla de instrucciones
    def display_instructions():
        font = pygame.font.Font(None, 36)
        instruction_text1 = font.render("¡Bienvenido al juego de carreras!", True, NEGRO)
        instruction_text2 = font.render("Mueve el auto usando las flechas izq y der.", True, NEGRO)
        instruction_text3 = font.render("Evita que los autos rojos te choquen ", True, NEGRO)
        instruction_text4 = font.render("ve sumando puntaje con el tiempo transcurrido.", True, NEGRO)
        instruction_text5 = font.render("Presiona la opcion jugar para empezar el juego. ", True, NEGRO)

        # Dibuja el fondo
        PANTALLA.blit(fondo, (0, 0))
        PANTALLA.blit(instruction_text1, (120, 200))
        PANTALLA.blit(instruction_text2, (120, 250))
        PANTALLA.blit(instruction_text3, (120, 300))
        PANTALLA.blit(instruction_text4, (120, 350))
        PANTALLA.blit(instruction_text5, (120, 400))

    # Ciclo principal del juego
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Mostrar pantalla de instrucciones
        display_instructions()

        # Actualizar la pantalla
        pygame.display.update()

    # Salir del juego
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_instrucciones()
