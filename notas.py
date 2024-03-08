
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))


romedio = (nota1 + nota2 + nota3 + nota4) / 4


if promedio >= 4:
    print("Excelente")
    descuento = 0.20  # 20% de descuento
elif promedio >= 3:
    print("Bien")
    descuento = 0
else:
    print("Deficiente")
    descuento = 0


costo_matricula = 1000  # Costo base de la matrícula
costo_final = costo_matricula - (costo_matricula * descuento)

print(f"El estudiante debe pagar: ${costo_final}")