
peso, altura = float(input("Peso (kg): ")), float(input("Altura (m): "))
imc = peso / (altura ** 2)
estado = "Bajo peso" if imc < 18.5 else "Normal" if 18.5 <= imc < 24.9 else "Sobrepeso" if 25 <= imc < 29.9 else "Obeso"
print(f"IMC: {imc:.2f} - Estado: {estado}")


peso = float(input("ingresa tu peso en kilogramos:"))
alt = float(input("Ingrese su altura en metros:"))
imc = peso / (alt ** 2)
if imc < 18.5:
    estado = "Bajo peso"
print(f"tu indice de masa muscular es:{imc} - Estado: {estado}")