import random
import time
import webbrowser

def saluda():
    hola = ["Benvingut", "Ei!", "Bon dia", "Allô!", "Eis!", "Hoooola!"]
    print(random.choice(hola))

def vida_estat():
    estats = ['Estic be', 'Perfecte!', 'Em sento sol', 'Doncs com que plou estic trist', 'Em trobo malament', 'Estic radiant!', 'Estic malalt...', 'Doncs estic adormit', 'No ho se gaire... Be?', 'Despert... El maleït gos ha tornat a bordar a les 6!!!', 'Deixa\'m en pau! Tant t\'avorreixes que has de parlar amb una màquina? No tens vida social o què?',]
    print(random.choice(estats))
    time.sleep(1.5)
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

def casar():
    tria = ['Si que vull, amor!', 'Crec que nomes et casaries amb uns pocs kiloBytes.', 'No crec que t\'ho permetin fer, aixo...', 'Si, accepto!']
    print(random.choice(tria))
