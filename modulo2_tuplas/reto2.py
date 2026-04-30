# 1. Definir catalogo como tupla de tuplas (titulo, director, año, puntuacion)
catalogo = (
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2),
    ("Cadena Perpetua", "Frank Darabont", 1994, 9.3),
    ("El Caballero de la Noche", "Christopher Nolan", 2008, 9.0),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9),
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8),
    ("Matrix", "Hermanas Wachowski", 1999, 8.7),
    ("El Señor de los Anillos", "Peter Jackson", 2001, 8.9)
)

# 2. Función para mostrar todas las películas con desempaquetado
def mostrar_catalogo():
    """Muestra todo el catálogo desempaquetando cada película"""
    print("\n" + "="*70)
    print("CATÁLOGO DE PELÍCULAS".center(70))
    print("="*70)
    print(f"{'Título':<30} {'Director':<25} {'Año':<6} {'Puntuación':<10}")
    print("-"*70)
    
    for pelicula in catalogo:
        titulo, director, año, puntuacion = pelicula  # Desempaquetado básico
        print(f"{titulo:<30} {director:<25} {año:<6} {puntuacion:<10.1f}")
    print("="*70 + "\n")

# 3. Función que usa el operador * para separar primera película del resto
def separar_catalogo():
    """Separa la primera película del resto usando el operador *"""
    # Desempaquetado con *resto
    primera, *resto = catalogo
    titulo, director, año, puntuacion = primera
    
    print("\n" + "="*50)
    print("PRIMERA PELÍCULa".center(50))
    print("="*50)
    print(f"Título: {titulo}")
    print(f"Director: {director}")
    print(f"Año: {año}")
    print(f"Puntuación: {puntuacion}")
    print("\n" + "="*50)
    print(f"RESTO DEL CATÁLOGO ({len(resto)} películas)".center(50))
    print("="*50)
    
    for pelicula in resto:
        tit, dir, ano, punt = pelicula
        print(f"• {tit} ({ano}) - {dir} - {punt}/10")
    print("="*50 + "\n")

# 4. Implementar buscar_por_director() que devuelva tupla de coincidencias
def buscar_por_director(director_buscar):
    """Busca películas por director y retorna tupla de coincidencias"""
    coincidencias = []
    
    for pelicula in catalogo:
        titulo, director, año, puntuacion = pelicula
        if director.lower() == director_buscar.lower():
            coincidencias.append(pelicula)
    
    return tuple(coincidencias)  # Convertir a tupla

# 5. Implementar obtener_estadisticas() retornando (min, max, promedio)
def obtener_estadisticas():
    """Calcula y retorna estadísticas de puntuaciones (min, max, promedio)"""
    puntuaciones = []
    
    for pelicula in catalogo:
        _, _, _, puntuacion = pelicula  # Usamos _ para descartar lo que no necesitamos
        puntuaciones.append(puntuacion)
    
    if not puntuaciones:
        return (0, 0, 0)
    
    min_punt = min(puntuaciones)
    max_punt = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    
    return (min_punt, max_punt, promedio)  # Retorna tupla de 3 valores

# 6. Función adicional para mostrar búsquedas con desempaquetado en bucle
def mostrar_busqueda(director):
    """Muestra los resultados de búsqueda usando desempaquetado"""
    resultados = buscar_por_director(director)
    
    print(f"\n Películas de {director}:")
    if resultados:
        for pelicula in resultados:
            titulo, _, año, puntuacion = pelicula  # Desempaquetado con _ para ignorar director
            print(f"   • {titulo} ({año}) - {puntuacion}/10")
    else:
        print(f"   No se encontraron películas de {director}")

# ===== DEMOSTRACIÓN DEL SISTEMA =====
print("=== SISTEMA DE CATÁLOGO DE PELÍCULAS ===\n")

# Mostrar catálogo completo con desempaquetado
mostrar_catalogo()

# Usar operador * para separar primera película del resto
separar_catalogo()

# Buscar películas por director
print("\n" + "="*50)
print("BÚSQUEDA POR DIRECTOR".center(50))
print("="*50)
mostrar_busqueda("Christopher Nolan")
mostrar_busqueda("Quentin Tarantino")
mostrar_busqueda("Steven Spielberg")

# Implementar obtener_estadisticas y desempaquetar el retorno
print("\n" + "="*50)
print("ESTADÍSTICAS DEL CATÁLOGO".center(50))
print("="*50)

# 6. Desempaquetar el retorno de obtener_estadisticas()
min_puntuacion, max_puntuacion, promedio_puntuacion = obtener_estadisticas()

# También podemos usar * para desempaquetar directamente en print
print(f" Puntuación más baja:  {min_puntuacion:.1f}/10")
print(f" Puntuación más alta:  {max_puntuacion:.1f}/10")
print(f" Puntuación promedio:  {promedio_puntuacion:.2f}/10")
print("="*50)

# Bonus: Uso de enumerate con desempaquetado
print("\n" + "="*50)
print("TOP 3 MEJORES PELÍCULAS".center(50))
print("="*50)

# Ordenar para mostrar las mejores
mejores = sorted(catalogo, key=lambda x: x[3], reverse=True)[:3]
for i, (titulo, director, año, puntuacion) in enumerate(mejores, 1):
    print(f"{i}. {titulo} - {director} ({año}) - {puntuacion}/10")
print("="*50)