import librerias


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


def guardar_en_archivo(cods, sabs, vols, temps):
    with open("produccion_lotes.txt", "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE DE LOTES\n")
        archivo.write("=" * 40 + "\n")

        for i in range(len(cods)):
            archivo.write(
                f"Lote: {cods[i]} | "
                f"Sabor: {sabs[i]} | "
                f"Volumen: {vols[i]} L | "
                f"Temperatura: {temps[i]} °C\n"
            )

    print(">> Archivo cerrado. Datos guardados con éxito.")


# Programa principal
codigos = []
sabores = []
volumenes = []
temperaturas = []
horas = []
operarios = []

opc = 0

while opc != 6:
    print("\n========================================")
    print(" SISTEMA BACCIO PERU SAC - MODULAR")
    print("========================================")
    print("1. Registrar Lote")
    print("2. Calcular Reposo")
    print("3. Mostrar Reporte")
    print("4. Validar Consistencia")
    print("5. Guardar en Archivo")
    print("6. Salir")

    try:
        opc = int(input("Elija una alternativa: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if opc == 1:
        librerias.registrar_lote(
            codigos,
            sabores,
            volumenes,
            temperaturas,
            horas,
            operarios
        )

    elif opc == 2:
        calcular_reposo(codigos, volumenes)

    elif opc == 3:
        print("\n--- REPORTE ---")

        if len(codigos) == 0:
            print("No hay lotes registrados.")
        else:
            for i in range(len(codigos)):
                print(
                    f"{i+1}. Lote: {codigos[i]} | "
                    f"Vol: {volumenes[i]} L"
                )

    elif opc == 4:
        temp_actual = float(input("Ingrese temperatura actual (°C): "))

        if temp_actual > -4.0:
            print(">> ALERTA: Consistencia en riesgo (Overrun).")
        else:
            print(">> Temperatura óptima.")

    elif opc == 5:
        guardar_en_archivo(
            codigos,
            sabores,
            volumenes,
            temperaturas
        )

    elif opc == 6:
        print("Saliendo del sistema...")

    else:
        print("Alternativa inválida.")