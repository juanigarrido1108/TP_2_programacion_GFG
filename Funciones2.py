import random
from Constantes import *
import pygame
import json
import copy

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#GENERAL
def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

#GENERAL
def reiniciar_estadisticas(datos_juego:dict) -> None:
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = 30

#GENERAL
def verificar_respuesta(datos_juego:dict,pregunta:dict,respuesta:int) -> bool:
    if respuesta == pregunta["respuesta_correcta"]:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
    else:
        if datos_juego["puntuacion"] > 0:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        retorno = False 

        
    return retorno

def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    elemento_juego["rectangulo"] = elemento_juego["superficie"].get_rect()
    elemento_juego["rectangulo"].x = pos_x
    elemento_juego["rectangulo"].y = pos_y
    
    return elemento_juego

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int) -> None:
    elemento_juego["superficie"] =  pygame.transform.scale(pygame.image.load(textura),(ancho,alto))
    
def obtener_respuesta_click(boton_respuesta_uno:dict,boton_respuesta_dos:dict,boton_respuesta_tres:dict,boton_respuesta_cuatro:dict,pos_click:tuple):
    lista_aux = [boton_respuesta_uno["rectangulo"],boton_respuesta_dos["rectangulo"],boton_respuesta_tres["rectangulo"], boton_respuesta_cuatro["rectangulo"]]
    respuesta = None
    
    for i in range(len(lista_aux)):
        if lista_aux[i].collidepoint(pos_click):
            respuesta = i + 1
    
    return respuesta

def cambiar_pregunta(lista_preguntas:list,indice:int,caja_pregunta:dict,boton_respuesta_uno:dict,boton_respuesta_dos:dict,boton_respuesta_tres:dict,boton_respuesta_cuatro:dict) -> dict:
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(caja_pregunta,"textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA)
    limpiar_superficie(boton_respuesta_uno,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_dos,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_tres,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA)
    limpiar_superficie(boton_respuesta_cuatro,"textura_respuesta.jpg",ANCHO_BOTON_PREGUNTA,ALTO_BOTON_PREGUNTA) 

    return pregunta_actual

def crear_botones_menu() -> list:
    lista_botones = []
    pos_y = 135

    for i in range(4):
        boton = crear_elemento_juego("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,570,pos_y)
        pos_y += 130
        lista_botones.append(boton)
        
    return lista_botones


def guardar_puntuacion(datos: list)-> None:
   with open("partidas.json", 'w') as partidas:
    json.dump(datos,partidas, indent = 4)


def limpiar_string(texto:str) -> str:
    return ""






def ordenar_top(partidas:list)-> list:
    lista_ordenada = sorted(partidas, key=lambda x: x["puntuacion"], reverse=True)
    top_diez = lista_ordenada[0:10]

    return top_diez
 
