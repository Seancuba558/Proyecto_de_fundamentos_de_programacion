def registrar_lote(cods, sabs, vols, temps, hrs, ops):
    print("--- REGISTRO DE NUEVO LOTE ---")
    cods.append(input("Ingrese Código del Lote (Ej. L001): "))
    sabs.append(input("Ingrese Sabor: "))
    vols.append(float(input("Ingrese Volumen (L): ")))
    temps.append(float(input("Ingrese Temp de extracción (°C): ")))
    hrs.append(input("Ingrese Hora (HH:MM): "))
    ops.append(input("Ingrese ID Operario: "))
    print(">> Lote registrado exitosamente.")



