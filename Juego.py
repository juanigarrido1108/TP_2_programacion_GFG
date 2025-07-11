import pygame
import json
from Constantes import *
from Funciones import *


pygame.init()

fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo_juego.jpg"),PANTALLA)
cuadro_pregunta = crear_elemento_juego("textura_pregunta.jpg",ANCHO_PREGUNTA,ALTO_PREGUNTA,120,80)
lista_respuestas = crear_respuestas_preguntados("textura_respuesta.jpg",ANCHO_BOTON,ALTO_BOTON,175,245)
boton_volver_terminado = crear_elemento_juego("textura_volver.jpg",100,40,20,500)
boton_puntaje_doble = crear_elemento_juego("puntaje_doble.png",100,40,20,395)
boton_pasar = crear_elemento_juego("pasar.png",100,40,20,275)
boton_doble_chance = crear_elemento_juego("doble.png",100,40,20,165)
evento_tiempo = pygame.USEREVENT 
pygame.time.set_timer(evento_tiempo,1000)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_preguntas:list,comodines:dict,banderas:dict) -> str:
    retorno = "juego"
    pregunta_actual = lista_preguntas[datos_juego["indice"]]
    if datos_juego["vidas"] == 0 or datos_juego["tiempo_restante"] == 0:
        print("GAME OVER")
        retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # CLICK_SONIDO.play()
            if evento.button == 1:
                for i in range(len(lista_respuestas)):
                    if boton_volver_terminado["rectangulo"].collidepoint(evento.pos):
                        reiniciar_estadisticas(datos_juego)
                        banderas["puntaje_doble"] = True
                        banderas["pasar"] = True
                        banderas["doble_chance"] = True
                        comodines["puntaje_doble"] = 0
                        comodines["pasar"] = 0
                        comodines["doble_chance"] = 0
                        retorno = "menu"
                    elif boton_puntaje_doble["rectangulo"].collidepoint(evento.pos):
                        if banderas["puntaje_doble"] == True:
                            banderas["puntaje_doble"] = False
                            comodines["puntaje_doble"] = 1
                            COMODIN_SONIDO.play()
                    elif boton_pasar["rectangulo"].collidepoint(evento.pos):
                        if comodines["pasar"] == 0:
                            COMODIN_SONIDO.play()
                            datos_juego["indice"] += 1
                            if datos_juego["indice"] >= len(lista_preguntas):
                                datos_juego["indice"] = 0
                            mezclar_lista(lista_preguntas)
                            pregunta_actual = pasar_pregunta(lista_preguntas,datos_juego["indice"],cuadro_pregunta,lista_respuestas)
                            comodines["pasar"] = 1
                            banderas["pasar"] = False
                    elif boton_doble_chance["rectangulo"].collidepoint(evento.pos):
                        if comodines["doble_chance"] == 0:
                            COMODIN_SONIDO.play()
                            comodines["doble_chance"] = 1
                            banderas["doble_chance"] = False                           
                    elif lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                        respuesta = (i + 1)
                        if verificar_respuesta(datos_juego,pregunta_actual,respuesta) == True:
                            CLICK_SONIDO.play() #cambiar sonido correcto
                            datos_juego["correctas_seguidas"] += 1
                            if datos_juego["correctas_seguidas"] >= 5:
                                datos_juego["vidas"] += 1
                                datos_juego["tiempo_restante"] += 7
                                datos_juego["correctas_seguidas"] = 0
                            if comodines["puntaje_doble"] == 1:
                                datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                        else:
                            if comodines["doble_chance"] == 1:
                                comodines["doble_chance"] = 0
                                banderas["doble_chance"] = False
                                datos_juego["correctas_seguidas"] = 0 
                                ERROR_SONIDO.play() #cambiar sonido incorrecto
                                break
                            else:
                                datos_juego["correctas_seguidas"] = 0
                                ERROR_SONIDO.play()
                        datos_juego["indice"] += 1
                        if datos_juego["indice"] >= len(lista_preguntas):
                            datos_juego["indice"] = 0
                            mezclar_lista(lista_preguntas)
                        pregunta_actual = pasar_pregunta(lista_preguntas,datos_juego["indice"],cuadro_pregunta,lista_respuestas)

                        comodines["pasar"] = 0
                        comodines["puntaje_doble"] = 0
                        comodines["doble_chance"] = 0                   
        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(cuadro_pregunta["superficie"],cuadro_pregunta["rectangulo"])
    pantalla.blit(boton_volver_terminado["superficie"],boton_volver_terminado["rectangulo"])
    if banderas["puntaje_doble"] == True:   
        pantalla.blit(boton_puntaje_doble["superficie"],boton_puntaje_doble["rectangulo"])
    if banderas["pasar"] == True:    
        pantalla.blit(boton_pasar["superficie"],boton_pasar["rectangulo"])
    if banderas["doble_chance"] == True:    
        pantalla.blit(boton_doble_chance["superficie"],boton_doble_chance["rectangulo"])
    for i in range(len(lista_respuestas)):
        pantalla.blit(lista_respuestas[i]["superficie"],lista_respuestas[i]["rectangulo"])
    
    mostrar_texto(cuadro_pregunta["superficie"],pregunta_actual["pregunta"],(15,10),FUENTE_PREGUNTA)
    mostrar_texto(lista_respuestas[0]["superficie"],pregunta_actual["respuesta_1"],(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[1]["superficie"],pregunta_actual["respuesta_2"],(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[2]["superficie"],pregunta_actual["respuesta_3"],(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[3]["superficie"],pregunta_actual["respuesta_4"],(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)

    mostrar_texto(boton_volver_terminado["superficie"],"VOLVER",(5,5),FUENTE_TEXTO,COLOR_NEGRO)
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_TEXTO,COLOR_BLANCO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),FUENTE_TEXTO,COLOR_BLANCO)
    mostrar_texto(pantalla,f"TIEMPO: {datos_juego['tiempo_restante']} seg",(300,10),FUENTE_TEXTO,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["correctas_seguidas"]}",(300,30),FUENTE_TEXTO,COLOR_BLANCO)
    mostrar_texto(pantalla,"X",(15,400),FUENTE_TEXTO,COLOR_NEGRO)
    mostrar_texto(pantalla,"PASAR",(20,330),FUENTE_TEXTO,COLOR_NEGRO)
    mostrar_texto(pantalla,"CHANCE\nDOBLE",(15,200),FUENTE_TEXTO,COLOR_NEGRO)

    return retorno