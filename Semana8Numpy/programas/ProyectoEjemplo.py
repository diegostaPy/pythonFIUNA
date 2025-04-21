"""
Programa de Análisis de Eficiencia para Camiones y Choferes

Este programa está diseñado para evaluar el desempeño de una flota de camiones volquete
 y sus conductores. El sistema genera datos sintéticos que simulan tres meses de 
 operaciones, incluyendo información sobre viajes realizados, combustible consumido y
   material transportado. Utilizando exclusivamente NumPy para el procesamiento de datos,
     el programa calcula métricas clave de eficiencia como la relación entre toneladas 
     transportadas y litros de combustible consumido, tanto por camión como por chofer. 
     Los resultados se almacenan en archivos CSV para facilitar su posterior análisis y 
     se complementan con un menú interactivo que permite visualizar las estadísticas más 
     relevantes.

El núcleo del programa consta de tres componentes principales: generación de datos 
sintéticos (que simulan diferentes tipos de camiones con capacidades variables y choferes
 con distintos niveles de habilidad), cálculo de estadísticas (donde se procesan los 
 registros operativos para obtener indicadores de desempeño), y visualización de 
 resultados (que presenta la información de manera gráfica para facilitar su 
 interpretación). La arquitectura del sistema está optimizada para manejar grandes 
 volúmenes de datos de manera eficiente, utilizando arrays estructurados de NumPy que 
 permiten operaciones vectorizadas y un consumo mínimo de recursos.
"""
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import os
import numpy as np

def leer_datos_sinteticos():
    print("Cargando datos existentes desde archivos CSV...")
    
    # Leer camiones
    camiones = np.genfromtxt(
        'Datos/camiones.csv',
        delimiter=',',
        dtype=[
            ('id_camion', 'U10'),
            ('tipo', 'U20'),
            ('capacidad_teorica', 'i4'),
            ('eficiencia_base', 'f4')
        ],
        skip_header=1,
        encoding='utf-8'
    )
    
    # Leer choferes
    choferes = np.genfromtxt(
        'Datos/choferes.csv',
        delimiter=',',
        dtype=[
            ('id_chofer', 'U10'),
            ('nombre', 'U20'),
            ('habilidad', 'f4'),
            ('antiguedad', 'i4')
        ],
        skip_header=1,
        encoding='utf-8'
    )
    
    # Leer registros
    registros = np.genfromtxt(
        'Datos/registros.csv',
        delimiter=',',
        dtype=[
            ('fecha', 'U10'),
            ('id_camion', 'U10'),
            ('tipo_camion', 'U20'),
            ('id_chofer', 'U10'),
            ('nombre_chofer', 'U20'),
            ('viajes', 'i4'),
            ('tierra_transportada', 'f4'),
            ('combustible', 'f4'),
            ('litros_cargados', 'f4')
        ],
        skip_header=1,
        encoding='utf-8'
    )
    
    print(f"Datos cargados: {len(camiones)} camiones, {len(choferes)} choferes, {len(registros)} registros")
    return camiones, choferes, registros


def calcular_estadisticas(camiones, choferes, registros):
    # Estadísticas por camión
    camion_ids = np.unique(registros['id_camion'])
    stats_camion = np.zeros(len(camion_ids), dtype=[
        ('id_camion', 'U10'),
        ('tipo', 'U20'),
        ('tierra_total', 'f4'),
        ('combustible_total', 'f4'),
        ('eficiencia', 'f4'),
        ('viajes_total', 'i4')
    ])
    
    for i, camion_id in enumerate(camion_ids):
        mask = registros['id_camion'] == camion_id
        tierra_total = np.sum(registros['tierra_transportada'][mask])
        comb_total = np.sum(registros['combustible'][mask])
        tipo = registros['tipo_camion'][mask][0]
        
        stats_camion[i] = (
            camion_id,
            tipo,
            tierra_total,
            comb_total,
            tierra_total / comb_total,
            np.sum(registros['viajes'][mask])
        )
    
    # Estadísticas por chofer
    chofer_ids = np.unique(registros['id_chofer'])
    stats_chofer = np.zeros(len(chofer_ids), dtype=[
        ('id_chofer', 'U10'),
        ('nombre', 'U20'),
        ('tierra_total', 'f4'),
        ('combustible_total', 'f4'),
        ('eficiencia', 'f4'),
        ('viajes_total', 'i4')
    ])
    
    for i, chofer_id in enumerate(chofer_ids):
        mask = registros['id_chofer'] == chofer_id
        tierra_total = np.sum(registros['tierra_transportada'][mask])
        comb_total = np.sum(registros['combustible'][mask])
        nombre = registros['nombre_chofer'][mask][0]
        
        stats_chofer[i] = (
            chofer_id,
            nombre,
            tierra_total,
            comb_total,
            tierra_total / comb_total,
            np.sum(registros['viajes'][mask])
        )
    
    # Guardar estadísticas en CSV
    np.savetxt('resultados/stats_camion.csv', stats_camion, delimiter=',', fmt='%s', 
               header=','.join(stats_camion.dtype.names), comments='',encoding='utf8')
    np.savetxt('resultados/stats_chofer.csv', stats_chofer, delimiter=',', fmt='%s', 
               header=','.join(stats_chofer.dtype.names), comments='',encoding='utf8')
    
    return stats_camion, stats_chofer

def mostrar_menu():
    print("\n--- MENÚ DE ESTADÍSTICAS ---")
    print("1. Mostrar estadísticas de camiones")
    print("2. Mostrar estadísticas de choferes")
    print("3. Mostrar top 5 más eficientes")
    print("4. Visualizar Datos")

    print("5. Salir")
    return input("Seleccione una opción: ")

def mostrar_estadisticas_camiones(stats):
    print("\n--- ESTADÍSTICAS POR CAMIÓN ---")
    for camion in stats_camion:
        print(f"\nCamión: {camion['id_camion']} ({camion['tipo']})")
        print(f"Tierra transportada: {camion['tierra_total']:.2f} ton")
        print(f"Combustible usado: {camion['combustible_total']:.2f} L")
        print(f"Eficiencia: {camion['eficiencia']:.2f} ton/L")
        print(f"Viajes totales: {camion['viajes_total']}")
def mostrar_estadisticas_choferes(stats):
    print("\n--- ESTADÍSTICAS POR CHOFER ---")
    for chofer in stats_chofer:
        print(f"\nChofer: {chofer['nombre']} ({chofer['id_chofer']})")
        print(f"Tierra transportada: {chofer['tierra_total']:.2f} ton")
        print(f"Combustible usado: {chofer['combustible_total']:.2f} L")
        print(f"Eficiencia: {chofer['eficiencia']:.2f} ton/L")
        print(f"Viajes totales: {chofer['viajes_total']}")

def mostrar_top_eficientes(stats_camion, stats_chofer):
    print("\n--- TOP 5 MÁS EFICIENTES ---")
    
    sorted_camiones = np.sort(stats_camion, order='eficiencia')[::-1]
    print("\nTop 5 camiones más eficientes:")
    for i, camion in enumerate(sorted_camiones[:5], 1):
        print(f"{i}. {camion['id_camion']}: {camion['eficiencia']:.2f} ton/L")
            
    # Top 5 choferes
    sorted_choferes = np.sort(stats_chofer, order='eficiencia')[::-1]
    print("\nTop 5 choferes más eficientes:")
    for i, chofer in enumerate(sorted_choferes[:5], 1):
        print(f"{i}. {chofer['nombre']}: {chofer['eficiencia']:.2f} ton/L")
def visualizar_resultados(stats_camion, stats_chofer):
    """Visualiza las estadísticas de camiones y choferes calculadas.
    
    Args:
        stats_camion (np.array): Array estructurado con estadísticas por camión
        stats_chofer (np.array): Array estructurado con estadísticas por chofer
    """
    # Configuración inicial
    plt.style.use('seaborn')
    os.makedirs('resultados', exist_ok=True)
    
    # 1. Gráfico de eficiencia por camión (ordenado)
    # Ordenar camiones por eficiencia
    camiones_ordenados = np.sort(stats_camion, order='eficiencia')[::-1]
    
    plt.figure(figsize=(14, 7))
    bars = plt.bar(camiones_ordenados['id_camion'], camiones_ordenados['eficiencia'],
        color=plt.cm.viridis(np.linspace(0, 1, len(camiones_ordenados))))
    
    # Añadir etiquetas y personalización
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2., 
            height/2,
            f"{height:.2f}\n({int(camiones_ordenados[bars.index(bar)]['viajes_total'])} viajes)",
            ha='center', 
            va='center',
            color='white',
            fontweight='bold')
    
    plt.xticks(rotation=45, ha='right')
    plt.title('Eficiencia por Camión (Ordenados)\nToneladas por litro de combustible', pad=20)
    plt.ylabel('Eficiencia [ton/L]')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('resultados/eficiencia_camiones_ordenados.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Comparación por tipo de camión (boxplot)
    tipos = np.unique(stats_camion['tipo'])
    
    plt.figure(figsize=(10, 6))
    data = [stats_camion['eficiencia'][stats_camion['tipo'] == tipo] for tipo in tipos]
    
    box = plt.boxplot(data, patch_artist=True, labels=tipos)
    
    # Colores para los boxplots
    colors = plt.cm.Set2(np.linspace(0, 1, len(tipos)))
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    
    plt.ylabel('Eficiencia [ton/L]')
    plt.title('Distribución de Eficiencia por Tipo de Camión', pad=15)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('resultados/eficiencia_tipos_camion.png', dpi=300)
    plt.close()
    
    # 3. Top 10 choferes (eficiencia y viajes)
    top_idx = np.argsort(stats_chofer['eficiencia'])[-10:][::-1]
    top_choferes = stats_chofer[top_idx]
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Barras de eficiencia
    bars = ax1.barh(
        top_choferes['nombre'], 
        top_choferes['eficiencia'],
        color=plt.cm.magma_r(np.linspace(0.2, 0.8, 10)))
    
    ax1.set_xlabel('Eficiencia [ton/L]', fontsize=12)
    ax1.set_title('Top 10 Choferes por Eficiencia y Viajes', pad=15)
    
    # Eje secundario para viajes
    ax2 = ax1.twiny()
    ax2.plot(
        top_choferes['viajes_total'], 
        np.arange(len(top_choferes)),
        'o-', 
        color='green',
        markersize=8,
        label='Viajes')
    
    ax2.set_xlabel('Número de Viajes', color='green')
    ax2.tick_params(axis='x', colors='green')
    
    # Etiquetas de eficiencia
    for bar in bars:
        width = bar.get_width()
        ax1.text(
            width * 0.95,
            bar.get_y() + bar.get_height()/2,
            f'{width:.2f}',
            ha='right',
            va='center',
            color='white',
            fontweight='bold')
    
    plt.gca().invert_yaxis()
    ax1.grid(axis='x', alpha=0.3)
    ax2.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('resultados/top_choferes_eficiencia_viajes.png', dpi=300)
    plt.close()
    
    # 4. Relación viajes-eficiencia choferes
    plt.figure(figsize=(10, 6))
    
    scatter = plt.scatter(
        stats_chofer['viajes_total'],
        stats_chofer['eficiencia'],
        c=stats_chofer['eficiencia'],
        cmap='viridis',
        s=100,
        alpha=0.7)
    
    plt.colorbar(scatter, label='Eficiencia [ton/L]')
    plt.xlabel('Total de Viajes', fontsize=12)
    plt.ylabel('Eficiencia [ton/L]', fontsize=12)
    plt.title('Relación entre Viajes y Eficiencia de Choferes', pad=15)
    
    # Línea de tendencia
    z = np.polyfit(stats_chofer['viajes_total'], stats_chofer['eficiencia'], 1)
    p = np.poly1d(z)
    plt.plot(
        stats_chofer['viajes_total'], 
        p(stats_chofer['viajes_total']), 
        "r--",
        label='Tendencia')
    
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('resultados/relacion_viajes_eficiencia.png', dpi=300)
    plt.close()
    
    print("Gráficos guardados en la carpeta 'resultados'")
print("Leyendo datos ...")
camiones, choferes, registros = leer_datos_sinteticos()
os.makedirs('resultados', exist_ok=True)
    
stats_camion, stats_chofer = calcular_estadisticas(camiones, choferes, registros)
    
while True:
    opcion = mostrar_menu()
        
    if opcion == '1':
        mostrar_estadisticas_camiones(stats_camion)
    elif opcion == '2':
        mostrar_estadisticas_choferes(stats_chofer)
    elif opcion == '3':
        mostrar_top_eficientes(stats_camion, stats_chofer)
    elif opcion == '4':
        visualizar_resultados(stats_camion, stats_chofer)

    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

