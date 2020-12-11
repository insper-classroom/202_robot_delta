#!/usr/bin/python
# -*- coding: utf-8 -*-

# Este NÃO é um programa ROS

from __future__ import print_function, division 

import cv2
import os,sys, os.path
import numpy as np
import random


print("Rodando Python versão ", sys.version)
print("OpenCV versão: ", cv2.__version__)
print("Diretório de trabalho: ", os.getcwd())


def linha(img, line):
    line_color = (255,255,0)
    line_width=3
    cv2.line(img, line[0], line[1], line_color, line_width)

    
def crosshair(img, point, size = 9, color = (0,0,255)):
    """ Desenha um crosshair centrado no point.
        point deve ser uma tupla (x,y)
        color é uma tupla R,G,B uint8
    """
    x,y = point
    cv2.line(img,(x - size,y),(x + size,y),color,5)
    cv2.line(img,(x,y - size),(x, y + size),color,5)    
    

def texto(img, a, p):
    """Escreve na img RGB dada a string a na posição definida pela tupla p"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(a), p, font,1,(0,50,100),2,cv2.LINE_AA)


def intersection(segment, circle):
    """
        Encontra as interseções entre o segmento e o círculo e as devolve numa lista
        Se não houver, retornará lista vazia

        Seguindo referência: https://stackoverflow.com/questions/1073336/circle-line-segment-collision-detection-algorithm
    """
    inter = []
    (x1,y2),(x2,y2) = segment
    xc, yc, r = circle
    d = (x2-x1, y2 - y1) # vetor direcional do segmento
    

    return inter



if __name__ == "__main__":

    tela = np.zeros((600,800), dtype=np.uint8)

    while(True):
        # NOTE que em testes a OpenCV 4.0 requereu frames em BGR para o cv2.imshow
        cv2.imshow('imagem', tela)

        p1 = (50,60)
        p2 = (400,500)
        segment = (p1, p2)
        linha(tela, segment)

        for i in range(200):
            x = random.randint(100,700)
            y = random.rantin(100, 500)
            r = random.randint(50, 90)
            circle = (x,y,r)
            
            inter = intersection(segment, circle)
            for point in inter:
                crosshair(tela, point, )


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


