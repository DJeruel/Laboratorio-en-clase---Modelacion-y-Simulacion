import os
import itertools
while True:
    e = 2.718
    print("¿Que Modelos de probabilidad desea realizar?")
    print("	1.	Poisson	")
    print("	2.	Binomial	")
    print("	3.	Normal	")
    print("	4.	salir	")
    opcion=input()
    if opcion== '1':
        print("== POISSON ==")
        µ =int(input("Ingrese (µ) miu (promedio): "))
        k =int(input("Ingrese k (numero de ocurrencia de interes): "))

        print("e = ", e)
    #Factorial
        factorial = 1
        for n in range(1, (k + 1)):
            factorial = factorial * n
        probabilidad = (  (µ**k)*(e**(-µ))  )  /  factorial
        probabilidad2 = probabilidad * 100
        print("\nLa probabilidad es :", probabilidad2)

    elif opcion== '2':
        print("== BINOMIAL ==")
        n =int(input("Ingrese (n) número de ensayos/experimentos: "))
        k =int(input("Ingrese (k) número de éxitos: "))
        p =float(input("Ingrese (p) probabilidad de éxitos: "))
        q =float(input("Ingrese (q) probabilidad de fracasos: "))

        # Factorial
        factorial = 1
        for n in range(1, (k + 1)):
            factorial = factorial * n

        probabilidad = ((n/k) * ((p ** k)*(q ** (n-k))))
        probabilidad2 = probabilidad * 100
        print("\nLa probabilidad es :", probabilidad2)

    elif opcion== '3':
        print("== NORMAL ==")
        x =float(input("Ingrese (x) : "))
        σ =int(input("Ingrese (σ) : "))
        µ =int(input("Ingrese (µ) : "))

        probabilidad = ((x - µ) / σ )
        print("\nLa probabilidad es :", probabilidad)

    elif opcion == '4':
        break
    input()