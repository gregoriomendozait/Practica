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
    print("""========== MENÚ PRINCIPAL ==========
1. Unidades por tipo de arreglo
2. Búsqueda de arreglos por rango de precio
3. Actualizar precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
=====================================""")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion > 6 or opcion < 1:
                print("Debe seleccionar una opción válida")
            else:
                return opcion
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_tipo(pTipo, pArreglos, pBodegas):
    total = 0
    pTipo = pTipo.lower().strip()
    for codigo, datos_arreglo in pArreglos.items():
        if pTipo == datos_arreglo[1]:
            for codigoBodega, datos_bodega in pBodegas.items():
                if codigo == codigoBodega:
                    total += datos_bodega[1]
                    break
    print(f"El total de unidades disponibles es:{total} ")

def busqueda_precio(pmin, pmax, pBodegas, pArreglos):
    resultados = []
    for codigobodega, datosbodega in pBodegas.items():
        precio = datosbodega[0]
        unidades = datosbodega[1]

        if pmin <= precio <= pmax and unidades > 0:
           for codigoarreglos, datosarreglos in pArreglos.items():
                if codigoarreglos == codigobodega:
                    nombre = datosarreglos[0]
                    resultados.append(f"{nombre}--{codigobodega}")
    if len(resultados) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        resultados.sort()
        print(f"Los arreglos encontrados son:{resultados}")
        # for arreglo in resultados:
        #     print(arreglo)
#repasar las siguientes 2 def
def buscar_codigo(pCodigo, Diccionario):
    pCodigo = pCodigo.strip().upper()
    for codigo in Diccionario.keys():
        if codigo == pCodigo:
            return True
    return False

def actualizar_precio(pCodigo, pnuevo_precio, pBodegas):
    pCodigo = pCodigo.strip().upper()
    if buscar_codigo(pCodigo, pBodegas):
        pBodegas[pCodigo][0] = pnuevo_precio
        return True
    return False

while True:
    mostrar_menu()
    opcionSelecionada = leer_opcion()
    if opcionSelecionada == 1:
        tipoBuscado = input("Ingrese el tipo de arreglo a consultar: ")
        unidades_tipo(tipoBuscado,arreglos, bodega)

    elif opcionSelecionada == 2:
        while True:
            try:
                preciominimo = int(input("Ingrese precio mínimo: "))
                preciomaximo = int(input("Ingrese precio máximo: "))
                if preciominimo < 0 or preciomaximo < 0 or preciominimo > preciomaximo:
                    print("Debe ingresar valores enteros")
                else:
                    busqueda_precio(preciominimo, preciomaximo, bodega, arreglos)
                    break

            except ValueError:
                print("Debe ingresar valores enteros")
    elif opcionSelecionada == 3:
        #repasar
        while True:
            Codigo = input("Ingrese el código del arreglo: ").strip().upper()
            while True:
                try:
                    NuevoPrecio = int(input("Ingrse nuevo precio: "))
                    if NuevoPrecio <= 0:
                        print("Debe ingresar valores enteros")
                    else: break
                except ValueError:
                    print("Debe ingresar valores enteros")
            if actualizar_precio(Codigo, NuevoPrecio, bodega):
                print("Precio actualizado")
            else:
                print("El código no existe")
            otravez = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
            if otravez != "s":
                break
    elif opcionSelecionada == 4:
        pass
    elif opcionSelecionada == 5:
        pass
    elif opcionSelecionada == 6:
        print("Programa finalizado.")
        break