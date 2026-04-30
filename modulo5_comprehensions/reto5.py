# ==================== DATASET DE VENTAS ====================

ventas = [
    {"producto": "laptop", "categoria": "electronica", "unidades": 20, "precio": 800},
    {"producto": "teclado", "categoria": "perifericos", "unidades": 50, "precio": 25},
    {"producto": "mouse", "categoria": "perifericos", "unidades": 30, "precio": 15},
    {"producto": "monitor", "categoria": "electronica", "unidades": 10, "precio": 200},
    {"producto": "silla gamer", "categoria": "muebles", "unidades": 5, "precio": 150},
    {"producto": "audifonos", "categoria": "perifericos", "unidades": 25, "precio": 45},
    {"producto": "webcam", "categoria": "electronica", "unidades": 8, "precio": 60},
    {"producto": "micrófono", "categoria": "electronica", "unidades": 12, "precio": 80}
]

# ==================== 1. LIST COMP: valor_total (unidades x precio) ====================
def calcular_valores_totales():
    """List comp: calcula valor_total (unidades * precio) por cada producto"""
    valores_totales = [venta["unidades"] * venta["precio"] for venta in ventas]
    return valores_totales

# ==================== 2. LIST COMP CON FILTRO: productos con valor_total > 1000 ====================
def productos_alto_valor():
    """List comp con filtro: nombres de productos con valor_total > 1000"""
    productos = [venta["producto"] for venta in ventas 
                 if (venta["unidades"] * venta["precio"]) > 1000]
    return productos

# ==================== 3. DICT COMP: producto_info {nombre: {valor, unidades}} ====================
def crear_producto_info():
    """Dict comp: mapea nombre -> {valor_total, unidades}"""
    producto_info = {
        venta["producto"]: {
            "valor_total": venta["unidades"] * venta["precio"],
            "unidades": venta["unidades"]
        }
        for venta in ventas
    }
    return producto_info

# ==================== 4. DICT COMP CON FILTRO: ranking_premium (precio > 50) ====================
def ranking_productos_premium():
    """Dict comp con filtro: productos con precio > 50, ordenado por valor_total desc"""
    premium = {
        venta["producto"]: venta["unidades"] * venta["precio"]
        for venta in ventas
        if venta["precio"] > 50
    }
    # Ordenar por valor_total descendente
    premium_ordenado = dict(sorted(premium.items(), key=lambda x: x[1], reverse=True))
    return premium_ordenado

# ==================== 5. SET COMP: categorias_unicas y productos_baratos ====================
def obtener_categorias_unicas():
    """Set comp: categorías únicas de todos los productos"""
    categorias_unicas = {venta["categoria"] for venta in ventas}
    return categorias_unicas

def obtener_productos_baratos():
    """Set comp: productos con precio <= 50"""
    productos_baratos = {venta["producto"] for venta in ventas if venta["precio"] <= 50}
    return productos_baratos

# ==================== 6. COMBINAR LAS TRES: resumen_formateado + gran_total ====================
def generar_resumen_formateado():
    """Combina comprehensions para generar resumen completo"""
    
    # List comp para totales individuales
    valores_totales = calcular_valores_totales()
    
    # Sum para gran_total
    gran_total = sum(valores_totales)
    
    # Dict comp para resumen de productos
    resumen_productos = {
        venta["producto"]: {
            "categoria": venta["categoria"],
            "unidades": venta["unidades"],
            "precio_unitario": venta["precio"],
            "valor_total": venta["unidades"] * venta["precio"]
        }
        for venta in ventas
    }
    
    # Set comp para estadísticas
    categorias = obtener_categorias_unicas()
    productos_top = set(productos_alto_valor())
    
    return {
        "gran_total": gran_total,
        "resumen_productos": resumen_productos,
        "categorias": categorias,
        "productos_top": productos_top
    }

# ==================== FUNCIONES PARA MOSTRAR RESULTADOS ====================

def mostrar_resultados():
    """Muestra todos los resultados del análisis"""
    
    print("\n" + "="*60)
    print("ANALISIS DE VENTAS CON COMPREHENSIONS".center(60))
    print("="*60)
    
    # 1. List comp: valores totales
    print("\n1. LIST COMP - VALOR TOTAL POR PRODUCTO:")
    print("   [unidades * precio para cada producto]")
    valores = calcular_valores_totales()
    for i, (venta, valor) in enumerate(zip(ventas, valores)):
        print(f"   {venta['producto']}: ${valor:,.2f}")
    
    # 2. List comp con filtro: productos con valor > 1000
    print("\n2. LIST COMP CON FILTRO - PRODUCTOS CON VALOR TOTAL > 1000:")
    altos = productos_alto_valor()
    if altos:
        for producto in altos:
            print(f"   - {producto}")
    else:
        print("   Ningun producto supera los $1000")
    
    # 3. Dict comp: producto_info
    print("\n3. DICT COMP - INFO POR PRODUCTO:")
    info = crear_producto_info()
    for producto, datos in info.items():
        print(f"   {producto}: {datos['unidades']} unidades, ${datos['valor_total']:,.2f}")
    
    # 4. Dict comp con filtro: ranking premium
    print("\n4. DICT COMP CON FILTRO - RANKING PREMIUM (precio > 50):")
    premium = ranking_productos_premium()
    if premium:
        for producto, valor in premium.items():
            print(f"   {producto}: ${valor:,.2f}")
    else:
        print("   No hay productos premium")
    
    # 5. Set comp: categorías únicas y productos baratos
    print("\n5. SET COMP - ANALISIS DE UNICIDAD:")
    categorias = obtener_categorias_unicas()
    print(f"   Categorías únicas: {categorias}")
    
    baratos = obtener_productos_baratos()
    print(f"   Productos baratos (precio <= 50): {baratos if baratos else 'ninguno'}")
    
    # 6. Combinar todo: resumen final + gran_total
    print("\n6. RESUMEN FINAL INTEGRADO:")
    resumen = generar_resumen_formateado()
    print(f"   GRAN TOTAL DE VENTAS: ${resumen['gran_total']:,.2f}")
    print(f"   Categorías disponibles: {len(resumen['categorias'])} categorías")
    print(f"   Productos top (valor > $1000): {len(resumen['productos_top'])} productos")
    
    print("\n" + "="*60)
    print("DETALLE COMPLETO DE VENTAS".center(60))
    print("="*60)
    
    print(f"\n{'Producto':<18} {'Categoria':<14} {'Unidades':<10} {'Precio':<12} {'Valor Total':<12}")
    print("-"*66)
    
    for venta in ventas:
        valor = venta["unidades"] * venta["precio"]
        print(f"{venta['producto']:<18} {venta['categoria']:<14} {venta['unidades']:<10} ${venta['precio']:<11,.2f} ${valor:<11,.2f}")
    
    print("-"*66)
    print(f"{'TOTAL':<18} {'':<14} {'':<10} {'':<12} ${sum(calcular_valores_totales()):<11,.2f}")
    print("="*60)

# ==================== BONUS: COMPARACION RENDIMIENTO ====================

def comparar_rendimiento():
    """Compara velocidad entre comprehension y bucle tradicional"""
    import time
    
    # Comprehension
    start = time.time()
    cuadrados_comp = [n**2 for n in range(1000000)]
    tiempo_comp = time.time() - start
    
    # Bucle tradicional
    start = time.time()
    cuadrados_bucle = []
    for n in range(1000000):
        cuadrados_bucle.append(n**2)
    tiempo_bucle = time.time() - start
    
    print("\n" + "="*60)
    print("RENDIMIENTO: COMPREHENSION vs BUCLE".center(60))
    print("="*60)
    print(f"   Comprehension: {tiempo_comp:.4f} segundos")
    print(f"   Bucle:         {tiempo_bucle:.4f} segundos")
    print(f"   La comprehension es {(tiempo_bucle/tiempo_comp):.2f}x más rápida")
    print("="*60)

# ==================== EJECUCION ====================

if __name__ == "__main__":
    print("=== SISTEMA DE ANALISIS DE VENTAS CON COMPREHENSIONS ===\n")
    mostrar_resultados()
    comparar_rendimiento()