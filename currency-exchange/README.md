# Cambio de divisas

Te damos la bienvenida a Cambio de divisas en el track Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.
Si te atascas con el ejercicio, consulta `HINTS.md`, pero primero intenta resolverlo sin usarlos :)

## Introduction

## Números

En Python hay tres tipos diferentes de números integrados: `ints`, `floats` y `complex`. Sin embargo, en este ejercicio solo vas a trabajar con `ints` y `floats`.

### ints

Los `ints` son números enteros. Por ejemplo, `1234`, `-10`, `20201278`.

Los enteros en Python tienen [precisión arbitraria][arbitrary-precision]: la cantidad de dígitos solo está limitada por la memoria disponible del sistema anfitrión.

### floats

Los `floats` son números que contienen un punto decimal. Por ejemplo, `0.0`,`3.14`,`-9.01`.

Los números de punto flotante normalmente se implementan en Python usando un `double` en C (_15 decimales de precisión_), pero su representación varía según el sistema anfitrión y otros detalles de implementación. Esto puede generar algunas sorpresas cuando trabajas con números de punto flotante, pero es «suficientemente bueno» para la mayoría de las situaciones.

Puedes ver más detalles y discusiones en los siguientes recursos:

- [Documentación de los tipos numéricos de Python][numeric-type-docs]
- [El tutorial de Python][floating point math]
- [Documentación de `int()` integrado][`int()` built in]
- [Documentación de `float()` integrado][`float()` built in]
- [0.30000000000000004.com][0.30000000000000004.com]

## Aritmética

Python admite por completo la aritmética entre `ints` y `floats`. Convierte los números más estrechos para que coincidan con sus equivalentes menos estrechos cuando se usan con los operadores aritméticos binarios (`+`, `-`, `*`, `/`, `//` y `%`).

Python considera que los `ints` son más estrechos que los `floats`. Por eso, usar un número de punto flotante en una expresión garantiza que el resultado también sea un número de punto flotante. Sin embargo, al hacer una división, el resultado siempre es un número de punto flotante, incluso si solo usas enteros.

```python
# The int is widened to a float here, and a float type is returned.
>>> 3 + 4.0
7.0
>>> 3 * 4.0
12.0
>>> 3 - 2.0
1.0
# Division always returns a float.
>>> 6 / 2
3.0
>>> 7 / 4
1.75
# Calculating remainders.
>>> 7 % 4
3
>>> 2 % 4
2
>>> 12.75 % 3
0.75
```

Si necesitas un resultado entero, puedes usar `//` para truncar el resultado.

```python
>>> 6 // 2
3
>>> 7 // 4
1
```

Para convertir un número de punto flotante en un entero, puedes usar `int()`. Para convertir un entero en un número de punto flotante, puedes usar `float()`.

```python
>>> int(6 / 2)
3
>>> float(1 + 2)
3.0
```

[0.30000000000000004.com]: https://0.30000000000000004.com/
[`float()` built in]: https://docs.python.org/3/library/functions.html#float
[`int()` built in]: https://docs.python.org/3/library/functions.html#int
[arbitrary-precision]: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#:~:text=In%20computer%20science%2C%20arbitrary%2Dprecision,memory%20of%20the%20host%20system.
[floating point math]: https://docs.python.org/3.9/tutorial/floatingpoint.html
[numeric-type-docs]: https://docs.python.org/3/library/stdtypes.html#typesnumeric

## Instructions

Tu amigo Chandler planea visitar países exóticos de todo el mundo. Lamentablemente, a Chandler no se le dan bien las matemáticas. Está bastante preocupado por que lo estafen en las casas de cambio durante su viaje, y quiere que le hagas una calculadora de divisas. Estas son sus especificaciones para la app:

## 1. Estima el valor después del cambio

Crea la función `exchange_money()`, que recibe 2 parámetros:

1. `budget`: la cantidad de dinero que planeas cambiar.
2. `exchange_rate`: la cantidad de moneda nacional equivalente a una unidad de moneda extranjera.

Esta función debe devolver el valor de la moneda cambiada.

**Nota:** Si tu moneda es USD y quieres cambiar USD por EUR con una tasa de cambio de `1.20`, entonces `1.20 USD == 1 EUR`.

```python
>>> exchange_money(127.5, 1.2)
106.25
```

## 2. Calcula cuánto dinero queda después de un cambio

Crea la función `get_change()`, que recibe 2 parámetros:

1. `budget`: la cantidad de dinero antes del cambio.
2. `exchanging_value`: la cantidad de dinero que se *toma* del presupuesto para cambiarla.

Esta función debe devolver la cantidad de dinero que *queda* del presupuesto.

```python
>>> get_change(127.5, 120)
7.5
```

## 3. Calcula el valor de los billetes

Crea la función `get_value_of_bills()`, que recibe 2 parámetros:

1. `denomination`: el valor de un solo billete.
2. `number_of_bills`: el número total de billetes.

Esta casa de cambio solo trabaja con efectivo en ciertos incrementos.
El total que recibes debe ser divisible entre el valor de un «billete» o unidad, lo que puede dejar una fracción o un residuo.
Tu función debe devolver solo el valor total de los billetes (_sin incluir las fracciones_) que la casa de cambio te daría.
Lamentablemente, la casa de cambio se queda con el residuo o el cambio como un bono extra.

```python
>>> get_value_of_bills(5, 128)
640
```

## 4. Calcula el número de billetes

Crea la función `get_number_of_bills()`, que recibe `amount` y `denomination`.

Esta función debe devolver el _número de billetes_ que puedes recibir dentro del _amount_ dado.
En otras palabras: ¿cuántos _billetes completos_ caben en la cantidad inicial?
Recuerda que solo puedes recibir _billetes completos_, no fracciones de billetes, así que asegúrate de dividir como corresponde.
En efecto, estás redondeando _hacia abajo_ al billete o denominación completa más cercana.

```python
>>> get_number_of_bills(127.5, 5)
25
```

## 5. Calcula lo que sobra después de cambiar a billetes

Crea la función `get_leftover_of_bills()`, que recibe `amount` y `denomination`.

Esta función debe devolver la _cantidad sobrante_ que no se puede devolver de tu _amount_ inicial con la denominación de billetes dada.
Es muy importante saber exactamente cuánto se queda la casa de cambio.

```python
>>> get_leftover_of_bills(127.5, 20)
7.5
```

## 6. Calcula el valor después del cambio

Crea la función `exchangeable_value()`, que recibe `budget`, `exchange_rate`, `spread` y `denomination`.

El parámetro `spread` es el *porcentaje que se toma* como comisión de cambio, escrito como un número entero.
Hay que convertirlo a decimal dividiéndolo entre 100.
Si `1.00 EUR == 1.20 USD` y el *spread* es `10`, la tasa de cambio real será: `1.00 EUR == 1.32 USD`, porque el 10% de 1.20 es 0.12, y esta comisión adicional se suma al cambio.

Esta función debe devolver el valor máximo de la nueva moneda después de calcular la *tasa de cambio* más el *spread*.
Recuerda que la *denominación* de la moneda es un número entero y no se puede subdividir.

**Nota:** el valor devuelto debe ser de tipo `int`.

```python
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
>>> exchangeable_value(127.25, 1.20, 10, 5)
95
```

## Source

### Created by

- @Ticktakto
- @Yabby1997
- @limm-jk
- @OMEGA-Y
- @wnstj2007
- @J08K

### Contributed to by

- @BethanyG
- @kytrinyx
- @pranasziaukas