Proyecto Final Programacíon para ciberseguridad
***********************************************
Este proyecto consta de herramientas vistas en clase con las cuales se espera demostrar el conocimiento adquirido
durante el semestre, esperamos sea de su agrado.

Instrucciones de uso
====================

Este programa cuenta con 7 modulos para su correcto funcionamiento, los cuales se llamam en el scrpit 
llamado Suite_GSLT.py estos 7 deben estar en el mismo directorio para que puedan ser llamados correctamente.

Paso 1:
+++++++

Se debera hacer la instalacion de todos los modulos externos necesarios para ello se cuenta
con el archivo requirements.txt
**como Admin**

pip3 install -r requirements.txt

Paso 2:
+++++++

El menu de opciones es muy intuitivo y facil de usar tratamos de evitar cualquier error que pudiera tumbar el codigo
con el manejo de excepciones y validaciones. 
Podrá señeccionar una de estas opciones:
1. Web Scraping
2. Análisis de Metadata
3. Ossint con Hunter
4. Conexión por Socket
0. Para salir

Paso 3:
+++++++

cada menu tiene sus propias herramientas y se imprimen en pantalla como se debe utilizar.

Uso de Argparse
===============

En el menú con la opcion 2 se debera ingresar: Metadata.py -C **ruta** \n
A decir verdad solo queriamos comprobar el conocimiento que tenieamos sobre esa funcionalidad.

Tabla:

+------------------------+
|        Modulos         |
+------------------------+
|*extractDataFromImages* |
|                        |
| *horaSistema.ps1*      |
|                        |
| *menu_principal.py*    |
| *Metadata.py*          |
|                        |
| *PRUEBAHUNTER.py*      |
|                        |
| *Scraping.py*          |
|                        | 
| *Suite_GSLT.py*        |
+------------------------+