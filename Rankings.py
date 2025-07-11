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
    with open("ranking.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    if "ranking" in datos:
        ranking = datos["ranking"]
        for i in range(min(10, len(ranking))):  # min() para evitar errores si hay menos de 10 elementos
            texto = f"{i+1}: {ranking[i]['nombre']} - {ranking[i]['puntuacion']} puntos"
            mostrar_texto(pantalla, texto, (110, pos_y), FUENTE_TEXTO, COLOR_NEGRO)
            pos_y += 35
    # with open("ranking.json", "r", encoding="utf-8") as archivo:
    #     datos = json.load(archivo)
    #     # ranking_nombre = datos["ranking"]  # Extraer la lista
    #     # ranking_puntuacion = datos ["ranking"]

    
    # # Mostrar los datos del ranking
    # for i in range(10):
    #     texto = f"{i}: {datos[i]["nombre"]} - {datos[i]["puntuacion"]} puntos"
    #     mostrar_texto(pantalla, texto, (130, pos_y), FUENTE_TEXTO, COLOR_NEGRO)
    #     pos_y += 35
    
    return retorno