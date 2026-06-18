# 📘 Projeto: Tabuada de 0 a 100 com Python

Este projeto em Python gera automaticamente a **tabuada de 0 até 100**, utilizando estruturas de repetição (`while`).

---

## 🚀 Objetivo

Praticar conceitos fundamentais de programação, incluindo:

- Estruturas de repetição (`while`)
- Loops aninhados
- Controle de fluxo
- Saída formatada no terminal

---

## 🧠 Como funciona

O programa utiliza:

- Um `while` externo para percorrer os números de **0 até 100**
- Um `while` interno para calcular a tabuada de **0 até 10** de cada número

---

## 💻 Código

```python
n = 0

while n <= 100:
    print("===============")
    print(f"Tabuada do {n}")

    contador = 0
    while contador <= 10:
        print(f"{n} x {contador} = {n * contador}")
        contador += 1

    print("===============")
    n += 1

print("Desenvolvido por: Kobe")
```

---

## ▶️ Como executar

1. Instale o Python (caso ainda não tenha)
2. Salve o arquivo como `tabuada.py`
3. Execute no terminal:

```bash
python tabuada.py
```

---

## 📌 Exemplo de saída

```
===============
Tabuada do 2
2 x 0 = 0
2 x 1 = 2
2 x 2 = 4
...
2 x 10 = 20
===============
```

---

## 📚 Requisitos

- Python 3.x

---

## 📄 Licença

Este projeto é livre para fins educacionais.
