# Mitigación de la fusión del núcleo

Te damos la bienvenida a Mitigación de la fusión del núcleo en el track Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.
Si te atascas con el ejercicio, consulta `HINTS.md`, pero primero intenta resolverlo sin usarlos :)

## Introduction

En Python, las sentencias [`if`][if statement], `elif` (_una contracción de «else and if»_) y `else` se usan para [controlar el flujo][control flow tools] de ejecución y tomar decisiones en un programa.
A diferencia de muchos otros lenguajes de programación, las versiones 3.9 y anteriores de Python no ofrecen una sentencia formal de tipo case-switch; en su lugar, usan varios `elif` para cumplir una función similar.

Python 3.10 introduce una variante de la sentencia case-switch llamada `structural pattern matching`, que se verá por separado en otro concepto.

Las sentencias condicionales usan expresiones que deben resolverse en `True` o `False`, ya sea devolviendo directamente un tipo `bool` o evaluándose como [«truthy» o «falsy»][truth value testing].

```python
x = 10
y = 5

# The comparison '>' returns the bool 'True',
# so the statement is printed.
if x > y:
    print("x is greater than y")
...
>>> x is greater than y
```

Cuando se combina con `if`, un bloque de código `else` opcional se ejecuta cuando la condición original del `if` se evalúa como `False`:

```python
x = 5
y = 10

# The comparison '>' here returns the bool 'False',
# so the 'else' block is executed instead of the 'if' block.
if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")
...
>>> y is greater than x
```

`elif` permite hacer múltiples evaluaciones o ramificaciones.

```python
x = 5
y = 10
z = 20

# The 'elif' statement allows for the checking of more conditions.
if x > y:
    print("x is greater than y and z")
elif y > z:
    print("y is greater than x and z")
else:
    print("z is greater than x and y")
...
>>> z is greater than x and y
```

Las [operaciones booleanas][boolean operations] y las [comparaciones][comparisons] se pueden combinar con los condicionales para hacer pruebas más complejas:

```python
>>> def classic_fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            say = 'FizzBuzz!'
        elif number % 5 == 0:
            say = 'Buzz!'
        elif number % 3 == 0:
            say = 'Fizz!'
        else:
            say = str(number)
        
        return say

>>> classic_fizzbuzz(15)
'FizzBuzz!'

>>> classic_fizzbuzz(13)
'13'
```

[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

## Instructions

En este ejercicio, vamos a desarrollar un sistema de control sencillo para un reactor nuclear.

Para que un reactor produzca potencia, debe encontrarse en un estado de _criticidad_.
Si el reactor está en un estado por debajo de la criticidad, puede dañarse.
Si el estado del reactor supera la criticidad, puede sobrecargarse y provocar una fusión del núcleo.
Queremos reducir las probabilidades de una fusión del núcleo y gestionar correctamente el estado del reactor.

Las siguientes tres tareas están relacionadas con escribir código para mantener el estado ideal del reactor.

## 1. Verifica la criticidad

Lo primero que debe hacer un sistema de control es comprobar si el reactor está _equilibrado en criticidad_.
Se dice que un reactor está equilibrado en criticidad si cumple las siguientes condiciones:

- La temperatura es menor que 800 K.
- La cantidad de neutrones emitidos por segundo es mayor que 500.
- El producto de la temperatura y los neutrones emitidos por segundo es menor que 500000.

Implementa la función `is_criticality_balanced()` que recibe `temperature`, medida en kelvin, y `neutrons_emitted` como parámetros, y devuelve `True` si se cumplen las condiciones de criticidad, y `False` si no.

```python
>>> is_criticality_balanced(750, 600)
True
```

## 2. Determina el rango de potencia de salida

Una vez que el reactor ha empezado a producir potencia, es necesario determinar su eficiencia.
La eficiencia se puede agrupar en 4 rangos:

1. `green` -> eficiencia del 80% o más,
2. `orange` -> eficiencia menor que el 80% pero de al menos el 60%,
3. `red` -> eficiencia por debajo del 60%, pero aún del 30% o más,
4. `black` -> eficiencia menor que el 30%.

El valor porcentual se puede calcular como `(generated_power/theoretical_max_power)*100`, donde `generated_power` = `voltage` * `current`.
Ten en cuenta que el valor porcentual normalmente no es un número entero, así que asegúrate de considerar el uso adecuado de las comparaciones `<` y `<=`.

Implementa la función `reactor_efficiency(<voltage>, <current>, <theoretical_max_power>)`, con tres parámetros: `voltage`, `current` y `theoretical_max_power`.
Esta función debe devolver el rango de eficiencia del reactor: 'green', 'orange', 'red' o 'black'.

```python
>>> reactor_efficiency(200,50,15000)
'orange'
```

## 3. Mecanismo a prueba de fallos

Tu tarea final consiste en crear un mecanismo a prueba de fallos para evitar la sobrecarga y la fusión del núcleo.
Este mecanismo determinará si el reactor está por debajo, en o por encima del umbral ideal de criticidad.
Luego, la criticidad se puede aumentar, disminuir o detener insertando (o retirando) barras de control en el reactor.

Implementa la función `fail_safe()`, que recibe 3 parámetros: `temperature`, medida en kelvin, `neutrons_produced_per_second` y `threshold`, y devuelve un código de estado para el reactor.

- Si `temperature * neutrons_produced_per_second` < 90% de `threshold`, devuelve un código de estado 'LOW' que indica que se deben retirar las barras de control para producir potencia.

- Si el valor `temperature * neutrons_produced_per_second` está dentro del 10% de `threshold` (es decir, entre un 0 y un 10% por debajo del umbral, en el umbral, o entre un 0 y un 10% por encima del umbral), el reactor está en _criticidad_ y se debe devolver el código de estado 'NORMAL', que indica que el reactor está en condiciones óptimas y que las barras de control están en una posición ideal.

- Si `temperature * neutrons_produced_per_second` no está en los rangos anteriores, el reactor está entrando en fusión del núcleo y se debe devolver un código de estado 'DANGER' para apagar el reactor de inmediato.

```python
>>> fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)
'DANGER'
```

## Source

### Created by

- @sachsom95
- @BethanyG

### Contributed to by

- @kbuc