import pygame
from Constantes import *
from Funciones import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *

pygame.init()

pygame.display.set_caption("arGeNTADOS")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)
corriendo = True
reloj = pygame.time.Clock()

datos_juego ={"puntuacion":0,"vidas":3,"nombre":"","tiempo_restante":TIEMPO_JUEGO,"volumen_musica":0,"volumen_efectos":0,"indice":0,"correctas_seguidas":0}
comodines = {"puntaje_doble":0,"pasar":0,"doble_chance":0}
banderas = {"puntaje_doble":True,"pasar":True,"doble_chance":True}
ventana_actual = "menu"
bandera_juego = False
bandera_musica = False

with open("ranking.json", "r", encoding="utf-8") as archivo:
    lista_rankings = json.load(archivo)
with open('Preguntas.json', 'r',encoding='utf-8') as archivo:
    lista_preguntas = json.load(archivo)
mezclar_lista(lista_preguntas)

porcentaje_volumen = datos_juego["volumen_musica"] / 100
pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.set_volume(porcentaje_volumen)
pygame.mixer.music.play(-1)
porcentaje_volumen_efectos = datos_juego["volumen_efectos"] / 100
CLICK_SONIDO.set_volume(porcentaje_volumen_efectos)
ERROR_SONIDO.set_volume(porcentaje_volumen_efectos)
COMODIN_SONIDO.set_volume(porcentaje_volumen_efectos)

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual = "salir"
    
    if ventana_actual == "menu":
        if bandera_musica == False:
            porcentaje_volumen = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load("musica.mp3")
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_musica = True
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            bandera_juego = True
            bandera_musica = False
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego,lista_preguntas,comodines,banderas)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
        porcentaje_volumen = datos_juego["volumen_musica"] / 100
        pygame.mixer.music.set_volume(porcentaje_volumen)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos,lista_rankings)
    elif ventana_actual == "salir":
        print("SALIENDO DE LA APLICACION")
        corriendo = False
    elif ventana_actual == "terminado":
        if bandera_juego == True:
            pygame.mixer.music.stop()
            bandera_juego = False
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego,comodines,banderas)
        if ventana_actual != "terminado":
            bandera_menu = False
    
    pygame.display.flip()

pygame.quit()