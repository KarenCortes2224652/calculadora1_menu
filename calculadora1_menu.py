# Calculadora con menú.

from math import log
print("-------------------------")
print("---CALCULADORA - MENÚ ---")
print("-------------------------")

#Input
bandera = False
x = float(input("Dame el valor del número x: "))
y = float(input("Dame el valor del número y: "))

print("\n Dame la opción que deseas realizar: \n")
# Se despliega el menú para seleccionar la opción que deseas realizar
print("1.Sumar(El primero más el segundo)")
print("2.Restar(El primero menos el segundo)")
print("3.Multiplicar(El primero por el segundo)")
print("4.Dividir(El primero entre el segundo)")
print("5.Potencia (El primero a la potencia de el segundo)")
print("6.Logaritmo (El logaritmo de el primero)")

opcion = int(input("\nDame la opción: "))

#Processing
if(opcion==1):
    z= x + y
    print(x,"+",y)
elif (opcion==2):
    z = x - y
    print(x,"-",y)
elif(opcion==3):
    z = x * y
    print(x,"X",y)
elif (opcion==4 and y!=0):
    z = x / y
    print(x,"/",y)
elif(opcion==4 and y==0):
    print("El denominador es igial a cero y")
    print("NO se puede realizar la division.")
    bandera= True
elif (opcion==5):
    z = pow(x,y)
    print(x,"^",y)
elif(opcion==6 and x>0):
    z=log(x)
    print("Logaritmo de",x)
elif(opcion==6 and x<=0):
    print("El valor de x es <= a cero y")
    print("NO se puede calcular el logaritmo. ")
else:
    print("opción no valida ")

    # Se escribe el resultado con otra condicion 
if(opcion<7 and bandera==False):
        print("Resultado =",z)

#Fin


 