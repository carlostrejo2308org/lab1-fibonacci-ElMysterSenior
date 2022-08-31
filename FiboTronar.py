


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Selecciona el numero de accion a realizar: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0


while not salir:

    print("Menu de opciones!")
    print("1. Fibonacci recursivo")
    print("2. Fibonacci no recursivo")
    print("3. Salir")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("Fibonacci recursivo")


        def fibo(num):
            if (num == 0 or num == 1):                          #Error por numero 0 o 1
                return 1                                        #Solucion usada Condicional if
            else:
                return fibo(num - 1) + fibo(num - 2)
        while True:

            n = input("Numero a obtener fibonacci")
            try:
                entero=int(n)
            except ValueError:
                print("Numero ingresado no es entero, es decimal") #Error por numero no entero (Decimal)

            if(entero>=1):                                         #Solucion usada Try except
                    break

        for i in range(entero):
                print(fibo(i))



    elif opcion == 2:

        print("Fibonacci no recursivo")

        n = int(input("Numero a obtener fibonacci"))

        num1 = 0

        num2 = 1

        aux = 0

        if n <= 0:

            print("Numero invalido, es negativc")

        elif n == 1:

            print("Fibonacci sequence upto", n, ":")

            print(num1)

        else:

            print("Fibonacci:")

            while aux < n:
                print(num1)

                aux2 = num1 + num2

                num1 = num2

                num2 = aux2

                aux += 1


    elif opcion == 3:

        salir = True


    else:
        print("Introduce un numero con accion asignada")
