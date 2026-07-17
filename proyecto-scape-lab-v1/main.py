# ==========================================
# ETAPA 1
# SALIDA POR CONSOLA
# ------------------------------------------
print("=" * 50)
print("            MISION PYTHON: ESCAPE LAB")
print("=" * 50)

print()
print("Has despertado dentro de un laboratorio secreto.")
print("No recuerdas cómo llegaste hasta aquí.")
print("Las luces parpadean lentamente.")
print("Todas las puertas parecen estar bloqueadas.")
print()

#============================================
# ETAPA 2
# VARIABLES: RECORDAR INFORMACIÓN
#============================================

nombre = input("Antes de comenzar, ¿cual es tu nombre?: ")
print()

print(f"Bienvenido(a), {nombre}")
print("Tu misión será encontrar la salida del laboratorio.")
print()

#============================================
# ETAPA 3
# TIPOS DE DATOS
#============================================
print("Selecciona la dificultad")

print("1. Fácil")
print("2. Normal")
print("3. Difícil")
dificultad = int(input("Opción: "))
print()

#============================================
# ETAPA 4
# TOMA DE DECISIONES: CONDICIONALES
#============================================
if dificultad == 1:
    print("Has elegido la dificultad fácil.")
    print("Recibirás pistas durante el juego")

elif dificultad == 2:
    print("Has elegido la dificultad normal")

elif dificultad == 3:
    print("Has elegido la dificultad difícil")
    print("No recibirás ayuda durante el juego.")

else:
    print("La opcion no existe")
    print("Se utilizará la dificultad normal.")
    dificultad = 2
print()

#============================================
# ETAPA 5
# VARIABLES BOOLEANAS: para constituir el estado del juego.
#============================================

# Estado inicial del juego
juego_activo = True
llave = False
tarjeta = False
codigo_descubierto = False

print("El laboratorio está listo")
print()

#============================================
# ETAPA 6
# Almacenar diversos valores en un mismo espacio de memoria
# LISTAS
#============================================
inventario = [] # todo corchete en python es una lista
print("Tu invetario está vacío")
print(inventario)
print()

#============================================
# ETAPA 7
# Darle la capacidad al video juego que se reinicie y no termine hasta decidirlo.
# Ciclos: while y for
#============================================

while juego_activo == True: # Ciclo while es una estructura que repetirá las veces que sea necesario, pero no sabemos cuantas veces serán. Ciclo INDETERMINADO.

    print()
    print("=" * 40)
    print("LABORATORIO - Recepción")
    print("="* 40)

    print("1. Explorar recepción")
    print("2. Revisar inventario")
    print("3. Intentar abrir la puerta de salida")
    print("4. Salir del juego")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print()
        print("Exploras cuidadosamente la recepción")

        if not llave: # Si llave guarda el valor: False
            print("Encuentras una pequeña llave.")
            print("La guardas en el inventario")
            llave = True
            inventario.append("LLave") # agregamos al inventario una llave
        
        elif not tarjeta:
            print("Despues de seguir buscando")
            print("Encuentras una tarjeta magnetica")
            tarjeta = True
            inventario.append("Tarjeta magnetica")
        
        elif not codigo_descubierto:
            print("Encuentras una nota.")
            print()
            print("La nota dice:")
            print("Código de emergencia: 314")
            codigo_descubierto = True
            inventario.append("Codigo descubierto")
        else:
            print("No encuentras nada más...")

    elif opcion == "2":
        print()
        print("Inventario:")
        if len(inventario) == 0:
            print("No tienes objetos actualmente en el inventario")
        else:
            for objeto in inventario:
                print("-", objeto)
    
    elif opcion == "3":
        print()
        print("Te acercas a la puerta principal.")

        if llave == True and tarjeta == True and codigo_descubierto == True:
            codigo = input("Introduce el código: ")
            if codigo == "314":
                print()
                print("La puerta comienza a abrirse lentamente")
                print("Has escapado del laboratorio")
                print()
                print("¡¡FELICIDADES!!")
                juego_activo = False
            else:
                print("Código incorrecto.")
        else:
            print("La puerta sigue bloqueada")
            print("Parece que todavía necesitas explorar")
    
    elif opcion == "4":
        print()
        print("Has abandonado la misión")
        juego_activo = False
    else:
        print()
        print("Opcion inválida.")
    
print()
print("="* 50)
print("Gracias por jugar Mision Python")
print("="* 50)

