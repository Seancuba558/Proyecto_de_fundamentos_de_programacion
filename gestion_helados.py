import librerias

# Programa principal
codigos = []
sabores = []
volumenes = []
temperaturas = []
horas = []
operarios = []

opc = 0

while opc != 6:
        print("========================================")
        print("   SISTEMA BACCIO PERU SAC - MODULAR")
        print("========================================")
        print("1. Registrar Lote")
        print("2. Calcular Reposo")
        print("3. Imprimir Etiqueta")
        print("4. Reporte Ordenado y Consolidado")
        print("5. Guardar Producción (Archivo)")
        print("6. Salir")
        
        try:
            opc = int(input("Elija una alternativa: "))
        except ValueError:
            print(">> Error: Debe ingresar un número.")
            opc = 0
            
        if opc == 1:
            librerias.registrar_lote(codigos, sabores, volumenes, temperaturas, horas, operarios)
        elif opc == 2:
            librerias.calcular_reposo(codigos, volumenes)
        elif opc == 3:
            librerias.imprimir_etiqueta(codigos, sabores, volumenes, operarios, horas)
        elif opc == 4:
            librerias.ordenar_y_mostrar(codigos, sabores, volumenes)
        elif opc == 5:
            librerias.guardar_en_archivo(codigos, sabores, volumenes, temperaturas, horas, operarios)
        elif opc == 6:
            print("Guardando configuraciones... Saliendo del sistema.")
        else:
            if opc != 0:
                print("Alternativa inválida. Intente de nuevo.")
            
        if opc != 6:
            input("\nPresione Enter para continuar...")