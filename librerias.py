def registrar_lote(cods, sabs, vols, temps, hrs, ops):
    print("--- REGISTRO DE NUEVO LOTE ---")
    cods.append(input("Ingrese Código del Lote (Ej. L001): "))
    sabs.append(input("Ingrese Sabor: "))
    vols.append(float(input("Ingrese Volumen (L): ")))
    temps.append(float(input("Ingrese Temp de extracción (°C): ")))
    hrs.append(input("Ingrese Hora (HH:MM): "))
    ops.append(input("Ingrese ID Operario: "))
    print(">> Lote registrado exitosamente.")

def calcular_reposo(cods, vols):
    buscar_cod = input("Ingrese código a calcular: ")
    indice = -1

    for i in range(len(cods)):
        if cods[i] == buscar_cod:
            indice = i
            break

    if indice != -1:
        reposo = 2.0 + (vols[indice] / 10.0) * 0.5
        print(f"El lote requiere {reposo:.2f} horas de reposo.")
    else:
        print(">> Error: Lote no encontrado.")

def imprimir_etiqueta(cods, sabs, vols, ops, hrs):
    buscar_cod = input("Ingrese el código del lote a imprimir: ")
    indice = -1
    
    # Búsqueda secuencial
    for i in range(len(cods)):
        if cods[i] == buscar_cod:
            indice = i
            break
            
    if indice != -1:
        print("-" * 35)
        print("       ETIQUETA DE PRODUCCIÓN      ")
        print("-" * 35)
        print(f"LOTE:     {cods[indice]}")
        print(f"SABOR:    {sabs[indice]}")
        print(f"VOLUMEN:  {vols[indice]} Litros")
        print(f"OPERARIO: {ops[indice]}")
        print(f"HORA:     {hrs[indice]}")
        print("-" * 35)
    else:
        print(">> Error: Código de lote no encontrado.")

def ordenar_y_mostrar(cods, sabs, vols):
    total = len(cods)
    if total == 0:
        print(">> No hay lotes registrados para ordenar.")
        return

    # Algoritmo de Ordenamiento Burbuja (Mayor a Menor Volumen)
    for i in range(total - 1):
        for j in range(total - i - 1):
            if vols[j] < vols[j+1]:
                # Intercambiar Volumen
                vols[j], vols[j+1] = vols[j+1], vols[j]
                # Intercambiar Códigos paralelos
                cods[j], cods[j+1] = cods[j+1], cods[j]
                # Intercambiar Sabores paralelos
                sabs[j], sabs[j+1] = sabs[j+1], sabs[j]
                
    print("--- REPORTE CONSOLIDADO (ORDENADO POR VOLUMEN) ---")
    for i in range(total):
        print(f"{i+1}. Lote: {cods[i]} | Sabor: {sabs[i]} | Vol: {vols[i]} L")

def guardar_en_archivo(cods, sabs, vols, temps, hrs, ops):
    total = len(cods)
    if total == 0:
        print(">> No hay datos para guardar.")
        return
        
    print(">> Abriendo archivo produccion_lotes.txt...")
    try:
        # Crea y escribe en un archivo de texto real de forma persistente
        with open("produccion_lotes.txt", "w", encoding="utf-8") as archivo:
            archivo.write("REPORTE DE PRODUCCIÓN - BACCIO PERU SAC\n")
            archivo.write("=" * 55 + "\n")
            for i in range(total):
                linea = f"Lote: {cods[i]} | Sabor: {sabs[i]} | Vol: {vols[i]}L | Temp: {temps[i]}°C | Hora: {hrs[i]} | Op: {ops[i]}\n"
                archivo.write(linea)
                
        print(f">> Escribiendo {total} registros estructurados...")
        print(">> Archivo cerrado. Datos guardados de forma persistente.")
    except Exception as e:
        print(f">> Error al guardar el archivo: {e}")

