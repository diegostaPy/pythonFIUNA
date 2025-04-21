import numpy as np
from datetime import datetime, timedelta
import csv

def generar_datos_sinteticos():
    np.random.seed(42)
    
    # Tipos de camiones
    tipos_camion = np.array(['Volquete Pequeño', 'Volquete Mediano', 'Volquete Grande', 'Articulado'])
    capacidades = np.array([8, 12, 16, 20])
    eficiencias_base = np.array([0.85, 0.80, 0.75, 0.70])
    
    # Generar 20 camiones (5 de cada tipo)
    camiones = np.zeros(20, dtype=[
        ('id_camion', 'U10'),
        ('tipo', 'U20'),
        ('capacidad_teorica', 'i4'),
        ('eficiencia_base', 'f4')
    ])
    
    for i in range(20):
        tipo_idx = i // 5
        eficiencia = np.clip(np.random.normal(eficiencias_base[tipo_idx], 0.05), 0.6, 0.95)
        camiones[i] = (
            f"{tipos_camion[tipo_idx][:3]}-{i+1:02d}",
            tipos_camion[tipo_idx],
            capacidades[tipo_idx],
            eficiencia
        )
    
    # Generar 25 choferes
    choferes = np.zeros(25, dtype=[
        ('id_chofer', 'U10'),
        ('nombre', 'U20'),
        ('habilidad', 'f4'),
        ('antiguedad', 'i4')
    ])
    
    for i in range(25):
        habilidad = np.clip(np.random.normal(0.8, 0.1), 0.5, 1.0)
        choferes[i] = (
            f"CH-{i+1:02d}",
            f"Chofer {i+1}",
            habilidad,
            np.random.randint(1, 60)
        )
    
    # Generar registros diarios por 3 meses (90 días)
    num_registros = 90 * 18  # aprox 18 camiones/día
    registros = np.zeros(num_registros, dtype=[
        ('fecha', 'U10'),
        ('id_camion', 'U10'),
        ('tipo_camion', 'U20'),
        ('id_chofer', 'U10'),
        ('nombre_chofer', 'U20'),
        ('viajes', 'i4'),
        ('tierra_transportada', 'f4'),
        ('combustible', 'f4'),
        ('litros_cargados', 'f4')
    ])
    
    idx = 0
    for dia in range(90):
        fecha = (datetime(2023, 1, 1) + timedelta(days=dia)).strftime('%Y-%m-%d')
        num_camiones_dia = np.random.randint(15, 21)
        camiones_dia = np.random.choice(camiones, size=num_camiones_dia, replace=False)
        
        for camion in camiones_dia:
            chofer = np.random.choice(choferes)
            
            # Determinar número de viajes
            tipo = camion['tipo']
            viajes_base = 6 if tipo == 'Volquete Pequeño' else \
                         5 if tipo == 'Volquete Mediano' else \
                         4 if tipo == 'Volquete Grande' else 3
            viajes = max(1, int(np.random.normal(viajes_base, 1) * chofer['habilidad']))
            
            # Calcular tierra transportada
            eficiencia_viaje = camion['eficiencia_base'] * chofer['habilidad'] * np.random.uniform(0.9, 1.1)
            tierra = camion['capacidad_teorica'] * eficiencia_viaje * viajes
            
            # Calcular combustible
            consumo_base = 80 if tipo == 'Volquete Pequeño' else \
                         120 if tipo == 'Volquete Mediano' else \
                         150 if tipo == 'Volquete Grande' else 200
            combustible = max(50, consumo_base * viajes * np.random.uniform(0.8, 1.2))
            
            registros[idx] = (
                fecha,
                camion['id_camion'],
                camion['tipo'],
                chofer['id_chofer'],
                chofer['nombre'],
                viajes,
                round(tierra, 2),
                round(combustible, 2),
                round(combustible * np.random.uniform(0.95, 1.05), 2)
            )
            idx += 1
    
    # Guardar en archivos CSV
    np.savetxt('Datos/camiones.csv', camiones, delimiter=',', fmt='%s', 
               header=','.join(camiones.dtype.names), comments='',encoding='utf8')
    np.savetxt('Datos/choferes.csv', choferes, delimiter=',', fmt='%s', 
               header=','.join(choferes.dtype.names), comments='',encoding='utf8')
    np.savetxt('Datos/registros.csv', registros, delimiter=',', fmt='%s', 
               header=','.join(registros.dtype.names), comments='',encoding='utf8')
    
    print("Datos sintéticos generados y guardados en CSV")
    
generar_datos_sinteticos()
    
 