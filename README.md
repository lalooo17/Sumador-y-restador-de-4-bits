# Sumador-Restador de 4 Bits en Python

Este repositorio contiene una implementación de un **sumador–restador de 4 bits** utilizando únicamente **puertas lógicas básicas**: AND, OR y NOT. El objetivo es mostrar cómo operaciones complejas, como suma y resta, se pueden construir a partir de bloques simples de lógica digital.

---

## 1. Descripción del ejercicio

Se nos pidió:

- Diseñar un sumador-restador de 4 bits.
- Usar solo las puertas lógicas AND, OR y NOT.
- Implementar la funcionalidad de suma y resta controlada por un bit `M`:
  - `M = 0` → suma
  - `M = 1` → resta

El ejercicio busca que entendamos la **propagación de carry**, el concepto de **complemento a dos** para la resta y cómo las operaciones XOR se pueden construir usando solo AND, OR y NOT.

---

## 2. Diseño del sumador-restador

### 2.1 Representación de los bits

Se usan listas de 4 bits de **menos significativo a más significativo**:

```text
A = [A0, A1, A2, A3]
B = [B0, B1, B2, B3]
A0 / B0 → bit menos significativo (LSB)
A3 / B3 → bit más significativo (MSB)
```


