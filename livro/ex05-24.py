# Modifique o programa anterior (5.23) de forma a ler um número n.
# imprima os n primeiros números primos.

fim= int(input("Digite um número: "))

if fim < 2:
    print(f"Não há números primos até {fim}.")

elif fim == 2:
    print("2.")

else:
    impar = 3
    numero = 3

    print("2 ")
    
    while numero <= fim:
        if numero % 2 != 0:
            while impar <= numero:
                if impar == numero:
                    print(f"{numero}")
                    break
            
                elif numero % impar == 0:
                    break

                impar+=2

        impar = 3
        numero+=1
        