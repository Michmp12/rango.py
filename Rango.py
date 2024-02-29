var_numeroInt = int(input('Ingresa la cantidad de números a evaluar'))
contador = 0

for i in range(var_numeroInt):
    num = float(input('Ingrese el número ->'))
    if num >= 10 and num <= 20:
        contador += 1
        

print('La cantidad de números en el rango de 10 a 20 es: (contador)')