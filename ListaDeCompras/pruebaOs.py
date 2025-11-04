import os
print(os.getcwd())

for arch in os.listdir():
    print(arch, end="")
    print(" Es Direcotrio: ",  os.path.isdir(arch), end="")
    print(" Tamaño: ",  os.path.getsize(arch), end="")
    print(" FechaModif: ",  os.path.getmtime(arch))


    

