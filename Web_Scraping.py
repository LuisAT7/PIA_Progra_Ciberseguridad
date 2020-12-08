import requests
from bs4 import BeautifulSoup as bs
import sys
import os
import argparse

i = 0
def download(url,folder):
	global i
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
		if "?" in url:
			url = url.split("?")[-2]
		try:
			with open(folder+'/'+str(i)+url.split('/')[-1], 'wb') as f:
				for chunk in r.iter_content(chunk_size=8192):
					f.write(chunk)
				i=i+1
		except Exception as e:
			print(e)


try:
        description = '''Ejemplo de uso:
                +Dos parametros -link & -c
                        -link http://www.fcfm.uanl.mx/
                        -c nuevacarpeta'''
        parser = argparse.ArgumentParser(description="Metadata de imagenes", epilog=description,formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument("-link",metavar="Link", dest="link", type=str, help="Link para la obtenccion", required=True)
        parser.add_argument("-c",metavar="Carpeta", dest="carpeta", type=str, help="nombre de la nueva carpeta", required=True)
        params = parser.parse_args()

        os.mkdir(params.carpeta)
        r = requests.get(url=params.link)
        soup = bs(r.content, 'html.parser')

        imagenes = soup('img')
        for imagen in imagenes:
                #print(imagen)
                url = imagen.get('src')
                print(url)
                if not 'data:' in url:
                        if 'http' in url:
                                download(url,params.carpeta)
                        else:
                                if url[0]=="/":
                                        split_url = params.link.split('/')
                                        url = split_url[0]+"//"+split_url[2]+url
                                else:
                                        url = params.link+"/"+url
                                download(url,params.carpeta)
except Exception as e:
        print("ERROR")
        print(e)
