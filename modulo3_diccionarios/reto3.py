# 1. Definir ventas_por_region como dict anidado { region: { Q1, Q2, Q3, Q4 } }
ventas_por_region = {
    "Norte": {
        "Q1": 15000,
        "Q2": 22000,
        "Q3": 18000,
        "Q4": 25000
    },
    "Sur": {
        "Q1": 12000,
        "Q2": 19000,
        "Q3": 21000,
        "Q4": 23000
    },
    "Este": {
        "Q1": 18000,
        "Q2": 24000,
        "Q3": 22000,
        "Q4": 28000
    },
    "Oeste": {
        "Q1": 14000,
        "Q2": 17000,
        "Q3": 16000,
        "Q4": 20000
    }
}

# 2. Calcular el total anual de cada región con items() y sum(values())
def calcular_totales_anuales(ventas):
    """Calcula el total anual por región"""
    totales = {}
    for region, trimestres in ventas.items():
        total_anual = sum(trimestres.values())
        totales[region] = total_anual
    return totales

# 3. Usar max() con key=lambda para la región con mayores ventas
def region_con_mayores_ventas(totales):
    """Encuentra la región con mayores ventas totales"""
    return max(totales.items(), key=lambda x: x[1])

# 4. Acumular ventas por trimestre con iteración anidada
def ventas_por_trimestre(ventas):
    """Acumula el total de ventas por trimestre (suma todas las regiones)"""
    trimestres = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
    
    for region, datos in ventas.items():
        for trimestre, monto in datos.items():
            trimestres[trimestre] += monto
    
    return trimestres

# 5. Generar porcentajes con dict comprehension sobre el gran total
def calcular_porcentajes_region(totales):
    """Calcula qué porcentaje representa cada región del total global"""
    gran_total = sum(totales.values())
    
    # Dict comprehension para porcentajes
    porcentajes = {region: round((monto / gran_total) * 100, 1) 
                   for region, monto in totales.items()}
    
    return porcentajes, gran_total

# 6. Imprimir reporte ordenado de mayor a menor con sorted() + items()
def mostrar_reporte_completo(ventas):
    """Genera reporte completo ordenado de mayor a menor"""
    print("\n" + "="*60)
    print(" REPORTE DE VENTAS POR REGIÓN".center(60))
    print("="*60)
    
    # Calcular totales
    totales = calcular_totales_anuales(ventas)
    
    # Calcular trimestres
    trimestres = ventas_por_trimestre(ventas)
    
    # Calcular porcentajes
    porcentajes, gran_total = calcular_porcentajes_region(totales)
    
    # 6. Ordenar de mayor a menor con sorted()
    print("\n TOTALES POR REGIÓN:")
    print("-"*60)
    print(f"{'Región':<15} {'Total Anual':<15} {'% del Total':<12}")
    print("-"*60)
    
    for region, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
        print(f"{region:<15} ${total:>12,.2f}     {porcentajes[region]:>6.1f}%")
    
    # Mostrar región ganadora
    region_top, ventas_top = region_con_mayores_ventas(totales)
    print("\n" + "="*60)
    print(f" REGIÓN CON MAYORES VENTAS: {region_top} (${ventas_top:,.2f})")
    print("="*60)
    
    # Mostrar ventas por trimestre
    print("\n VENTAS ACUMULADAS POR TRIMESTRE:")
    print("-"*60)
    for trimestre, total in trimestres.items():
        print(f"{trimestre}: ${total:>12,.2f}")
    
    # Mostrar gran total
    print("\n" + "="*60)
    print(f" GRAN TOTAL DE VENTAS: ${gran_total:>30,.2f}")
    print("="*60 + "\n")

# Mostrar ventas detalladas por región (bonus)
def mostrar_detalle_por_region(ventas):
    """Muestra desglose detallado de ventas por región"""
    print("\n DETALLE DE VENTAS POR REGIÓN:")
    print("="*60)
    
    for region, trimestres in ventas.items():
        print(f"\n {region}:")
        for trimestre, monto in trimestres.items():
            print(f"   {trimestre}: ${monto:>12,.2f}")
        print(f"   {'-'*30}")
        print(f"   Total: ${sum(trimestres.values()):>12,.2f}")
    print("="*60)

# ===== DEMOSTRACIÓN DEL SISTEMA =====
if __name__ == "__main__":
    print("=== SISTEMA DE ANÁLISIS DE VENTAS ===\n")
    
    # Mostrar detalle por región
    mostrar_detalle_por_region(ventas_por_region)
    
    # Mostrar reporte completo
    mostrar_reporte_completo(ventas_por_region)
    
    # Bonus: jugando con comprensiones
    print(" EJEMPLOS DE COMPRENSIÓN DE DICCIONARIO:")
    
    # Si quisiéramos aumentar ventas 10%
    aumento = {region: {q: v*1.1 for q, v in datos.items()} 
               for region, datos in ventas_por_region.items()}
    print("✓ Comprensión anidada: aumentaría ventas 10%")
    
    # Filtrar regiones con más de 75,000
    totales = calcular_totales_anuales(ventas_por_region)
    top_regiones = {r: t for r, t in totales.items() if t > 75000}
    print(f"✓ Regiones con más de $75,000: {list(top_regiones.keys())}")