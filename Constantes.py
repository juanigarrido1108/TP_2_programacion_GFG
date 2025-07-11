import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
ANCHO = 600
ALTO = 600
PANTALLA = (ANCHO,ALTO)
FPS = 30

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

ANCHO_PREGUNTA = 350
ALTO_PREGUNTA = 150
ANCHO_BOTON = 250
ALTO_BOTON = 60
ANCHO_CUADRO = 250
ALTO_CUADRO = 50

TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
CLICK_SONIDO = pygame.mixer.Sound("click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("error.mp3")
COMODIN_SONIDO = pygame.mixer.Sound("comodin_sonido.mp3")
ERROR = pygame.mixer.Sound("ERROR_PREGUNTA.mp3")
ACIERTO = pygame.mixer.Sound("acierto.mp3")

MUSICA_TERMINADO = pygame.mixer.Sound("musica_terminado.mp3")

FUENTE_PREGUNTA = pygame.font.SysFont("Arial",28,True)
FUENTE_MENU = pygame.font.SysFont("Courier New",28,True)
FUENTE_RESPUESTA = pygame.font.SysFont("Arial",20,True)
FUENTE_TEXTO = pygame.font.SysFont("Courier New",25,True)
FUENTE_VOLUMEN = pygame.font.SysFont("Arial",50,True)
FUENTE_CUADRO = pygame.font.SysFont("Arial",40,True)

BOTON_JUGAR = 0

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
TIEMPO_JUEGO = 30