"""
    ESTADO DEL JUEGO

"""
juego_activo = True
habitacion_actual = "Recepcion"
inventario = []
energia = False
codigo_descubierto = False
tarjeta_obtenida = False
salida_abierta = False

while juego_activo == True:
    if habitacion_actual == "Recepcion":
        print("="* 40)
        print("RECEPCION")
        print("="* 40)
        print("Te encuentras en la entrada del laboratorio")
        print()
        print("¿Qué deseas hacer?:")
        print("1. Ir al almacén")
        print("2. Ir a la sala de servidores")
        print("3. Revisar inventario")
        print("4. Salir del juego")
        opcion = input("Opcion: ")
        if opcion == "1":
            habitacion_actual = "Almacen"
        elif opcion == "2":
            habitacion_actual = "Sala de servidores"
        elif opcion == "3":
            print()
            if len(inventario) == 0:
                print("Tu inventario está vacío")
            else: 
                for objeto in inventario:
                    print("-", objeto)
        elif opcion == "4":
            juego_activo = False
        else:
            print("Opcion no valida")
    
    elif habitacion_actual == "Almacen":
        print()
        print("=" * 40)
        print("ALMACÉN")
        print("=" * 40)

        print("Hay muchas cajas viejas.")
        print("También observas un gabinete de herramientas.")
        print()

        # Solo este mensaje depende del inventario
        if "Llave inglesa" not in inventario:
            print("Sobre una mesa encuentras una llave inglesa.")
        else:
            print("Ya no queda nada útil sobre la mesa.")

        print()
        print("1. Tomar llave inglesa")
        print("2. Volver a recepción")

        opcion = input("Opción: ")

        if opcion == "1":

            if "Llave inglesa" not in inventario:

                inventario.append("Llave inglesa")
                print("Has guardado la llave inglesa.")

            else:

                print("Ya tienes ese objeto.")

        elif opcion == "2":

            habitacion_actual = "Recepcion"

        else:

            print("Opción inválida.")
    
    elif habitacion_actual == "Sala de servidores":
        print()
        print("=" * 40)
        print("SALA DE SERVIDORES")
        print("=" * 40)

        if energia:
            print("Las luces están encendidas.")
        else:
            print("Todo está apagado.")

        print()
        print("¿Qué deseas hacer?")
        print("1. Revisar gabinete eléctrico")
        print("2. Ir al laboratorio")
        print("3. Volver a recepción")

        opcion = input("Opción: ")

        if opcion == "1":

            if "Llave inglesa" in inventario:

                if energia:

                    print("La energía ya fue restablecida.")

                else:

                    print("Abres el gabinete eléctrico.")
                    print("La energía ha sido restablecida.")

                    energia = True

            else:

                print("Necesitas una herramienta.")

        elif opcion == "2":

            if energia:

                habitacion_actual = "Laboratorio IA"

            else:

                print("La puerta no funciona sin electricidad.")

        elif opcion == "3":

            habitacion_actual = "Recepcion"

        else:

            print("Opción inválida.")

    elif habitacion_actual == "Laboratorio IA":
        print()
        print("="* 40)
        print("LABORATORIO")
        print("="* 40)

        print("Te encuentras en el corazón del laboratorio")
        print("Aqui se desarrollaba una poderosa inteligencia artifical")
        print()
        print("Al fondo observas una enorme puerta metalica")
        print("Sobre ella se puede leer: ")
        print("SALIDA DE EMERGENCIA ")
        print()

        print("Que deseas hacer?")
        print("1. Resolver el acertijo de la IA")
        print("2. Revisar la computadora")
        print("3. Ir a la puerta de salida")
        print("4. Volver a la sala de servidores")    
        opcion = input("opcion:")
        if opcion == "1":
            if tarjeta_obtenida == True:
                print()
                print("La inteligencia artificial ya fue superada")
            else:
                print()
                print("La IA dice:")
                print()
                print("¿Qué numero continua la secuencia?:")
                print("2")
                print("4")
                print("8")
                print("16")
                print("?")

                respuesta = input("Respuesta: ")
                if respuesta == "32":
                    print("La IA repsonde:")
                    print("Respuesta correcta")
                    print()

                    print("Obtienes una tarjeta magnética")
                    inventario.append("Tarjeta magnetica")
                    tarjeta_obtenida = True
                else:
                    print()
                    print("La IA repsonde:")
                    print("Respuesta incorrecta")

        elif opcion == "2":
            if energia == True:
                if codigo_descubierto == True:
                    print("")
                    print("Ya conoces el código de emergencia")
                else:
                    print()
                    print("la computadora inicia...")
                    print()
                    print("CODIGO DE EMERGENCIA")
                    print("314")
                    codigo_descubierto = True
                
            else:
                print("La computadora no tiene energia")
        elif opcion == "3":
            habitacion_actual = "Salida"
        elif opcion == "4":
            habitacion_actual = "Sala de servidores"
        else:
            print()
            print("Opcion no valida")

    elif habitacion_actual == "Salida":
        print()
        print("=" * 40)
        print("PUERTA PRICIPAL DE SALIDA")
        print("=" * 40)
        if tarjeta_obtenida == True and codigo_descubierto == True:
            codigo = input("Introduce el código: ")
            if codigo == "314":
                print()
                print("La puerta se abre lentamente")
                print("has escapado del laboratorio")
                juego_activo = False
            else:
                print("Código incorrecto")
        else:
            print()
            print("Todavia no puedes escapar")
            print("Explora el laboratorio")