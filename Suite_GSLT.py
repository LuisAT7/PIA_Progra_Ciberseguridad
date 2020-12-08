#!/usr/bin/env python3
# coding=utf-8

import os
import sys
import menu_principal
from menu_principal import colores
import logging
import subprocess

logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s',
    level  = logging.INFO,
    filemode = "a"
    )
# Si el root logger ya tiene handlers, se eliminan antes de añadir los nuevos.
# Esto es importante para que los logs no empiezen a duplicarse.
if logging.getLogger('').hasHandlers():
    logging.getLogger('').handlers.clear()
# niveles superiores.
file_debug_handler = logging.FileHandler('logs_debug.log')
file_debug_handler.setLevel(logging.DEBUG)
file_debug_format = logging.Formatter('%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s')
file_debug_handler.setFormatter(file_debug_format)
logging.getLogger('').addHandler(file_debug_handler)

consola_handler = logging.StreamHandler()
consola_handler.setLevel(logging.INFO)
consola_handler_format = logging.Formatter('%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s')
consola_handler.setFormatter(consola_handler_format)
logging.getLogger('').addHandler(consola_handler)

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
def Principal():

    # Revisar el sistema en el cual estaremos trabajando
    operating_system = menu_principal.Sistea_Op()

    if operating_system == "posix":
        # Revisar si esta como Root
        #si no lo esta se sale
        if os.geteuid() != 0:
            print("\n {0}Suite de Scraping en python - by Gustavo González y Luis Trejo".format(menu_principal.colores.GREEN))
            print("\n Not running as root. \n\nSaliendo de Suite GSLT\n")
            core.exit_set()

    txt = os.getcwd()
    valor = checkFileExistance(txt+'\\acuerdo.txt')
    if valor is True:
        with open('acuerdo.txt', 'r') as file:
            validar = file.readline()
            if validar == 'El usuario a aceptado los terminos.':
                pass
    else:
        print('\nAVISO URGENTE\nAl usar este programa debe estar conciente que es\npueden infringir algunas normas segun sea su lugar\nde origen los creadores no nos hacemos responsable del mal uso de este programa ')

        opc = input('¿Esta de acuerdo con los terminos de este programa [y/n]: ')
        opc += " "
        if opc[0].lower() == 'y':
            with open('acuerdo.txt', 'w') as file:
                file.write('El usuario a aceptado los terminos.')

        else:
            print('Lamentamos que no este de acuerdo que tenga un buen día')
            sys.exit()
    while True:
        menu_principal.Limpiar('1')
        archivo = "horaSistema.ps1"
        lineaPS = "Powershell -Executionpolicy Bypass -File " + archivo
        rutina = subprocess.check_output(lineaPS)
        print('\n\t\t\t    Hora de ejecucion del Script '+rutina.decode())
        input('\n\n\t\t\t\t       PRESIONE ENTER PARA CONTINUAR ')
        menu_principal.clean()
        menu_principal.Menu_Opc()
if __name__ == "__main__":
    logging.debug('Inicio main script')
    print('\n')
    logging.info('Inicio main script')
    Principal()
    logging.debug('Fin main script')
    print('\n')
    logging.info('\n\nFin main script')

    logging.shutdown()
