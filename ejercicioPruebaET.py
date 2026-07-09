arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            mostrar_menu()
            opcion = int(input("Ingrese opción: "))
            if opcion > 0 and opcion <=6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
    
def buscar_codigo(pCodigo, pDiccionario):
    pCodigo = pCodigo.strip().upper()
    for codigo in pDiccionario.keys():
        if codigo == pCodigo:
            return True
    return False

def actualizar_precio(pCodigo, nuevo_precio, pBodegas):
    pCodigo = pCodigo.strip().upper()
    if buscar_codigo(pCodigo, pBodegas):
        pBodegas[pCodigo][0] = nuevo_precio
        return True
    else:
        return False

def unidades_tipo(pTipoBuscado, pArreglos, pBodegas):
    pTipoBuscado = pTipoBuscado.strip().lower()
    total = 0
    for codigo, values in pArreglos.items():
        if values[1] == pTipoBuscado:
            for codigoBodega, valuesBodega in pBodegas.items():
                if codigo == codigoBodega:
                    total += valuesBodega[1]
                    break
    print(f"El total de unidades disponibles es:{total}")

def busqueda_precio(pmin, pmax, pBodegas, pArreglos):
    resultados = []
    for codigoBodega, datosBodega in pBodegas.items():
        precio = datosBodega[0]
        stock = datosBodega[1]
        if pmin <= precio <= pmax and stock > 0:
            for codigo, datos in pArreglos.items():
                if codigo == codigoBodega:
                    nombre = datos[0]
                    resultados.append(f"{nombre}--{codigoBodega}")
    if len(resultados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        resultados.sort()
        #print(f"Los arreglos encontrados: {resultados}")
        for elemento in resultados:
            print(elemento)


def validar_codigo(pCodigo, pArreglos, pBodegas):
    
    pCodigo = pCodigo.strip().upper()
    if pCodigo == "":
        return False
    if pCodigo in pArreglos or pCodigo in pBodegas:
        return False
    return True
    

def validar_nombre(pNombre):
    
    pNombre = pNombre.strip()
    if pNombre == "":
        return False
    return True
    
def validar_tipo(pTipo):
    pTipo = pTipo.strip().lower()
    if pTipo == "":
        return False
    return True

def validar_color(pColor):
    pColor = pColor.strip().lower()
    if pColor == "":
        return False
    return True

def validar_tamano(pTamano):
    pTamano = pTamano.strip().upper()
    if pTamano == "":
        return False
    if pTamano in ("S", "M", "L"):
        return True
    return False
    
def validar_tarjeta(pTarjeta):
    pTarjeta = pTarjeta.strip().lower()
    if pTarjeta != "s":
        return False
    return True

def validar_temporada(pTemporada):
    pTemporada = pTemporada.strip().lower()
    if pTemporada == "":
        return False
    return True

def validar_precio(pPrecio):
    try:
        precioNumerico = int(pPrecio)
        if precioNumerico > 0:
            return True
        return False
    except ValueError:
        return False

def validar_unidades(pUnidades):
    try:
        UnidadesNumerico = int(pUnidades)
        if UnidadesNumerico >= 0:
            return True
        return False
    except ValueError:
        return False
    
def agregar_arreglo(pCodigo, pNombre, pTipo, pColor, pTamano, pTarjeta, pTemporada, pPrecio, pUnidades, pArreglos, pBodegas):
    pCodigo = pCodigo.strip().upper()
    if pCodigo in pArreglos:
        return False
    pArreglos[pCodigo] = [
        pNombre.strip(),
        pTipo.strip(),
        pColor.strip(),
        pTamano.strip().upper(),
        pTarjeta,
        pTemporada.strip()
    ]
    pBodegas[pCodigo] = [int(pPrecio), int(pUnidades)]
    return True

def eliminar_arreglo(pCodigo, pArreglos, pBodegas):
    pCodigo = pCodigo.strip().upper()

    if buscar_codigo(pCodigo, pArreglos):
        del pArreglos[pCodigo]
        del pBodegas[pCodigo]
        return True
    else:
        return False


while True:
    opcionSeleccionada = leer_opcion()
    try:
        if opcionSeleccionada == 1:
            tipoBuscado = input("Ingrese el tipo de arreglo a buscar: ")
            unidades_tipo(tipoBuscado, arreglos, bodega)


        elif opcionSeleccionada == 2:
            while True:
                try:
                    precioMinimo = int(input("Ingrese precio mínimo: "))
                    precioMaximo = int(input("Ingrese precio máximo: "))
                    if precioMinimo < 0 or precioMaximo < 0 or precioMinimo > precioMaximo:
                        print("Debe ingresar valores enteros")
                    else:
                        busqueda_precio(precioMinimo, precioMaximo, bodega, arreglos)
                        break

                except ValueError:
                    print("Debe ingresar valores enteros")



        elif opcionSeleccionada == 3:
            while True:
                Codigo = input("Ingrese el código del arreglo a cambiar precio: ").strip().upper()
                while True:
                    try:
                        nuevoPrecio = int(input("Ingrese nuevo precio: "))
                        if nuevoPrecio <= 0:
                            print("Debe ingresar valores enteros")
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar valores enteros")
                if actualizar_precio(Codigo, nuevoPrecio, bodega):
                    print("Precio actualizado.")
                else:
                    print("El codigo no existe")
                otroIntento = input("Desea actualizar otro precio (s/n)?: ").strip().lower()
                if otroIntento != "s":
                    break
                
        elif opcionSeleccionada == 4:
            codigo = input("Ingrese código: ")
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo: ")
            color = input("Ingrese color: ")
            tamano = input("Ingrese tamaño: ")
            tarjeta = input("¿Incluye tarjeta (s/n)?: ")
            temporada = input("Ingrese temporada: ")
            precio = input("Ingrese precio: ")
            unidades = input("Ingrese unidades: ")

            if not validar_codigo(codigo, arreglos, bodega):
                print("Código inválido o ya existe")
            elif not validar_nombre(nombre):
                print("Nombre inválido")
            elif not validar_tipo(tipo):
                print("Tipo inválido")
            elif not validar_color(color):
                print("Color inválido")
            elif not validar_tamano(tamano):
                print("Tamaño inválido")
            elif not validar_temporada(temporada):
                print("Temporada inválida")
            elif not validar_precio(precio):
                print("Precio inválido")
            elif not validar_unidades(unidades):
                print("Unidades inválidas")
            else:
                if agregar_arreglo(codigo, nombre, tipo, color, tamano, tarjeta, temporada, precio, unidades, arreglos, bodega):
                    print("Arreglo agregado")
                else:
                    print("El código ya existe")  

        elif opcionSeleccionada == 5:
            Codigo = input("Ingrese el código del arreglo a eliminar: ")
            if eliminar_arreglo(Codigo, arreglos, bodega):
                print("Arreglo eliminado")
            else:
                print("El código no existe")

        elif opcionSeleccionada == 6:
            print("Programa finalizado")
            break
    except ValueError:
        print("Debe seleccionar una opción válida (del 1 al 6)")