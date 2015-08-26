import webbrowser
import time

def noticies():
    webbrowser.open("http://www.324.cat")
    return True

def proposta():
    print("Proposa-ho!")
    time.sleep(1.5)
    webbrowser.open("https://github.com/mikicat/Contestador/issues")
