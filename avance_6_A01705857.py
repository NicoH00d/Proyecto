import time
pi=3.141592

def suma():
    n1=float(input("ingrese el primer número\n"))
    n2=float(input("ingrese el segundo número\n"))
    return (n1+n2)
def resta():
    n1=float(input("ingrese el primer número\n"))
    n2=float(input("ingrese el segundo número\n"))
    return (n1-n2)
def multi():
    n1=float(input("ingrese el primer número\n"))
    n2=float(input("ingrese el segundo número\n"))
    return (n1*n2)
def division():
    n1=float(input("ingrese el primer número\n"))
    n2=float(input("ingrese el segundo número\n"))
    return (n1/n2)
def potencia():
    n1=float(input("ingrese el numero\n"))
    n2=float(input("ingrese la potencia\n"))
    return(n1**n2)
#----------------esto es para hacer la lista----------------------------#

def promedio(n):
    sum=0
    for x in n:
        sum=sum+x
        prom=sum/len(n)
    return prom
#-----------------------------------------------------------------------#


def valeria ():
    print("Hola\n ---C A L C U L A D O R A    G E O M É T R I C A    A R I T M É T I C A---\n¿Qué desea realizar hoy?")
    problema=input("1 para problemas geometricos, 2 para problemas aritmeticos, 3 para obtener un promedio\n")
    while problema != "1" and problema != "2" and problema !="3":
        print("Ese es un dato no válido, por favor vuelva a intentarlo")
        problema=(input())


    if problema =="1":
        print("Problemas geométricos")
        selec=input("Escoga el numero correspondiente de lo que desee realizar\n---ÁREAS---\n1. ÁREA DE UN CUADRILÁTERO\n2. ÁREA DE UN TRIANGULO\n3. ÁREA DE UN CÍRCULO\n4. ÁREA DE UN ROMBO\n---VOLÚMENES---\n5. VOLUMEN CUBO\n6. VOLUMEN PIRÁMIDE CUADRADA\n7. VOLUMEN PIRAMIDE TRIANGULAR\n8. VOLUMEN CONO\n9. VOLUMEN ESFERA\n10. VOLUMEN CILINDRO\n11.-SALIR-\n")

        while selec != "11":
            while selec != "1" and selec != "2" and selec != "3" and selec != "4" and selec != "5" and selec != "6" and selec != "7" and selec != "8" and selec != "9" and selec != "10" and selec!="11":
                selec=input("Ese dato no es valido, vuelva a intentarlo.\n")
        
            if selec =="1":
                print("Área cuadrilatero")
                c1=float(input("ingrese el lado 1\n"))
                c2=float(input("ingrese el lado 2\n"))
                areac=c1*c2
                print("El área de su cuadrado es de",areac," unidades cuadradas")

            if selec =="2":
                print("Área triángulo")
                t1=float(input("ingrese el lado 1\n"))
                t2=float(input("ingrese el lado 2\n"))
                areat=(t1*t2)/2
                print("El área de su triángulo es de",areat," unidades cuadradas")

            if selec =="3":
                print("Área círculo")
                rad=float(input("ingrese el radio \n"))
                areaci=pi*rad**2
                print("El área de su círculo es de",areaci," unidades cuadradas")

            if selec =="4":
                print("Área rombo")
                dia1=float(input("ingrese la diagonal mayor \n"))
                dia2=float(input("ingrese la diagonal menor \n"))
                arearo=(dia1*dia2)/2
                print("El área de su rombo es de",arearo," unidades cuadradas")

            if selec=="5":
                print("Volumen cubo")
                lad1=float(input("ingrese el lado 1\n"))
                lad2=float(input("ingrese el lado 2\n"))
                lad3=float(input("ingrese el lado 3\n"))
                volumenc=lad1*lad2*lad3
                print("El volumen de su cubo es de",volumenc,"unidades cúbicas")

            if selec=="6":
                print("Volumen piramide cuadrada")
                ladd1=float(input("ingrese el lado 1\n"))
                ladd2=float(input("ingrese el lado 2\n"))
                ladd3=float(input("ingrese el lado 3\n"))
                volumencc=(ladd1*ladd2*ladd3)/3
                print("El volumen de su piramide es de",volumencc,"unidades cúbicas")

            if selec=="7":
                print("Volumen piramide triángular")
                laddd1=float(input("ingrese el lado 1\n"))
                laddd2=float(input("ingrese el lado 2\n"))
                laddd3=float(input("ingrese el lado 3\n"))
                volumenccc=(laddd1*laddd2*laddd3)/6
                print("El volumen de su piramide es de",volumenccc,"unidades cúbicas")

            if selec=="8":
                print("Volumen cono")
                cono1=float(input("ingrese el radio\n"))
                cono2=float(input("ingrese la altura\n"))
                volumencono=(pi*cono1**2*cono2)/3
                print("El volumen de su piramide es de",volumencono,"unidades cúbicas")

            if selec=="9":
                print("Volumen esfera")
                radio=float(input("ingrese el radio\n"))
                volesfera=(pi*radio**3)*4/3
                print("El volumen de su esfera es de",volesfera,"unidades cúbicas")

            if selec=="10":
                print("Volumen cilindro")
                radio99=float(input("ingrese el radio\n"))
                omg2=float(input("ingrese la altura\n"))
                volcilindro=(pi*radio99**2)*omg2
                print("El volumen de su cilindro es de",volcilindro,"unidades cúbicas")
            time.sleep(1)
            selec=input("\n-------------------------------------------------------------\nEscoga el numero correspondiente de lo que desee realizar\n---ÁREAS---\n1. ÁREA DE UN CUADRILÁTERO\n2. ÁREA DE UN TRIANGULO\n3. ÁREA DE UN CÍRCULO\n4. ÁREA DE UN ROMBO\n---VOLÚMENES---\n5. VOLUMEN CUBO\n6. VOLUMEN PIRÁMIDE CUADRADA\n7. VOLUMEN PIRAMIDE TRIANGULAR\n8. VOLUMEN CONO\n9. VOLUMEN ESFERA\n10. VOLUMEN CILINDRO\n11.-SALIR-\n")
        valeria()
        
    elif problema =="2":
        print("Menú aritmetico")
        arit=input("Escoga el numero correspondiente de lo que desee realizar\n1. SUMA\n2. RESTA\n3. Multiplicacion\n4. División.\n5. Elevar a potencia\n6. Salir\n")

        while arit != "6":
            while arit != "1" and arit != "2" and arit != "3" and arit != "4" and arit != "5":
                arit=input("Ese dato no es valido, vuelva a intentarlo\n")
                
            if arit =="1":
                print("la suma es:",suma())
                
            if arit == "2":
                print("la resta es:",resta())
        
            if arit =="3":
                print("la multiplicación es:",multi())

            if arit=="4":
                print("la división es:",division())
            if arit =="5":
                print("El numero ala potencia elegida es:",potencia())


                
            time.sleep(1)
            arit=input("\n------------------------------------------------------\nEscoga el numero correspondiente de lo que desee realizar\n1. SUMA\n2. RESTA\n3. Multiplicacion\n4. División.\n5. Elevar a potencia\n6. Salir\n")

        valeria()

    elif problema=="3":
                
        lista=[]
        cant=int(input("introduce la cantidad de datos: "))
        cont=0
        while cont < cant:
            num=float(input("introduce el dato: "))
            lista.append(num)
            cont=cont+1

        print("El promedio es de:", promedio(lista))




valeria()
    



