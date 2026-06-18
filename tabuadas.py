n = 0

while n <= 100:
    print("===============")
    print(f"Tabuada do {n}")
    
    for contador in range(11):
        resultado = n * contador
        print(f"{n} x {contador} = {resultado}")
    
    print("===============")
    n += 1

print("Desenvolvido por: Kobe")