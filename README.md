# Sumador - Restador de 4 Bits en Python

## Descripción del proyecto

Este proyecto implementa un **sumador y restador de 4 bits** utilizando conceptos básicos de lógica digital, simulados mediante programación en Python.

El sistema permite:

- Realizar la suma de dos números binarios de 4 bits.
- Realizar la resta de dos números binarios de 4 bits.
- Manejar el acarreo de salida (carry out).
- Comprender el funcionamiento interno de un sumador-restador digital.

El objetivo principal del ejercicio es aplicar conceptos de:

- Representación binaria
- Aritmética binaria
- Complemento a dos
- Diseño lógico modular

---

## Objetivo del ejercicio

Diseñar un sistema que simule el comportamiento de un circuito digital capaz de:

- Sumar dos números binarios cuando el modo es `0`.
- Restar dos números binarios cuando el modo es `1`.

Esto se logra utilizando un único circuito lógico (sumador) y modificando la entrada para realizar la resta mediante complemento a dos.

---

## Conceptos utilizados

### Bit
Unidad mínima de información digital que puede tomar el valor de:

- `0`
- `1`

### MSB y LSB

- **MSB (Most Significant Bit)**: Bit más significativo, ubicado a la izquierda.
- **LSB (Least Significant Bit)**: Bit menos significativo, ubicado a la derecha.

Ejemplo:
[1, 0, 1, 1]
↑ ↑
MSB LSB


El LSB se procesa primero porque es donde inicia la suma binaria.

---

### Complemento a dos

La resta binaria se realiza mediante:

1. Invertir los bits del número a restar.
2. Sumar 1 al resultado.
3. Realizar una suma normal.

Esto permite que la resta se implemente usando el mismo circuito sumador.

---

## Diseño del sistema

El diseño sigue la estructura de un **sumador completo (Full Adder)** repetido 4 veces.

Cada etapa recibe:

- Bit de A
- Bit de B
- Acarreo de entrada

Y produce:

- Bit resultado
- Acarreo de salida

### Modo de operación

| Modo | Operación |
|------|-----------|
| 0 | Suma |
| 1 | Resta |

Cuando el modo es 1:

- Los bits de B se invierten.
- El acarreo inicial se establece en 1.

---

A = 5  -> 0101,
B = 3  -> 0011

---

Suma: 

0101 + 0011 = 1000
Resultado: [1,0,0,0]
Carry: 0

---

Resta:

0101 - 0011 = 0010
Resultado: [0,0,1,0]
Carry: 1

