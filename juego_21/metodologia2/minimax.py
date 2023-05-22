probabilidad_deseada = 0
lanzamientos = 0

while probabilidad_deseada < 0.9:
    lanzamientos += 1
    probabilidad_no_deseada = (34/36) ** lanzamientos
    probabilidad_deseada = 1 - probabilidad_no_deseada

print("Número de lanzamientos necesarios para tener una probabilidad deseada mayor al 90%:", lanzamientos)
print("Probabilidad de obtener la combinación deseada al menos una vez en", lanzamientos, "lanzamientos:", probabilidad_deseada)