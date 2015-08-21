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

form = formulari()

def mayus():
    print("______   ______   __   __   ______   ______   ______   ______  ______  ____     ______   ______")
    print("||       ||   |   ||\  ||     ||     ||       ||___      ||    ||   |  ||  \    ||   |   ||___|")
    print("||       ||   |   || \ ||     ||     ||--         ||     ||    ||---|  ||   |   ||   |   ||  \ ")
    print("||____   ||___|   ||  \||     ||     ||____   ____||     ||    ||   |  ||__/    ||___|   ||   \ ")
    print("\n")
    print("                                                                                     by Mikicat")
    print("\n")
    print("Important: La primera lletra NO HA DE SER MAJUSCULA")
mayus()

def main():
    while True:
        time.sleep(1)
        print("\n")
        print("Benvingut al contestador")
        pregunta = input("Què vols preguntar? ")
        paraules = pregunta.split()
        if "estas?" in paraules:
            vida_estat()
        elif "com" in paraules and "va" in paraules and "tot?" in paraules:
            vida_estat()
        elif "dia" in paraules and "es" in paraules and "avui?" in paraules:
            avui()
        elif "coses" in paraules and "t'agraden" in paraules or "t'agraden?" in paraules:
            gustos()
        elif "noticies" in paraules or "noticies?" in paraules:
            noticies()
        elif "passa" in paraules and "mon?" in paraules:
            noticies()
        elif "web" in paraules and "escola?":
            web_escola()
        elif "teu" in paraules and "nom?" in paraules:
            nom()
        elif "dius?" in paraules or "dius" in paraules:
            nom()
        elif "fora" in paraules:
            quit()
        elif "recorda'm" in paraules:
            recorda()
            break
        elif "contacta" in paraules or "contactar" in paraules:
            form.contacta()
        elif "mirar" in paraules and "formulari" in paraules:
            contra = open('contra.dat', 'rb')
            ldpasswd = pickle.load(contra)
            contra.close()
            passwd = input("Contrasenya: ")
            if passwd == ldpasswd:
                form.mira_formulari()
            else:
                print("Accés Denegat")
                break
        elif "temps" in paraules and "avui?" in paraules:
            temps()
        elif "esborra" in paraules and "conversa" in paraules or "esborrar" in paraules and "conversa?" in paraules:
            print("\n" * 50)
        elif "guardar" in paraules and "formulari" in paraules and "desencriptat" in paraules or "desencriptat?" in paraules:
            form.formulari_txt()
        elif "campus" in paraules or "web" in paraules and "estudiants" in paraules:
            web_estudiants()
        else:
            respostes_limitades()
            mayus()
main()


