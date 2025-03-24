mediciones_invalidas = 0
suma_temperaturas = 0
contador = 0

while mediciones_invalidas < 3:
    temperatura = float(input())
    
    if 0 <= temperatura and temperatura <= 1000:
        suma_temperaturas += temperatura
        contador += 1
        print("Temperatura actual",temperatura)
    else:
        print("¡Alarma! Temperatura fuera del rango permitido (0°C - 1000°C).")
        mediciones_invalidas += 1

    
    
    if contador == 3:  # Cuando se acumulan tres mediciones válidas
        promedio = suma_temperaturas / 3
        print("Promedio",promedio)
        if abs(temperatura - promedio) > 20:
            print("¡Alarma! Se ha detectado una fluctuación inesperada en la temperatura.")
        else:
            print("La temperatura está dentro del rango normal.")
            # Reiniciamos las variables para las próximas mediciones
            suma_temperaturas = 0
            contador = 0
    
   
print("Se han ingresado más de 3 mediciones inválidas. Finalizando el programa.")