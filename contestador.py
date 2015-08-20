import random
import sys
import time
import pickle
import webbrowser
from tecnologia import *
from escola import *
from vida import *
from altres import *
import time
def mayus():
    print("Important: La primera lletra NO HA DE SER MAJUSCULA")
mayus()
def main():
    while True:
        time.sleep(1)
        print("Benvingut al contestador")
        pregunta = input("Què vols preguntar? ")
        lletres = pregunta.split()
        if "estas?" in lletres:
            vida_estat()
        elif "com" in lletres and "va" in lletres and "tot?" in lletres:
            vida_estat()
        elif "dia" in lletres and "es" in lletres and "avui?" in lletres:
            avui()
        elif "coses" in lletres and "t'agraden" in lletres or "t'agraden?" in lletres:
            gustos()
        elif "noticies" in lletres or "noticies?" in lletres:
            noticies()
        elif "passa" in lletres and "mon?" in lletres:
            noticies()
        elif "web" in lletres and "escola?":
            web_escola()
        elif "teu" in lletres and "nom?" in lletres:
            nom()
        elif "dius?" in lletres or "dius" in lletres:
            nom()
        elif "fora" in lletres:
            quit()
        elif "recorda'm" in lletres:
            recorda()
            break
        elif "contacta" in lletres or "contactar" in lletres:
            contacta()
        elif "mirar" in lletres and "formulari" in lletres:
            contra = open('contra.dat', 'rb')
            ldpasswd = pickle.load(contra)
            contra.close()
            passwd = input("Contrasenya: ")
            if passwd == ldpasswd:
                ask = input("D.N.I: ")
                dni = open('dni.dat', 'rb')
                readni = pickle.load(dni)
                dni.close()
                if ask == readni:
                    print("\n" * 50)
                    mira_formulari()
                else:
                    print("Accés Denegat")
            else:
                print("Accés Denegat")
                break
        elif "temps" in lletres and "avui?" in lletres:
            temps()
        elif "esborra" in lletres and "conversa" in lletres or "esborrar" in lletres and "conversa?" in lletres:
            print("\n" * 50)
        else:
            respostes_limitades()
            mayus()
main()


