mercosur = ["Argentina", "Brasil", "Uruguay", "Paraguay" ]

pais = input("Ingrese Pais:")
pais = pais.title()

if pais in mercosur: 
    print(pais, "esta en el mercosur")
    print(pais, "esta en el indice:", mercosur.index(pais))
else:
    print(pais, "NO esta en el mercosur")

