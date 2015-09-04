# Fitxer per utilitzar la primera vegada de totes.
# Et configura la Contrasenya.
import pickle

def contra():
    newpwd = input("Nova Contrasenya: ")
    repeat = input("Repeteix la Contrasenya: ")
    if newpwd == repeat:
        try:
            contra = open('contra.dat', 'wb')
            pickle.dump(newpwd, contra)
            contra.close()
        except FileNotFoundError:
            print('El fitxer contra.dat no existeix')
    else:
        print("Les contrasenyes no coincideixen.")

contra()
