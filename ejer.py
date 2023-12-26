

def imprimir_impares_entre(l, r):
    # Verificar que l y r sean números enteros
    if not isinstance(l, int) or not isinstance(r, int):
        print("Error: Ambos l y r deben ser números enteros.")
        return
    
    # Asegurarse de que l sea menor o igual a r
    if l > r:
        l, r = r, l
    
    # Imprimir los números impares en el rango
    print(f"Números impares entre {l} y {r} (inclusive):")
    for num in range(l, r + 1):
        if num % 2 != 0:
            print(num)

# Ejemplo de uso
l = int(input("Ingrese el valor de l: "))
r = int(input("Ingrese el valor de r: "))
imprimir_impares_entre(l, r)

