from figuras.rectangulo import Rectangulo
from figuras.sector import Sector
from figuras.circulo import Circulo
from figuras.trapezoide import Trapezoide
from figuras.pentagono import Pentagono
from figuras.cuadrilatero import cuadrilatero
from figuras.cuboAlgt import Cubo
from figuras.octagono import octagono

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
    print("18.-Area of a Cube formula")
    print("16.-Salir")
    opcion = int(input("Que figura elige?"))
     
    if opcion== 1:
        from figuras.AreaRombo import Rombo
        dmayor = int(input("Ingresa dmayor del rombo: "))
        dmenor = int(input("Ingresa dmenor del rombo: "))
        Rombo = AreaRombo(dmayor,dmenor)
        Rombo.imprimirInfo()
        Rombo.area()
        break
     

    elif opcion == 4:
        lado = int(input("Ingrese medida del lado del Pentagono: "))
        Penta = Pentagono(lado)
        Penta.ImprimirInfo()
        lado2 = (input("Teclee enter para que regresar al menu: "))

    elif opcion == 5:
        Lado1= int(input("ingrese la medida del primer lado: "))
        Lado2= int(input("ingrese la medida del segundo lado: "))
        cuadrilatero=(Lado1 * Lado2)
        Sen= int(input("¿Cual es la medida del angulo?"))
        RESULTADO= (cuadrilatero * Sen)
        print(f'EL AREA DEL CUADRILATERO ES:{RESULTADO}')

    elif opcion == 7:
        perimetro= int(input("Ingrese la medida deseada: "))
        apotema= float(input("Ingrese la medida: "))
        area= (perimetro * apotema)/2
        print(f'El area del octagono es: {area}')
        

    elif opcion == 9:
        pi= int(input("Ingresa pi: "))
        radio = int(input("Ingresa el radio: "))
        uncirculo = Circulo(pi,radio)   
        print(f'El area es  {uncirculo.area()}')

    elif opcion == 8:
        from figuras.poligono import Poligono
        Lado = int(input("Ingresa el numero de lados de la figura:\n"))
        aLongitud = int(input("Ingresa la longitud de sus lados:\n"))
        Poligono = Poligono(Longitd,Lado)
        Poligono.area()
        Poligono.ImprimirInfo()

    elif opcion ==9:
        pi = float(input("Ingresa pi: "))
        radio = float(input("Ingresa radio: "))
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
    elif opcion == 11:
        diagonalE=int(input("Ingresa el numero de la diagonal menor:\n"))
        diagonalF=int(input("Ingrear el numero de la diagonal mayor:\n"))
        papalote= Kite(diagonalE,diagonalF)
        papalote.ImpInfo()
        papalote.area()

    elif opcion ==14:
        from figuras.paralelogramo import Paralelogramo
        base = int(input("Ingresa la base del Paralelogramo:\n"))
        altura = int(input("Ingresa la altura del Paralelogramo:\n"))
        Paralelo = Paralelogramo(base,altura)
        Paralelo.area()
        Paralelo.ImprimirInfo()
    elif opcion==2:
        pass

    elif opcion==16:
        break

    elif opcion==6:
        pi = float(input("Ingresa el Pi: "))
        radioCaudrado = int(input("Ingresa el Radio al Cuadrado:"))
        numGrados = int(input("Ingresa el numero de grados:"))
        misector = Sector(pi,radioCaudrado,numGrados)
        misector.area()
        misector.ImpInf()


    elif opcion==18:
        Lado1 = int(input("Ingrese la medida del lado 1"))
        Lado2 = int(input("Ingrese la medida del lado 2"))
        SumLd = int(input("Ingrese la suma de los lados del cubo"))
        Cubo = Cubo(base,altura,SumLd)
        Cubo.area()
        Cubo.ImprimirInfo()
        




    elif opcion==13
         pi = int(input("Ingrese pi "))
         a = int(input("Ingrese medida de a "))
         b = int(input("Ingrese medida de b "))
         area = self.__pi * self.__b * self.__b
         ellipse.area()
         area.ImpInf()
