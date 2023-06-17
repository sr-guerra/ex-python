# altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, ...

multiplicando = int(input("Tabuada do: "))
multiplicador = 0

while multiplicador <= 10:
    print(f"{multiplicando} x {multiplicador} = {multiplicando * multiplicador}")
    multiplicador += 1