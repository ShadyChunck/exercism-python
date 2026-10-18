# El juego de arcade del fantasma tragón

Te damos la bienvenida a El juego de arcade del fantasma tragón en el track Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.
Si te atascas con el ejercicio, consulta `HINTS.md`, pero primero intenta resolverlo sin usarlos :)

## Introduction

Python representa los valores verdadero y falso con el tipo [`bool`][bools], que es una subclase de `int`.
 En este tipo solo hay dos valores: `True` y `False`.
  Estos valores se pueden asignar a una variable:

```python
>>> true_variable = True
>>> false_variable = False
```

Podemos evaluar expresiones Boolean con los operadores `and`, `or` y `not`:

```python
>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
```

[bools]: https://docs.python.org/3/library/stdtypes.html#typebool

## Instructions

En este ejercicio, necesitas implementar algunas reglas de [Pac-Man][Pac-Man], el clásico juego de arcade de los años 80.

Tienes cuatro reglas para implementar, todas relacionadas con los estados del juego.

> _No te preocupes por cómo se derivan los argumentos, solo concéntrate en combinar los argumentos para devolver el resultado esperado._

## 1. Define si Pac-Man come un fantasma

Define la función `eat_ghost()` que toma dos parámetros (_si Pac-Man tiene una píldora de poder activa_ y _si Pac-Man está tocando a un fantasma_) y devuelve un valor Boolean si Pac-Man es capaz de comer un fantasma.
 La función debe devolver `True` solo si Pac-Man tiene una píldora de poder activa y está tocando a un fantasma.

```python
>>> eat_ghost(False, True)
...
False
```

## 2. Define si Pac-Man anota puntos

Define la función `score()` que toma dos parámetros (_si Pac-Man está tocando una píldora de poder_ y _si Pac-Man está tocando un punto_) y devuelve un valor Boolean si Pac-Man anotó puntos.
 La función debe devolver `True` si Pac-Man está tocando una píldora de poder o un punto.

```python
>>> score(True, True)
...
True
```

## 3. Define si Pac-Man pierde

Define la función `lose()` que toma dos parámetros (_si Pac-Man tiene una píldora de poder activa_ y _si Pac-Man está tocando a un fantasma_) y devuelve un valor Boolean si Pac-Man pierde.
 La función debe devolver `True` si Pac-Man está tocando a un fantasma y no tiene una píldora de poder activa.

```python
>>> lose(False, True)
...
True
```

## 4. Define si Pac-Man gana

Define la función `win()` que toma tres parámetros (_si Pac-Man se comió todos los puntos_, _si Pac-Man tiene una píldora de poder activa_ y _si Pac-Man está tocando a un fantasma_) y devuelve un valor Boolean si Pac-Man gana.
 La función debe devolver `True` si Pac-Man se comió todos los puntos y no perdió según las reglas definidas en la parte 3.

```python
>>> win(False, True, False)
...
False
```

[Pac-Man]: https://en.wikipedia.org/wiki/Pac-Man

## Source

### Created by

- @neenjaw

### Contributed to by

- @cmccandless
- @BethanyG