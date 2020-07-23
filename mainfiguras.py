from figuras.rectangulo import Rectangulo
from figuras.circulo import Circulo
from figuras.trapezoide import Trapezoide

while True:
    print("1.-Area of a rhombus formula")
    print("2.-Area of a hexagon formula")
    print("3.-Area of a quadrilateral formula")
    print("4.-Pentagon area formula")
    print("5.-Area of a quadrilateral formula lesly")
    print("6.-Sector area formula")
    print("7.-Area of an octagon formula")
    print("8.-Regular polygon area formula")
    print("9.-Circle area formula")
    print("10.-Rectangle area formula")
    print("11.-Area of a kite formula")
    print("12.-Area of an annulus formula")
    print("13.-Ellipse area formula")
    print("14.-Area of a parallelogram formula")
    print("15.-Square area formula")
    print("16.-Triangle area formula")
    print("17.-Trapezoid area formula")
    print("16.-Salir")
    opcion = int(input("Que figura elige?"))
    if opcion==1:
        pass

    elif opcion == 9:
        pi= int(input("Ingresa pi: "))
        radio = int(input("Ingresa el radio: "))
        uncirculo = Circulo(pi,radio)   
        print(f'El area es  {uncirculo.area()}')



    elif opcion == 10:
        base = int(input("\nIngresa la base: "))
        altura = int(input("Ingrese la altura: "))
        res = Rectangulo(base, altura)
        while True:
            opcionRectangulo = input("Que desea hacer: \n1- Sacar el area\n2.- Ver informacion\n3.- Regresar al menu principal\nIngresa una opcion: ")
            if opcionRectangulo == "1":
                print(f"\n>>>El area es: {res.area()}\n")
            elif opcionRectangulo == "2":
                print(res.imprimirInfo())
            elif opcionRectangulo == "3":
                print("Regresando al menu principal")
                break

    elif opcion ==14:
        from figuras.paralelogramo import Paralelogramo
        base = int(input("Ingresa la base del Paralelogramo:\n"))
        altura = int(input("Ingresa la altura del Paralelogramo:\n"))
        Paralelo = Paralelogramo(base,altura)
        Paralelo.area()
        Paralelo.ImprimirInfo()

    elif opcion==15:
        from figuras.cuadrado import Cuadrado
        lado = int(input("Ingrese lado: "))
        c = Cuadrado(lado)
        print('El area es:')
        break

    elif opcion == 17:
        Bmayor = int(input("Ingrese medida de la Base Mayor: "))
        Bmenor = int(input("Ingrese medida de la Base menor: "))
        result = Trapezoide(Bmayor,Bmenor)
        result.imprimirInfo()
        result.area()


    elif opcion==2:
        pass



    elif opcion==16:
        from figuras.triangulo import Triangulo
        base = int(input("Ingresa base del triangulo: "))
        altura = int(input("Ingresa altura del triangulo: "))
        T = Triangulo(base,altura)
        T.imprimirInfo()
        T.area() 
        break

    elif opcion==6:
        pin = int(input("Ingresa el Pin: "))
        radioCaudrado = int(input("Ingresa el Radio al Cuadrado:"))
        numGrados = int(input("Ingresa el numero de grados:"))
        resultado = sector(pin,radioCaudrado,numGrados)
        sector.area()
        sector.ImpInf()

