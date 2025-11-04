import pathlib

print(pathlib.Path.cwd())

unArch = pathlib.Path("pepito.txt")

if unArch.exists():
    print("Existe")
else:
    print("No Existe")

print(unArch.absolute())

otroArch = pathlib.Path("texto.txt")

if otroArch.exists():
    print("Existe")
else:
    print("No Existe")
