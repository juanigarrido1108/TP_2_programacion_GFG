<<<<<<< HEAD
import pygame
import json
from Constantes import *
from Funciones import *


pygame.init()

cuadro_texto = crear_elemento_juego("textura_terminado.jpg",ANCHO_CUADRO,ALTO_CUADRO,120,150)
fondo_terminado = pygame.transform.scale(pygame.image.load("terminado.jpg"),PANTALLA)
boton_volver_terminado = crear_elemento_juego("textura_volver.jpg",100,40,200,500)

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_rankings:list) -> str:
    retorno = "terminado"
    
    porcentaje_volumen = datos_juego["volumen_musica"] / 100
    MUSICA_TERMINADO.set_volume(porcentaje_volumen)
    MUSICA_TERMINADO.play()

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver_terminado["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
                MUSICA_TERMINADO.stop()
                
        
        if evento.type == pygame.KEYDOWN:
            limpiar_superficie(cuadro_texto,"textura_terminado.jpg",ANCHO_CUADRO,ALTO_CUADRO)
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods()
            
                        
            if tecla_presionada == "backspace":
                datos_juego["nombre"] = datos_juego["nombre"][0:len(datos_juego["nombre"]) - 1]
            elif tecla_presionada == "space":
                datos_juego["nombre"] += " "
            elif len(tecla_presionada) == 1: 
                #Manipula el bloc mayus y el shift izq/der
                if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2 :
                    datos_juego["nombre"] += tecla_presionada.upper()
                else:
                    datos_juego["nombre"] += tecla_presionada
            elif tecla_presionada == "return":
                actualizar_ranking_eficiente(datos_juego,lista_rankings)
                reiniciar_estadisticas(datos_juego)
                retorno = "menu"
                MUSICA_TERMINADO.stop()
                                               
    pantalla.blit(fondo_terminado,(0,0))
    pantalla.blit(cuadro_texto["superficie"],cuadro_texto["rectangulo"])
    pantalla.blit(boton_volver_terminado["superficie"],boton_volver_terminado["rectangulo"])
    
    mostrar_texto(pantalla,f"PUNTUACIÓN\n{datos_juego["puntuacion"]}",(425,85),FUENTE_TEXTO,COLOR_ROJO)
    mostrar_texto(boton_volver_terminado["superficie"],"VOLVER",(5,5),FUENTE_TEXTO,COLOR_NEGRO)
    
    if datos_juego["nombre"] != "":
        limpiar_superficie(cuadro_texto,"textura_terminado.jpg",ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],datos_juego["nombre"],(10,0),FUENTE_CUADRO,COLOR_ROJO)

        if random.randint(1,2) == 1:
            mostrar_texto(cuadro_texto["superficie"],f"{datos_juego["nombre"]}|",(10,0),FUENTE_CUADRO,COLOR_ROJO)

    else:
        limpiar_superficie(cuadro_texto,"textura_terminado.jpg",ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],"INGRESE SU NOMBRE",(10,10),FUENTE_TEXTO,"#8A7A7A")
        
    return retorno
=======
import pygame
from Constantes import *
from Funciones import *

pygame.init()
cuadro_texto = crear_elemento_juego("textura_respuesta.jpg",ANCHO_CUADRO,ALTO_CUADRO,200,200)

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_rankings:list) -> str:
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            limpiar_superficie(cuadro_texto,"textura_respuesta.jpg",ANCHO_CUADRO,ALTO_CUADRO)
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods()
            
                        
            if tecla_presionada == "backspace":
                datos_juego["nombre"] = datos_juego["nombre"][0:len(datos_juego["nombre"]) - 1]
            elif tecla_presionada == "space":
                datos_juego["nombre"] += " "
            elif len(tecla_presionada) == 1: 
                #Manipula el bloc mayus y el shift izq/der
                if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2 :
                    datos_juego["nombre"] += tecla_presionada.upper()
                else:
                    datos_juego["nombre"] += tecla_presionada
            elif tecla_presionada == "return":
                #Guarda la puntuacion al ranking
                #lista_rankings.append(puntuacion)
                #Actualizo el json
                reiniciar_estadisticas(datos_juego)
                retorno = "menu"
                
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(cuadro_texto["superficie"],cuadro_texto["rectangulo"])
    
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego["puntuacion"]} puntos",(250,100),FUENTE_PREGUNTA)
    
    if datos_juego["nombre"] != "":
        limpiar_superficie(cuadro_texto,"textura_respuesta.jpg",ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],datos_juego["nombre"],(10,0),FUENTE_CUADRO,COLOR_BLANCO)

        if random.randint(1,2) == 1:
            mostrar_texto(cuadro_texto["superficie"],f"{datos_juego["nombre"]}|",(10,0),FUENTE_CUADRO,COLOR_BLANCO)

    else:
        limpiar_superficie(cuadro_texto,"textura_respuesta.jpg",ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],"INGRESE SU NOMBRE",(10,10),FUENTE_RESPUESTA,"#8A7A7A")
        
    return retorno


>>>>>>> a6773ec83242dec1242961dbbf327379917bae6d
