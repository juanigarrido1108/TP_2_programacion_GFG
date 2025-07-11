import random
import json
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

    for i in range(4):
        respuesta = crear_elemento_juego(textura,ancho,alto,pos_x,pos_y)
        pos_y += 90
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

def actualizar_ranking_eficiente(datos_juego:dict, datos_cargados:dict) -> dict:
    
    # Actualiza el ranking de manera eficiente:
    # Agrega el nuevo registro
    # Ordena por puntuación (descendente)
    # Mantiene solo los mejores 100 registros (opcional)
    # Guarda en el archivo JSON
    
    # Determinar la estructura del JSON y extraer la lista
    # Extraer la lista del JSON con estructura fija {"ranking": [...]}
    if isinstance(datos_cargados, dict) and "ranking" in datos_cargados:
        lista_rankings = datos_cargados["ranking"]
    else:
        # Si no tiene la estructura esperada, crear lista vacía
        lista_rankings = []
        
    # Agregar el nuevo registro
    nuevo_registro = {
        "nombre": datos_juego["nombre"],
        "puntuacion": datos_juego["puntuacion"]
        }
    lista_rankings.append(nuevo_registro)
        
    # Ordenar por puntuación (de mayor a menor)
    lista_rankings.sort(key=lambda x: x["puntuacion"], reverse=True)
        
    # Mantiene solo los mejores 10 registros para optimizar
    lista_rankings = lista_rankings[:10]
        
    # Guardar en el archivo JSON manteniendo la estructura {"ranking": [...]}
    estructura_json = {"ranking": lista_rankings}
    with open("ranking.json", "w", encoding="utf-8") as archivo:
        json.dump(estructura_json, archivo, indent=2, ensure_ascii=False)
    
    return lista_rankings
