# ==========================================
# Consultorio de atencion odontologica
# ==========================================


# Lista para guardar los clientes
clientes = []


# ==========================================
# Funcionn para calcular los valores de la cita
# ==========================================

def calcular_valor(tipo_cliente, tipo_atencion, cantidad):

    # Valores de la cita
    if tipo_cliente == "Particular":
        valor_cita = 80000

    elif tipo_cliente == "EPS":
        valor_cita = 5000

    else:
        valor_cita = 30000


    # Valores de la atencion
    if tipo_cliente == "Particular":

        if tipo_atencion == "Limpieza":
            valor_atencion = 60000

        elif tipo_atencion == "Calzas":
            valor_atencion = 80000

        elif tipo_atencion == "Extraccion":
            valor_atencion = 100000

        else:
            valor_atencion = 50000


    elif tipo_cliente == "EPS":

        if tipo_atencion == "Limpieza":
            valor_atencion = 0

        elif tipo_atencion == "Calzas":
            valor_atencion = 40000

        elif tipo_atencion == "Extraccion":
            valor_atencion = 40000

        else:
            valor_atencion = 0


    else:  # PREPAGADA

        if tipo_atencion == "Limpieza":
            valor_atencion = 0

        elif tipo_atencion == "Calzas":
            valor_atencion = 10000

        elif tipo_atencion == "Extraccion":
            valor_atencion = 10000

        else:
            valor_atencion = 0


    # Formula:
    # Valor de la cita + (valor de atencion * cantidad)

    total = valor_cita + (valor_atencion * cantidad)

    return valor_cita, valor_atencion, total

#consultorio odontologico
def main():

    while True:

        print("\n")
        print("====================================")
        print("     CONSULTORIO ODONTOLOGICO")
        print("====================================")

        # ----------------------------------
        # Datos del cliente
        # ----------------------------------

        cedula = input("Ingrese la cedula: ")

        nombre = input("Ingrese el nombre: ")

        telefono = input("Ingrese el telefono: ")


        # ----------------------------------
        # Tipo cliente dependiendo de su eps o particular
        # ----------------------------------

        print("\nTIPO DE CLIENTE")
        print("1. Particular")
        print("2. EPS")
        print("3. Prepagada")

        opcion = input("Seleccione una opcion: ")


        if opcion == "1":
            tipo_cliente = "Particular"

        elif opcion == "2":
            tipo_cliente = "EPS"

        elif opcion == "3":
            tipo_cliente = "Prepagada"

        else:
            print("Opcion incorrecta.")
            continue


        # ----------------------------------
        # Tipo de atencion requerida
        # ----------------------------------

        print("\nTIPO DE ATENCION")
        print("1. Limpieza")
        print("2. Calzas")
        print("3. Extraccion")
        print("4. Diagnostico")

        opcion = input("Seleccione una opcion: ")


        if opcion == "1":
            tipo_atencion = "Limpieza"

        elif opcion == "2":
            tipo_atencion = "Calzas"

        elif opcion == "3":
            tipo_atencion = "Extraccion"

        elif opcion == "4":
            tipo_atencion = "Diagnostico"

        else:
            print("Opcion incorrecta.")
            continue


        # ----------------------------------
        # cantidad de tipo atencion
        # ----------------------------------

        if tipo_atencion == "Limpieza" or tipo_atencion == "Diagnostico":

            cantidad = 1

            print("La cantidad es 1.")

        else:

            cantidad = int(input("Ingrese la cantidad: "))

            while cantidad <= 0:

                print("La cantidad debe ser mayor que cero.")

                cantidad = int(input("Ingrese la cantidad: "))


        # ----------------------------------
        # Prioridad de la atencion
        # ----------------------------------

        print("\nPRIORIDAD DE ATENCION")
        print("1. Normal")
        print("2. Urgente")

        opcion = input("Seleccione una opcion: ")


        if opcion == "1":
            prioridad = "Normal"

        elif opcion == "2":
            prioridad = "Urgente"

        else:
            print("Opcion incorrecta.")
            continue


        fecha = input("Ingrese la fecha de la cita: ")


        # ----------------------------------
        # Calculo el valor,atencion,tipo cliente,cantidad procedimeinto
        # ----------------------------------

        valor_cita, valor_atencion, total = calcular_valor(
            tipo_cliente,
            tipo_atencion,
            cantidad
        )


        # ----------------------------------
        # Guardo la informacion del clliente
        # ----------------------------------

        cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "telefono": telefono,
            "tipo_cliente": tipo_cliente,
            "tipo_atencion": tipo_atencion,
            "cantidad": cantidad,
            "prioridad": prioridad,
            "fecha": fecha,
            "valor_cita": valor_cita,
            "valor_atencion": valor_atencion,
            "total": total
        }


        clientes.append(cliente)


        # ----------------------------------
        # Mostrar todo o resumen del cliente
        # ----------------------------------

        print("\n====================================")
        print("       CITA REGISTRADA")
        print("====================================")

        print("Cliente:", nombre)
        print("Tipo de cliente:", tipo_cliente)
        print("Tipo de atencion:", tipo_atencion)
        print("Cantidad:", cantidad)
        print("Prioridad:", prioridad)
        print("Fecha:", fecha)

        print("------------------------------------")

        print("Valor de la cita: $", valor_cita)
        print("Valor de la atencion: $", valor_atencion)
        print("TOTAL A PAGAR: $", total)


        continuar = input("\nDesea ingresar otro cliente? (S/N): ")


        if continuar.upper() == "N":
            break


    # ==========================================
    # Calculos de los procedimientos
    # ==========================================

    print("\n\n")
    print("====================================")
    print("       RESUMEN DEL CONSULTORIO")
    print("====================================")


    # Total de clientes, en cuestion de registro

    total_clientes = len(clientes)

    print("Total de clientes:", total_clientes)


    # ----------------------------------
    # Ingreso total de cliente
    # ----------------------------------

    ingresos_totales = 0

    for cliente in clientes:

        ingresos_totales = ingresos_totales + cliente["total"]


    print("Ingresos totales: $", ingresos_totales)


    # ----------------------------------
    # Configuro el NUMERO DE EXTRACCIONES
    # ----------------------------------

    numero_extracciones = 0

    for cliente in clientes:

        if cliente["tipo_atencion"] == "Extraccion":

            numero_extracciones = numero_extracciones + 1


    print("Clientes para extraccion:", numero_extracciones)


    # ==========================================
    # Ordeno los clientes
    # ==========================================

    clientes.sort(
        key=lambda cliente: cliente["valor_atencion"],
        reverse=True
    )


    print("\n")
    print("====================================")
    print(" CLIENTES ORDENADOS")
    print(" POR VALOR DE ATENCION")
    print("====================================")


    for cliente in clientes:

        print(
            "Cedula:", cliente["cedula"],
            "| Nombre:", cliente["nombre"],
            "| Atencion:", cliente["tipo_atencion"],
            "| Valor: $", cliente["valor_atencion"]
        )


    # ==========================================
    # Busco cliente con la cedula
    # ==========================================

    print("\n")
    cedula_buscar = input("Ingrese la cedula que desea buscar: ")


    encontrado = False


    for cliente in clientes:

        if cliente["cedula"] == cedula_buscar:

            print("\n====================================")
            print("        CLIENTE ENCONTRADO")
            print("====================================")

            print("Cedula:", cliente["cedula"])
            print("Nombre:", cliente["nombre"])
            print("Telefono:", cliente["telefono"])
            print("Tipo de cliente:", cliente["tipo_cliente"])
            print("Tipo de atencion:", cliente["tipo_atencion"])
            print("Cantidad:", cliente["cantidad"])
            print("Prioridad:", cliente["prioridad"])
            print("Fecha:", cliente["fecha"])
            print("Valor de la cita: $", cliente["valor_cita"])
            print("Valor de la atencion: $", cliente["valor_atencion"])
            print("Total a pagar: $", cliente["total"])

            encontrado = True

            break


    if encontrado == False:

        print("\nNo se encontro un cliente con esa cedula.")


main()
