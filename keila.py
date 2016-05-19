texto=raw_input("ingrese textos")
letras=""
numeros=""
tem=len(texto)
for i in range(tem):

  if texto[i].isdigit():
    numeros=numeros+texto[i]
  else:
   letras=letras+texto[i]
print numeros
print letras

