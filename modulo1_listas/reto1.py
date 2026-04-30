# Definir inventario con tres productos [nombre, cantidad, precio]
# Definir inventario con tres productos [nombre, cantidad, precio]
inventario = [
    ["manzanas", 50, 2500],
    ["peras", 30, 3000],
    ["naranjas", 40, 2000]
]

def actualizar_precio(producto, nuevo_precio):
    """Actualiza el precio de un producto específico"""
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio
            print(f"✓ Precio de {producto} actualizado a ${nuevo_precio:,.0f} COP")
            return
    print(f"✗ Producto '{producto}' no encontrado")

def registrar_venta(producto, cantidad):
    """Descuenta stock si hay suficiente cantidad disponible"""
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] -= cantidad
                total_venta = cantidad * item[2]
                print(f"✓ Venta registrada: {cantidad} {producto}(s) - Total: ${total_venta:,.0f} COP")
                print(f"  Stock restante de {producto}: {item[1]} unidades")
            else:
                print(f"✗ Stock insuficiente de {producto}. Disponible: {item[1]}, Solicitado: {cantidad}")
            return
    print(f"✗ Producto '{producto}' no encontrado")

def anadir_producto(producto, cantidad, precio):
    """Añade un nuevo producto o actualiza stock si ya existe"""
    for item in inventario:
        if item[0] == producto:
            # Producto existe - actualizar stock
            item[1] += cantidad
            # Opcional: actualizar precio si se proporciona
            if precio != item[2]:
                item[2] = precio
            print(f"✓ Producto '{producto}' actualizado: +{cantidad} unidades, nuevo stock: {item[1]}")
            return
    
    # Producto no existe - añadir nuevo
    inventario.append([producto, cantidad, precio])
    print(f"✓ Nuevo producto '{producto}' añadido con {cantidad} unidades a ${precio:,.0f} COP")

def mostrar_inventario():
    """Muestra el estado actual del inventario de forma organizada"""
    print("\n" + "="*65)
    print("INVENTARIO ACTUAL".center(65))
    print("="*65)
    print(f"{'Producto':<15} {'Stock':<10} {'Precio Unitario':<18} {'Valor Total':<15}")
    print("-"*65)
    
    valor_total_inventario = 0
    for producto, cantidad, precio in inventario:
        valor_producto = cantidad * precio
        valor_total_inventario += valor_producto
        print(f"{producto:<15} {cantidad:<10} ${precio:>15,.0f} COP  ${valor_producto:>13,.0f} COP")
    
    print("-"*65)
    print(f"Valor total del inventario: ${valor_total_inventario:>38,.0f} COP")
    print("="*65 + "\n")

# ===== DEMOSTRACIÓN DEL SISTEMA =====
print("=== SISTEMA DE INVENTARIO ===\n")

# Mostrar inventario inicial
print("Inventario inicial:")
mostrar_inventario()

# Llamar a actualizar_precio con el segundo producto (peras)
print("1. Actualizando precio de peras...")
actualizar_precio("peras", 3500)

# Llamar a registrar_venta con el primer producto (manzanas)
print("\n2. Registrando venta de manzanas...")
registrar_venta("manzanas", 15)

# Llamar a anadir_producto con un producto nuevo
print("\n3. Añadiendo nuevo producto...")
anadir_producto("uvas", 25, 4000)

# También probar actualizar stock de producto existente
print("\n4. Añadiendo más stock a naranjas...")
anadir_producto("naranjas", 20, 2000)

# Llamar a mostrar_inventario final
mostrar_inventario()