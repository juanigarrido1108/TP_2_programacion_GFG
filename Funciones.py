import random
from Constantes import *
import pygame

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

def crear_elemento_juego(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> dict:
    elemento_juego = {}
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto)) 
    elemento_juego["rectangulo"] = pygame.rect.Rect(pos_x,pos_y,ancho,alto)
    
    return elemento_juego

def crear_respuestas_preguntados(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int) -> list:
    lista_respuestas = []

    for i in range(3):
        respuesta = crear_elemento_juego(textura,ancho,alto,pos_x,pos_y)
        pos_y += 80
        lista_respuestas.append(respuesta)
        
    return lista_respuestas

def limpiar_superficie(elemento_juego:dict,textura:str,ancho:int,alto:int) -> None:
    elemento_juego["superficie"] = pygame.transform.scale(pygame.image.load(textura),(ancho,alto)) 
    
def reiniciar_estadisticas(datos_juego:dict) -> None:
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["nombre"] = ""
    datos_juego["tiempo_restante"] = TIEMPO_JUEGO

#GENERAL (PUEDE SERVIRME EN PYGAME) 
def verificar_respuesta(datos_juego:dict,pregunta:dict,respuesta:int) -> bool:
    if respuesta == pregunta["respuesta_correcta"]:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
    else:
        datos_juego["vidas"] -= 1
        datos_juego["puntuacion"] -= PUNTUACION_ERROR
        retorno = False    
        
    return retorno

def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

def pasar_pregunta(lista_preguntas:list,indice:int,cuadro_pregunta:dict,lista_respuestas:list) -> dict:
    pregunta_actual = lista_preguntas[indice]
    limpiar_superficie(cuadro_pregunta,"textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA)
    
    for i in range(len(lista_respuestas)):
        limpiar_superficie(lista_respuestas[i],"textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON)
        
    return pregunta_actual

def crear_botones_menu(textura:str,ancho:int,alto:int,pos_x:int,pos_y:int,cantidad_botones:int) -> list:
    lista_botones = []

    for i in range(cantidad_botones):
        boton = crear_elemento_juego(textura,ancho,alto,pos_x,pos_y)
        pos_y += 80
        lista_botones.append(boton)
        
    return lista_botones