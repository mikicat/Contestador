import random
import time
import webbrowser

def vida_estat():
    estats = ['Estic be', 'Perfecte!', 'Em sento sol', 'Doncs com que plou estic trist', 'Em trobo malament']
    print(random.choice(estats))
    return True

def temps():
    print("Doncs mira... Ara ho veuràs!")
    time.sleep(1.5)
    webbrowser.open("http://meteo.cat/prediccio/general/")

def avui():
    print("Avui es %s" % time.asctime())
    return True
    
def nom():
    print("Em dic Rootbot.")
    pregunta_nom = input("I tu, com et dius? ")
    print("Encantat de conèixe't, %s" % pregunta_nom)
