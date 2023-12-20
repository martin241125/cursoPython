conjunto1 = {1,2,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1)
resultado2 = conjunto2.issuperset(conjunto1)



# verificar si hay algun numero en comun

resultado3 = conjunto2.isdisjoint(conjunto1)

print(resultado)
print(resultado2)
print(resultado3)