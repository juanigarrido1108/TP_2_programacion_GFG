import pygame
from Constantes import *
from Funciones import *

from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *

pygame.init()

pygame.display.set_caption("GRUPO GFG\nPREGUNTADOS")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego ={"puntuacion":0,"vidas":3,"nombre":"","tiempo_restante":TIEMPO_JUEGO,"volumen_musica":0,"indice":0}
ventana_actual = "menu"
bandera_juego = False
mezclar_lista(lista_preguntas)
#Deberia venir del json
lista_rankings = []

porcentaje_volumen = datos_juego["volumen_musica"] / 100
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(porcentaje_volumen)
pygame.mixer.music.play(-1)

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual = "salir"
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            #MUSICA SOLO EN EL JUEGO
            # porcentaje_volumen = datos_juego["volumen_musica"] / 100
            # pygame.mixer.music.load("musica.mp3")
            # pygame.mixer.music.set_volume(porcentaje_volumen)
            # pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego,lista_preguntas)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
        
        #MUSICA EN TODO EL JUEGO
        porcentaje_volumen = datos_juego["volumen_musica"] / 100
        pygame.mixer.music.set_volume(porcentaje_volumen)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,lista_rankings)
    elif ventana_actual == "salir":
        print("SALIENDO DE LA APLICACION")
        corriendo = False
    elif ventana_actual == "terminado":
        if bandera_juego == True:
            #MUSICA EN SOLO EL JUEGO
            pygame.mixer.music.stop()
            bandera_juego = False
        
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego,lista_rankings)
    
    pygame.display.flip()

pygame.quit()