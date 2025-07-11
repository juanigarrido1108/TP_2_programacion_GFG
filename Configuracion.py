import pygame
from Constantes import *
from Funciones import *
pygame.init()

boton_suma_musica = crear_elemento_juego("mas.webp",60,60,420,200)
boton_resta_musica = crear_elemento_juego("menos.webp",60,60,20,200)
boton_suma_efectos = crear_elemento_juego("mas.webp",60,60,420,400)
boton_resta_efectos = crear_elemento_juego("menos.webp",60,60,20,400)
boton_volver = crear_elemento_juego("textura_volver.png",100,40,10,10)
boton_silencio = crear_elemento_juego("silencio.png",60,60,20,300)
boton_silencio_efectos = crear_elemento_juego("silencio.png",60,60,20,500)

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "ajustes"

    porcentaje_volumen_efectos = datos_juego["volumen_efectos"] / 100
    CLICK_SONIDO.set_volume(porcentaje_volumen_efectos)
    ERROR_SONIDO.set_volume(porcentaje_volumen_efectos)
    COMODIN_SONIDO.set_volume(porcentaje_volumen_efectos)
    ERROR.set_volume(porcentaje_volumen_efectos)
    ACIERTO.set_volume(porcentaje_volumen_efectos)

    #Gestionar los eventos
    porcentaje_volumen_efectos = datos_juego["volumen_efectos"] / 100
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_suma_musica["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] <= 95:
                    datos_juego["volumen_musica"] += 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_resta_musica["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            if boton_suma_efectos["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_efectos"] <= 95:
                    datos_juego["volumen_efectos"] += 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_resta_efectos["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_efectos"] > 0:
                    datos_juego["volumen_efectos"] -= 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_silencio["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] = 0
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_silencio_efectos["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_efectos"] > 0:
                    datos_juego["volumen_efectos"] = 0
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
                CLICK_SONIDO.play()
            
    
    #Mostrar en pantalla los elementos
    fondo_configuraciones = pygame.transform.scale(pygame.image.load("configuraciones.jpg"),PANTALLA)
    pantalla.blit(fondo_configuraciones,(0,0))
    pantalla.blit(boton_suma_musica["superficie"],boton_suma_musica["rectangulo"])
    pantalla.blit(boton_resta_musica["superficie"],boton_resta_musica["rectangulo"])
    pantalla.blit(boton_suma_efectos["superficie"],boton_suma_efectos["rectangulo"])
    pantalla.blit(boton_resta_efectos["superficie"],boton_resta_efectos["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    pantalla.blit(boton_silencio["superficie"],boton_silencio["rectangulo"])
    pantalla.blit(boton_silencio_efectos["superficie"],boton_silencio_efectos["rectangulo"])

    mostrar_texto(pantalla,f"MUSICA: {datos_juego["volumen_musica"]}%",(100,200),FUENTE_VOLUMEN)
    mostrar_texto(pantalla,f"EFECTOS: {datos_juego["volumen_efectos"]}%",(100,400),FUENTE_VOLUMEN)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_TEXTO,COLOR_NEGRO)
    
    return retorno
