<<<<<<< HEAD
import pygame
from Constantes import *
from Funciones import *

pygame.init()
# lista_botones = crear_botones_menu("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,350,125,4)
lista_botones = crear_botones_menu("textura_volver.jpg",ANCHO_BOTON,ALTO_BOTON,325,135,4)
fondo_menu = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)  
lista_nombres_botones = ["JUGAR","AJUSTES","RANKINGS","SALIR"]

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    #Manejar los eventos
    retorno = manejar_eventos(cola_eventos)
    #Dibujamos los cambios en pantalla
    dibujar_pantalla(pantalla)

    return retorno

def manejar_eventos(cola_eventos:list[pygame.event.Event]):
    retorno = "menu"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #SOLO CLICK IZQUIERDO
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        CLICK_SONIDO.play()
                        if i == 0:
                            retorno = "juego"
                        elif i == 1:
                            retorno = "ajustes"
                        elif i == 2:
                            retorno = "rankings"
                        elif i == 3:
                            retorno = "salir"
    
    return retorno

def dibujar_pantalla(pantalla:pygame.Surface) -> None:
    pantalla.blit(fondo_menu,(0,0))
    for i in range(len(lista_botones)):
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
        mostrar_texto(lista_botones[i]["superficie"],lista_nombres_botones[i],(62,10),FUENTE_MENU,COLOR_NEGRO)
=======
import pygame
from Constantes import *
from Funciones import *

pygame.init()
lista_botones = crear_botones_menu("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,115,125,4)
fondo_menu = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)  
lista_nombres_botones = ["JUGAR","AJUSTES","RANKINGS","SALIR"]

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    #Manejar los eventos
    retorno = manejar_eventos(cola_eventos)
    #Dibujamos los cambios en pantalla
    dibujar_pantalla(pantalla)

    return retorno

def manejar_eventos(cola_eventos:list[pygame.event.Event]):
    retorno = "menu"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #SOLO CLICK IZQUIERDO
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        CLICK_SONIDO.play()
                        if i == 0:
                            retorno = "juego"
                        elif i == 1:
                            retorno = "ajustes"
                        elif i == 2:
                            retorno = "rankings"
                        elif i == 3:
                            retorno = "salir"
    
    return retorno

def dibujar_pantalla(pantalla:pygame.Surface) -> None:
    pantalla.blit(fondo_menu,(0,0))
    for i in range(len(lista_botones)):
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
        mostrar_texto(lista_botones[i]["superficie"],lista_nombres_botones[i],(80,10),FUENTE_TEXTO,COLOR_NEGRO)
>>>>>>> a6773ec83242dec1242961dbbf327379917bae6d
