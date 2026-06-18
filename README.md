# 📘 Projeto: Tabuada com Loop `while` em Python

Este projeto demonstra como utilizar **loops `while`** em Python para gerar a tabuada de números de **0 a 100**.

## 🚀 Objetivo

Praticar o uso de estruturas de repetição (`while`) criando um programa simples que:

- Percorre números de 0 a 100
- Para cada número, imprime sua tabuada de 1 a 10
- Utiliza **dois loops `while`** (um externo e um interno)

## 🧠 Conceitos Utilizados

- Loop `while`
- Variáveis e incrementos
- Estruturas aninhadas (loop dentro de loop)
- Impressão formatada (`f-string`)

## 📂 Estrutura do Código

```python
# Loop externo: controla o número base (0 a 100)
numero = 0

while numero <= 100:
    print(f"\n📊 Tabuada do {numero}")

    # Loop interno: multiplica o número de 1 a 10
    multiplicador = 1

    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1

    numero += 1
```
