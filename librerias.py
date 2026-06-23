def registrar_lote(cods, sabs, vols, temps, hrs, ops):
    print("\n--- REGISTRO DE NUEVO LOTE ---")

    codigo = input("Ingrese Código del Lote: ")
    sabor = input("Ingrese Sabor: ")
    volumen = float(input("Ingrese Volumen (L): "))
    temperatura = float(input("Ingrese Temp de extracción: "))
    hora = input("Ingrese Hora (HH:MM): ")
    operario = input("Ingrese ID Operario: ")

    cods.append(codigo)
    sabs.append(sabor)
    vols.append(volumen)
    temps.append(temperatura)
    hrs.append(hora)
    ops.append(operario)

    print(">> Lote registrado exitosamente.")

