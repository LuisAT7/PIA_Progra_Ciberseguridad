#!/usr/bin/env python3

import os
import requests
from lxml import html
from bs4 import BeautifulSoup
import logging
import hashlib
from functools import partial

def Obtener_hash(filename):
       with open(filename, mode='rb') as f:
           d = hashlib.sha512()
           for buf in iter(partial(f.read, 128), b''):
               d.update(buf)
       return d.hexdigest()



class Scraping:

    def scrapingImages(self,url,var1):
        print("\nObteniendo imagenes de la url:"+ url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener imagenes
            images = parsed_body.xpath('//img/@src')

            print ('Imagenes %s encontradas' % len(images))

            #create directory for save images
            os.system("mkdir {0}".format(var1))

            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                # download images in images directory
                r = requests.get(download)
                f = open('{0}/%s'.format(var1) % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
            logging.info('\n\nfunción scrapingImages ejecutada...')
        except Exception as e:
                print(e)
                print ("Error conexion con " + url)
                pass

    def scrapingPDF(self,url,var2):
        print("\nObteniendo pdfs de la url:"+ url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # expresion regular para obtener pdf
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

            #create directory for save pdfs
            if len(pdfs) >0:
                os.system("mkdir {0}".format(var2))

            print ('posibles encontrados %s pdf' % len(pdfs))

            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print(download)

                # descarga pdfs
                r = requests.get(download)
                f = open('{0}/%s'.format(var2) % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()

            logging.info('\n\nfunción scrapingImages ejecutada...')
        except Exception as e:
            print(e)
            print("Error conexion con " + url)
            pass

    def scrapingLinks(self,url,carpeta,nombretxt):
            print("\nObteniendo links de la url:"+ url)

            try:
                response = requests.get(url)
                parsed_body = html.fromstring(response.text)

                # expresion regular para obtener links
                links = parsed_body.xpath('//a/@href') #MEJORAAAAR PQ TAMBIEN GUARDA HIPERVÍNCULOS

                print('links %s encontrados' % len(links))

                if len(links) >0:
                    os.system("mkdir {0}".format(carpeta))
                    pp = os.getcwd()
                    cd = (pp +'\\'+str(carpeta))
                    os.chdir(cd)
                    file = open(nombretxt+'.txt', 'w')
                    for link in links:
                        file.write(link +'\n')
                    file.close()

                    print('\n\nEl hash de el txt es:\n'+Obtener_hash(nombretxt+'.txt')+'\n\n')

                logging.info('\n\nfunción scrapingLinks a sido ejecutada...')
                #for link in links:
                    #print(link)

            except Exception as e:
                    print(e)
                    print("Error conexion con " + url)
                    pass
