import pickle

def contra():
    newpwd = input("Nova Contrasenya: ")
    repeat = input("Repeteix la Contrasenya: ")
    if newpwd == repeat:
        contra = open('contra.dat', 'wb')
        pickle.dump(newpwd, contra)
        contra.close()
    else:
        print("Les contrasenyes no coincideixen.")



