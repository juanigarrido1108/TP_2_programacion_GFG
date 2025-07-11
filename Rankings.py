<<<<<<< HEAD
import pygame
import json
from Constantes import *
from Funciones import *


pygame.init()

boton_volver = crear_elemento_juego("textura_volver.jpg",100,40,10,10)
fondo_rankings = pygame.transform.scale(pygame.image.load("ranking.png"),PANTALLA)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.blit(fondo_rankings, (0, 0))
    pantalla.blit(boton_volver["superficie"], boton_volver["rectangulo"])
    mostrar_texto(boton_volver["superficie"], "VOLVER", (5, 5), FUENTE_TEXTO, COLOR_NEGRO)
    
    pos_y = 85
    
    try:
        with open("ranking.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            ranking_data = datos["ranking"]  # Extraer la lista
    except FileNotFoundError:
        ranking_data = []
    
    # Mostrar los datos del ranking
    for i in range(len(ranking_data)):
        jugador = ranking_data[i]
        texto = f"{jugador['posicion']}: {jugador['nombre']} - {jugador['puntuacion']} puntos"
        mostrar_texto(pantalla, texto, (130, pos_y), FUENTE_TEXTO, COLOR_NEGRO)
        pos_y += 35
    
    return retorno
    # retorno = "rankings"
    
    # for evento in cola_eventos:
    #     if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
    #         if boton_volver["rectangulo"].collidepoint(evento.pos):
    #             CLICK_SONIDO.play()
    #             retorno = "menu"
    
    # pantalla.blit(fondo_rankings,(0,0))
    # pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    # mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_TEXTO,COLOR_NEGRO)
    # pos_y = 85
    # # Mostrar los datos del ranking
    
    # for i in range(len(lista_rankings)):
    #     with open("ranking.json", "r", encoding="utf-8") as archivo:
    #         lista_rankings = json.load(archivo)
    #     texto = f"{lista_rankings[i]["posicion"]}: {lista_rankings[i]["nombre"]} - {lista_rankings[i]["puntuacion"]} puntos"
    #     mostrar_texto(pantalla,texto,(130,pos_y),FUENTE_TEXTO,COLOR_NEGRO)
    #     pos_y += 35
    
    # return retorno
=======
import pygame
from Constantes import *
from Funciones import *

pygame.init()

boton_volver = crear_elemento_juego("textura_respuesta.jpg",100,40,10,10)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    mostrar_texto(pantalla,f"ACA VA EL TOP 10",(150,200),FUENTE_VOLUMEN,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_BLANCO)

    return retorno
    
>>>>>>> a6773ec83242dec1242961dbbf327379917bae6d
