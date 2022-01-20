#!/usr/bin/python3

# REALIZADO POR GABRIEL ARTERO MONSALVATJE Y CARLOTA RUIZ DE CONEJO DE LA SEN

import logging 
import sys 
from subprocess import call
import os
from os import remove


logging.basicConfig(level=logging.DEBUG) 
logger = logging.getLogger('instalacionDocker')

# COMANDOS PARA LA INTALACION DE DOCKER
call(["sudo apt-get update",  "-y"], shell=True)
call(["sudo apt-get install ca-certificates curl gnupg lsb-release",  "-y"], shell=True)
call(["curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg",  "-y"], shell=True)
call(["echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",  "-y"], shell=True)
call(["sudo apt-get update",  "-y"], shell=True)
call(["sudo apt-get install docker-ce docker-ce-cli containerd.io",  "-y"], shell=True)
call(["sudo apt-get install docker-ce=5:18.09.1~3-0~ubuntu-xenial docker-ce-cli=5:18.09.1~3-0~ubuntu-xenial containerd.io",  "-y"], shell=True)
logger.debug("Docker se ha instalado correctamente") 
