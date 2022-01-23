#!/usr/bin/python3

# REALIZADO POR GABRIEL ARTERO MONSALVATJE Y CARLOTA RUIZ DE CONEJO DE LA SEN

import sys 
from subprocess import call
import os


# GUARDAMOS EL VALOR DE LA VARIABLE DE ENTORNO
numeroGrupo = os.environ.get("GROUP_NUMBER")


# MODIFICAMOS EL TITULO DE LA APLICACION
call(["cp", "practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "practica_creativa2/bookinfo/src/productpage/templates/productpageCopia.html"])
fCopia = open("practica_creativa2/bookinfo/src/productpage/templates/productpageCopia.html", 'r')
fOriginal = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'w')
for line in fCopia:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        fOriginal.write("{% block title %}Simple Bookstore App - GRUPO " + numeroGrupo + "{% endblock %}")
    else:
        fOriginal.write(line)
fOriginal.close()
fCopia.close()


# ARRANCAMOS LA APLICACIÓN
call(["python3", "practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"])
