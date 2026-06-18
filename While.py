n = 0
contador = 0
while n != 101:
  print("===============")
  print(f"Tabuada do {n}")
  for contador in range(11):
    resultado = 0;
    resultado += n * contador;
    print(f"{n} x {contador} = {resultado}")
  n +=1;
  print("===============")