#!/usr/bin/python3

import logging 
import sys 
from subprocess import call
import os


logging.basicConfig(level=logging.DEBUG) 
logger = logging.getLogger('pc2')

def funcion1():
    # COMANDOS NECESARIOS PARA LA PUESTA EN MARCHA DE LA APLICACIÓN	
    call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"])
    logger.debug("Repositorio clonado correctamente") 

    call(["cd", "./practica_creativa2/bookinfo/src/productpage"])


    call(["pip3", "install", "-r", "requirements.txt"])
    logger.debug("El XML de C1 se ha creado correctamente") 


    # MODIFICAMOS EL TITULO DE LA APLICACION
    call(["cd", "templates"])

    ############ FALTA ESTA PARTE: HAY QUE USAR LA VARIABLE DE ENTORNO PREVIAMENTE CREADA PARA 
    ############ MODIFICAR ESTE VALOR

    fc1 = open("index.html", "w")
    fc1.replace("{% block title %}Simple Bookstore App{% endblock %}", "{% block title %}Grupo 23{% endblock %}")
    fc1.close()


    call(["python3", "productpage-monolith.py", "9080"])
    logger.debug("La aplicación se está ejecuntando correctamente. Puede acceder a ella desde https://<ip-publica>:9080/productpage") 



