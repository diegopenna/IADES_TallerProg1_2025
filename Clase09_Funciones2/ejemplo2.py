def menu(*platos):
    print("Menu del dia:\n")
    for plato in platos:
        print(plato)
    
    print("\nCantidad de Platos:", len(platos))

menu("Milanesa con pure", "Bife con ensalada", "Arroz con pollo")
print()
menu(["Milanesa con pure", "Bife con ensalada", "Arroz con pollo"], "Flan con D. de leche")
