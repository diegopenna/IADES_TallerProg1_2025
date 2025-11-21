
import pickle, pathlib

#ruta absoluta
#archivo = "C:\\Users\\diego\\Documents\\IADES\\2025\\TP1\\source\\clases\\Repaso\\prueba.txt"
#ruta relativa
#archivo = ".\\Repaso\\prueba.txt"
#ruta absoluta
#archivo = "C:\\Users\\diego\\Documents\\IADES\\2025\\TP1\\tp_intermedio.txt"
#ruta relativa
#archivo = "..\\..\\tp_intermedio.txt"
#ruta relativa complicada
#archivo = "..\\..\\source\\..\\..\\TP1\\tp_intermedio.txt"
archivo = ".\\Repaso\\prueba.txt"

f = open(archivo, "rt", encoding="utf8") #Abriendo como lectura en modo texto
print(f.read())
f.close()

with open(archivo, "rt", encoding="utf8") as f:
    for linea in f:
        print(linea, end="\n")

with open(archivo, "wt", encoding="utf8") as f: #Abre en modo escritura, si no existe lo crea, si exite lo pisa
    f.write("Una Linea\n")
    f.write("Otra linea\n")
    print("Ahora con Print",file=f)


with open(archivo, "rt", encoding="utf8") as f:
    lineas = f.readlines()
    for linea in lineas:
        print(linea.rstrip(), end="\n")

print("Hola mundo|")

with open(archivo, "at", encoding="utf8") as f: #Abre en modo agreagar, si no existe lo crea, si exite lo pisa
    f.write(" Agrega el final\n")
    f.write("   Otra linea el final\n")
    print("       Ahora con Print el final",file=f)


with open(archivo, "rt", encoding="utf8") as f:
    
    linea = "*"
    while linea != "":
        linea = f.readline().rstrip()
        print(linea)

print(lineas)

with open(".\\Repaso\\lista.dump", "wb") as f:
    pickle.dump(lineas, f)

lineas = "Lalala"

print(lineas)

with open(".\\Repaso\\lista.dump", "rb") as f:
    lineas = pickle.load(f) 

print(lineas)


archivo = pathlib.Path(".\\Repaso\\Pepito.txt")

print(archivo.absolute())

if (not archivo.exists()):
    print("El archivo", archivo.name ,  " no existe.")


    
try:
    f = open(".\\Repaso\\Pepito.txt")
    var = int(f.read())
    print(f.read())
    print(var)
except FileNotFoundError:
    print("No puede abrir el archivo Pepito.txt porque no existe")
except ValueError:
    print("El archivo Pepito.txt no tiene un numero cargado")
except Exception:
    print("Ocurrio un Error desconocido")
else:
    print("El codigo ejecuta no tuvo ningun error")
finally:
    if f != None: 
        print("Cerrando Archivo")
        f.close()
    print("El finally siempre se ejecuta")


