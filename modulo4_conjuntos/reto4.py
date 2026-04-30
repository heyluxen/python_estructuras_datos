# ==================== PARTE 1: TIENDAS ====================

# 1. Definir tienda_centro, tienda_norte y tienda_sur como sets de productos
tienda_centro = {"laptop", "mouse", "teclado", "monitor", "audifonos", "camara"}
tienda_norte = {"tablet", "mouse", "impresora", "monitor", "usb", "disco duro"}
tienda_sur = {"teclado", "mouse", "audifonos", "parlantes", "silla gamer", "monitor"}

# 2. Calcular catalogo_completo con union() y productos_comunes con intersection()
def analizar_catalogos():
    """Analiza los catalogos de las tres tiendas"""
    
    # Union de todos los productos (sin duplicados)
    catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
    
    # Interseccion de las tres tiendas (productos en todas)
    productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)
    
    return catalogo_completo, productos_comunes

# 3. Usar difference() para exclusivos de cada tienda e isdisjoint() para solapamientos
def exclusivos_por_tienda():
    """Encuentra productos exclusivos de cada tienda"""
    
    exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
    exclusivos_norte = tienda_norte.difference(tienda_centro, tienda_sur)
    exclusivos_sur = tienda_sur.difference(tienda_centro, tienda_norte)
    
    return exclusivos_centro, exclusivos_norte, exclusivos_sur

def verificar_solapamientos():
    """Verifica si hay solapamiento entre tiendas (comparten productos)"""
    
    centro_norte = not tienda_centro.isdisjoint(tienda_norte)
    centro_sur = not tienda_centro.isdisjoint(tienda_sur)
    norte_sur = not tienda_norte.isdisjoint(tienda_sur)
    
    return centro_norte, centro_sur, norte_sur

# ==================== PARTE 2: USUARIOS Y PELICULAS ====================

# 4. Definir usuario1, usuario2, usuario3 como sets de generos cinematograficos
usuario1 = {"accion", "aventura", "ciencia ficcion", "superheroes"}
usuario2 = {"comedia", "romance", "drama", "musical"}
usuario3 = {"accion", "comedia", "animacion", "aventura", "ciencia ficcion"}

def analizar_preferencias():
    """Analiza preferencias de usuarios usando operadores matematicos"""
    
    # 5. Usar & (interseccion) - generos comunes
    comunes_1_2 = usuario1 & usuario2
    comunes_1_3 = usuario1 & usuario3
    comunes_2_3 = usuario2 & usuario3
    comunes_todos = usuario1 & usuario2 & usuario3
    
    # 5. Usar | (union) - universo de generos
    universo_generos = usuario1 | usuario2 | usuario3
    
    # 5. Usar - (diferencia) - generos exclusivos
    exclusivos_1 = usuario1 - usuario2 - usuario3
    exclusivos_2 = usuario2 - usuario1 - usuario3
    exclusivos_3 = usuario3 - usuario1 - usuario2
    
    # 5. Usar ^ (diferencia simetrica) - generos que solo tiene uno de los dos
    dif_simetrica_1_2 = usuario1 ^ usuario2
    
    return (comunes_1_2, comunes_1_3, comunes_2_3, comunes_todos,
            universo_generos, exclusivos_1, exclusivos_2, exclusivos_3,
            dif_simetrica_1_2)

# 6. Usar <= (subconjunto) para verificar preferencias
def verificar_subconjuntos():
    """Verifica relaciones de subconjunto entre preferencias"""
    
    es_subconjunto_1_en_3 = usuario1 <= usuario3
    es_subconjunto_2_en_3 = usuario2 <= usuario3
    es_superconjunto_3_de_1 = usuario3 >= usuario1
    
    return es_subconjunto_1_en_3, es_subconjunto_2_en_3, es_superconjunto_3_de_1

# ==================== FUNCIONES PARA MOSTRAR RESULTADOS ====================

def mostrar_reporte_tiendas():
    """Muestra el analisis completo de las tiendas"""
    print("\n" + "="*60)
    print("ANALISIS DE CATALOGOS DE TIENDAS".center(60))
    print("="*60)
    
    print("\nCATALOGOS POR TIENDA:")
    print(f"   Centro: {tienda_centro}")
    print(f"   Norte:  {tienda_norte}")
    print(f"   Sur:    {tienda_sur}")
    
    catalogo_completo, productos_comunes = analizar_catalogos()
    print(f"\nCATALOGO COMPLETO (union): {len(catalogo_completo)} productos")
    print(f"   {catalogo_completo}")
    print(f"\nPRODUCTOS EN LAS 3 TIENDAS (interseccion): {productos_comunes}")
    
    exc_centro, exc_norte, exc_sur = exclusivos_por_tienda()
    print(f"\nPRODUCTOS EXCLUSIVOS (difference):")
    print(f"   Solo Centro: {exc_centro if exc_centro else 'ninguno'}")
    print(f"   Solo Norte:  {exc_norte if exc_norte else 'ninguno'}")
    print(f"   Solo Sur:    {exc_sur if exc_sur else 'ninguno'}")
    
    c_n, c_s, n_s = verificar_solapamientos()
    print(f"\nSOLAPAMIENTOS (isdisjoint = False si comparten):")
    print(f"   Centro <-> Norte: {'Comparten productos' if c_n else 'No comparten'}")
    print(f"   Centro <-> Sur:   {'Comparten productos' if c_s else 'No comparten'}")
    print(f"   Norte <-> Sur:    {'Comparten productos' if n_s else 'No comparten'}")

def mostrar_reporte_usuarios():
    """Muestra el analisis completo de preferencias de usuarios"""
    print("\n" + "="*60)
    print("ANALISIS DE PREFERENCIAS DE USUARIOS".center(60))
    print("="*60)
    
    print("\nPREFERENCIAS POR USUARIO:")
    print(f"   Usuario 1: {usuario1}")
    print(f"   Usuario 2: {usuario2}")
    print(f"   Usuario 3: {usuario3}")
    
    (comunes_1_2, comunes_1_3, comunes_2_3, comunes_todos,
     universo, exc_1, exc_2, exc_3, dif_sim) = analizar_preferencias()
    
    print(f"\nOPERADORES MATEMATICOS:")
    print(f"   & (interseccion) - Generos comunes:")
    print(f"      Usuario 1 ∩ Usuario 2: {comunes_1_2 if comunes_1_2 else 'ninguno'}")
    print(f"      Usuario 1 ∩ Usuario 3: {comunes_1_3}")
    print(f"      Usuario 2 ∩ Usuario 3: {comunes_2_3 if comunes_2_3 else 'ninguno'}")
    print(f"      Todos ∩: {comunes_todos if comunes_todos else 'ninguno'}")
    
    print(f"\n   | (union) - Universo de generos:")
    print(f"      Total generos unicos: {len(universo)}")
    print(f"      {universo}")
    
    print(f"\n   - (diferencia) - Generos exclusivos:")
    print(f"      Solo Usuario 1: {exc_1 if exc_1 else 'ninguno'}")
    print(f"      Solo Usuario 2: {exc_2 if exc_2 else 'ninguno'}")
    print(f"      Solo Usuario 3: {exc_3 if exc_3 else 'ninguno'}")
    
    print(f"\n   ^ (diferencia simetrica) - Usuario 1 △ Usuario 2:")
    print(f"      {dif_sim}")
    
    sub_1_3, sub_2_3, super_3_1 = verificar_subconjuntos()
    print(f"\nOPERADORES DE COMPARACION:")
    print(f"   Usuario 1 ⊆ Usuario 3? {sub_1_3}")
    print(f"   Usuario 2 ⊆ Usuario 3? {sub_2_3}")
    print(f"   Usuario 3 ⊇ Usuario 1? {super_3_1}")

def mostrar_recomendaciones():
    """Bonus: generar recomendaciones usando operadores de conjuntos"""
    print("\n" + "="*60)
    print("RECOMENDACIONES PERSONALIZADAS".center(60))
    print("="*60)
    
    recomendados = usuario1 - usuario3
    print(f"\nPara Usuario 3 (recomendaciones basadas en Usuario 1):")
    print(f"   Le gusta: {usuario3}")
    print(f"   Podria gustarle: {recomendados if recomendados else 'ya las tiene todas'}")
    
    populares = (usuario1 & usuario3) - usuario2
    print(f"\nPara Usuario 2 (tendencias que no conoce):")
    if populares:
        print(f"   Generos populares que no ve: {populares}")
    else:
        print(f"   Ya conoce todos los generos populares")

# ===================== DEMOSTRACION COMPLETA =====================

def reporte_integrado():
    """Imprime el resumen final integrado (requisito 6)"""
    print("\n" + "="*60)
    print("RESUMEN FINAL INTEGRADO".center(60))
    print("="*60)
    
    mostrar_reporte_tiendas()
    mostrar_reporte_usuarios()
    mostrar_recomendaciones()
    
    print("\n" + "="*60)
    print("ANALISIS COMPLETADO".center(60))
    print("="*60)

# ===================== EJECUCION =====================

if __name__ == "__main__":
    print("=== SISTEMA DE ANALISIS DE TIENDAS Y RECOMENDACIONES ===\n")
    reporte_integrado()