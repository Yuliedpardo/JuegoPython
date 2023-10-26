import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

def iniciar_carrera():

    # Configuración de la pantalla
    ancho = 400
    alto = 700
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption('Juego de Carreras')

    # Colores
    BLANCO = (255, 255, 255)

    # Música de fondo
    pygame.mixer.music.load('sonido/carreras.mp3')
    pygame.mixer.music.play(-1)  # Reproduce la música infinitamente
    pygame.mixer.music.set_volume(0.2)  # Volumen

    # Cargar la imagen de fondo
    fondo = pygame.image.load("images/pista.jpg")
    fondo = pygame.transform.scale(fondo, (ancho, alto))

    # Cargar imágenes
    imagen_jugador = pygame.image.load('images/carroP.png')  # Ajusta la ruta según tu imagen
    imagen_jugador = pygame.transform.scale(imagen_jugador, (50, 100))

    imagen_obstaculo = pygame.image.load('images/carroE.png')  # Ajusta la ruta según tu imagen
    imagen_obstaculo = pygame.transform.scale(imagen_obstaculo, (50, 100))

    # Jugador
    ancho_jugador = 50
    alto_jugador = 50
    x_jugador = (ancho - ancho_jugador) // 2
    y_jugador = alto - alto_jugador - 50
    velocidad_jugador = 5

    # Obstáculos
    ancho_obstaculo = 50
    alto_obstaculo = 50
    velocidad_obstaculo = 5
    obstaculos = []

    # Fuente para mostrar el puntaje
    fuente = pygame.font.Font(None, 36)

    # Reloj para controlar la velocidad de actualización
    reloj = pygame.time.Clock()

    # Tiempo inicial (en milisegundos)
    tiempo_inicio = pygame.time.get_ticks()

    # Función para dibujar al jugador en la pantalla
    def dibujar_jugador(x, y):
        pantalla.blit(imagen_jugador, (x, y))

    # Función para dibujar los obstáculos en la pantalla
    def dibujar_obstaculos(obstaculos):
        for obstaculo in obstaculos:
            pantalla.blit(imagen_obstaculo, obstaculo)

    # Ciclo principal del juego
    ejecutando = True

    # Función para mostrar el puntaje en la pantalla
    def mostrar_puntaje(puntaje):
        texto_puntaje = fuente.render("Puntaje: " + str(puntaje), True, BLANCO)
        pantalla.blit(texto_puntaje, (10, 10))

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas = pygame.key.get_pressed()

        # Actualizar el tiempo y el puntaje
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - tiempo_inicio) / 1000
        puntaje = int(tiempo_transcurrido)

        # Movimiento del jugador
        if teclas[pygame.K_LEFT] and x_jugador - velocidad_jugador > 0:
            x_jugador -= velocidad_jugador
        if teclas[pygame.K_RIGHT] and x_jugador + velocidad_jugador < ancho - ancho_jugador:
            x_jugador += velocidad_jugador

        # Generar obstáculos
        if random.randint(1, 600) < 10:  # Probabilidad de generar un obstáculo
            x_obstaculo = random.randint(0, ancho - ancho_obstaculo)
            y_obstaculo = -alto_obstaculo
            obstaculos.append(pygame.Rect(x_obstaculo, y_obstaculo, ancho_obstaculo, alto_obstaculo))

        # Mover obstáculos
        for obstaculo in obstaculos:
            obstaculo.y += velocidad_obstaculo
            if obstaculo.y > alto:
                obstaculos.remove(obstaculo)

        # Colisión con obstáculos
        for obstaculo in obstaculos:
            if pygame.Rect(x_jugador, y_jugador, ancho_jugador, alto_jugador).colliderect(obstaculo):
                print("Game Over")
                ejecutando = False

        # Limpiar la pantalla
        pantalla.blit(fondo, (0, 0))

        # Dibujar al jugador y los obstáculos
        dibujar_jugador(x_jugador, y_jugador)
        dibujar_obstaculos(obstaculos)

        # Mostrar el puntaje
        mostrar_puntaje(puntaje)

        # Actualizar la pantalla
        pygame.display.update()
        reloj.tick(60)

    # Salir del juego
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_carrera()
