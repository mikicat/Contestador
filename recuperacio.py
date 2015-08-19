import pickle

def dni():
    ask = input("El teu D.N.I: ")
    dni = open('dni.dat', 'wb')
    pickle.dump(ask, dni)
    dni.close()
    contra()
    
def contra():
    ask = input("D.N.I: ")
    dni = open('dni.dat', 'rb')
    readni = pickle.load(dni)
    dni.close()
    if ask == readni:
        newpwd = input("Nova Contrasenya: ")
        repeat = input("Repeteix la Contrasenya: ")
        if newpwd == repeat:
            contra = open('contra.dat', 'wb')
            pickle.dump(newpwd, contra)
            contra.close()
        else:
            print("Acces Denegat")
    else:
        print("Acces Denegat")



