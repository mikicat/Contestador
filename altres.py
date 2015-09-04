import time
import sys
import pickle
from tkinter import *

def respostes_limitades():
    print("Whooops!")
    print("Recorda que tinc respostes limitades")

def read_record():
    hora = input("Per d'aquí quants minuts? ")
    num = float(hora)
    print("\n" * 50)
    countdown = num * 60
    while countdown > 0:
        time.sleep(1)
        countdown -= 1
    print("\n")
    load_file = open('recordatori.dat', 'rb')
    loaded_recordatori = pickle.load(load_file)
    load_file.close()
    tk = Tk()
    tk.wm_attributes("-topmost", 1)
    tk.title('Compte endarrere acabat!')
    Label(tk, text="RECORDA: %s" % loaded_recordatori).grid(row=0, column=0, sticky=W)
    Button(tk, text="Quit", command=tk.destroy).grid(row=1, column=1, sticky=W)


def recorda():
    print("RECORDA: PERQUE EL COMPTE ENRERE FUNCIONI HA D'ESTAR EL PROGRAMA OBERT, I HAURAS D'EXECUTAR-NE UN ALTRE PER PODER CONTINUAR PARLANT")
    nota = input("Què vols recordar? ")
    save_file = open('recordatori.dat', 'wb')
    pickle.dump(nota, save_file)
    save_file.close()
    read_record()
class formulari():
    def mira_formulari(self):
        try:
            load = open('formulari.dat', 'rb')
            loaded = pickle.load(load)
            load.close()
            print(loaded)
        except FileNotFoundError:
            print('El fitxer formulari.dat no existeix)

    def formulari_txt(self):
        try:
            load = open('formulari.dat', 'rb')
            loaded = pickle.load(load)
            load.close()
            formulari_desencriptat = open('formulari.txt', 'w')
            formulari_desencriptat.write(loaded)
            formulari_desencriptat.close()
            print("S'ha guardat el formulari desencriptat en el fitxer 'formulari.txt'")
        except FileNotFoundError:
            print('El fitxer formulari.txt no existeix')

    def contacta(self):
        #formulari
        nom = input("Nom: ")
        cognom = input("Cognom(s): ")
        email = input("Email: ")
        comentari = input("Comentari: ")
        dades = {'Nom' : nom,
        'Cognom' : cognom,
        'Email' : email,
        'Comentari' : comentari,
        }
        try:
            save = open('formulari.dat', 'wb')
            pickle.dump(dades, save)
            save.close()
        except FileNotFoundError:
            print('El fitxer formulari.dat no existeix')
