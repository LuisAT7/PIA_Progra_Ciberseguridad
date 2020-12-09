#!/usr/bin/env python3

import argparse
from ExtraerData import Scraping
from extractDataFromImages import printMeta
import os


try:
        description = """Ejemplo de uso:
        +Se proporciona una carpeta con imagenes:
        Se guardará un txt abajo de cada foto con la metadata que se pudo extraer.

        Metadata.py -C C:\\Users\\cUsuario\\OneDrive\\Documents\\1.Programacion Python\\3 Semestre\\Tarea 2\\images"""

        parser = argparse.ArgumentParser(description="Metadata de imagenes", epilog=description,formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-C",metavar="Directorio", dest="carpeta", type=str, help="directorio donde estan las imagenes", required=True)
        params = parser.parse_args()

        #pp = os.getcwd()
        cd = (params.carpeta)
        os.chdir(cd)
        print(os.getcwd())
        printMeta()
except ValueError:
        pass
