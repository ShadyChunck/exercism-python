# Help

## Ejecutar las pruebas

Usamos [pytest][pytest: Getting Started Guide] como ejecutor de tests de nuestro sitio web.
Necesitarás instalar `pytest` en tu máquina de desarrollo si quieres ejecutar los tests del track de Python de forma local.
También deberías instalar los siguientes plugins de `pytest`:

- [pytest-cache][pytest-cache]
- [pytest-subtests][pytest-subtests]

Puedes encontrar información más detallada en nuestra [guía de tests de Python][Python track tests page].


### Cómo ejecutar los tests

Para ejecutar los tests incluidos, navega hasta la carpeta donde está guardado el ejercicio usando `cd` en tu terminal (_reemplaza `<exercise-folder-location>` de abajo con tu ruta_).
Los archivos de tests normalmente terminan en `_test.py` y son los mismos tests que se ejecutan en el sitio web cuando subes una solución.

Linux/MacOS
```bash
$ cd <path/to/exercise-folder-location>
```

Windows
```powershell
PS C:\Users\foobar> cd <path\to\exercise-folder-location>
```

<br>

Después, ejecuta el comando `pytest` en tu terminal, reemplazando `<exercise_test.py>` con el nombre del archivo de tests:

Linux/MacOS
```bash
$ python3 -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```

Windows
```powershell
PS C:\Users\foobar> py -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```


### Opciones comunes
- `-o` : sobrescribe el `pytest.ini` predeterminado (_puedes usar esto para evitar advertencias de marcadores_)
- `-v` : activa la salida detallada.
- `-x` : detiene la ejecución de los tests en el primer fallo.
- `--ff` : ejecuta los fallos del test anterior antes de ejecutar los demás casos de test.

Para más opciones, usa `python3 -m pytest -h` o `py -m pytest -h`.


### Cómo corregir las advertencias

Si no usas `pytest -o markers=task` al invocar `pytest`, podrías recibir un `PytestUnknownMarkWarning` en los tests que usan nuestra nueva sintaxis:

```bash
PytestUnknownMarkWarning: Unknown pytest.mark.task - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
```

Para evitar escribir `pytest -o markers=task` en cada test que ejecutes, puedes usar un archivo de configuración `pytest.ini`.
Hemos creado uno que puedes descargar desde el nivel superior del directorio del track de Python: [pytest.ini][pytest.ini].

También puedes crear tu propio archivo `pytest.ini` con el siguiente contenido:

```ini
[pytest]
markers =
    task: A concept exercise task.
```

Si colocas el archivo `pytest.ini` en el directorio _root_ o _working_ de los ejercicios de tu track de Python, se registrarán los marcadores y se detendrán las advertencias.
Puedes encontrar más información sobre los marcadores de pytest en la documentación de `pytest` sobre [cómo marcar funciones de test][pytest: marking test functions with attributes] y en la documentación de `pytest` sobre [cómo trabajar con marcadores personalizados][pytest: working with custom markers].

Puedes encontrar información sobre cómo personalizar las configuraciones de pytest en la documentación de `pytest` sobre [formatos de archivos de configuración][pytest: configuration file formats].


### Cómo ampliar tu IDE o editor de código

Muchos IDE y editores de código tienen soporte integrado para usar `pytest` y otras herramientas de calidad de código.
Puedes encontrar algunas opciones creadas por la comunidad en nuestra [página de herramientas del track de Python][Python track tools page].

[Pytest: Getting Started Guide]: https://docs.pytest.org/en/latest/getting-started.html
[Python track tools page]: https://exercism.org/docs/tracks/python/tools
[Python track tests page]: https://exercism.org/docs/tracks/python/tests
[pytest-cache]:http://pythonhosted.org/pytest-cache/
[pytest-subtests]:https://github.com/pytest-dev/pytest-subtests
[pytest.ini]: https://github.com/exercism/python/blob/main/pytest.ini
[pytest: configuration file formats]: https://docs.pytest.org/en/6.2.x/customize.html#configuration-file-formats
[pytest: marking test functions with attributes]: https://docs.pytest.org/en/6.2.x/mark.html#raising-errors-on-unknown-marks
[pytest: working with custom markers]: https://docs.pytest.org/en/6.2.x/example/markers.html#working-with-custom-markers

## Enviar tu solución

Puedes enviar tu solución con el comando `exercism submit arcade_game.py`.
Este comando subirá tu solución al sitio web de Exercism e imprimirá la URL de la página de la solución.

Es posible enviar una solución incompleta, lo que te permite:

- Ver cómo otras personas completaron el ejercicio
- Solicitar ayuda de un mentor

## ¿Necesitas ayuda?

Si quieres ayuda para resolver el ejercicio, consulta las siguientes páginas:

- La [documentación del track Python](https://exercism.org/docs/tracks/python)
- La [categoría de programación del track Python en el foro](https://forum.exercism.org/c/programming/python)
- La [categoría de programación de Exercism en el foro](https://forum.exercism.org/c/programming/5)
- Las [preguntas frecuentes](https://exercism.org/docs/using/faqs)

Si esos recursos no son suficientes, puedes enviar tu solución (incompleta) para solicitar mentoría.

A continuación tienes algunos recursos para obtener ayuda si te encuentras con algún problema:

- [The PSF](https://www.python.org) alberga las descargas de Python, la documentación y recursos de la comunidad.
- [Python Community Forums](https://discuss.python.org/) ayuda, discusión de PEP, desarrolladores del núcleo de Python y mucho más.
- [The Exercism Community on Discord](https://exercism.org/r/discord)
- [The Exercism Community Discussion Forums](https://forum.exercsim.org)
- [Python Community on Discord](https://pythondiscord.com/) es una comunidad muy útil y activa.
- [/r/learnpython/](https://www.reddit.com/r/learnpython/) es un subreddit pensado para quienes están aprendiendo Python.
- [#python on Libera.chat](https://www.python.org/community/irc/) aquí es donde los desarrolladores del núcleo del lenguaje se reúnen y sacan adelante su trabajo.
- [Free Code Camp Community Forums](https://forum.freecodecamp.org/)
- [Pythontutor](http://pythontutor.com/) para recorrer pequeños fragmentos de código paso a paso de forma visual.

Además, [StackOverflow](http://stackoverflow.com/questions/tagged/python) es un buen lugar para buscar tu problema o tu pregunta y ver si ya se ha respondido antes.
Si no es así, siempre puedes [preguntar](https://stackoverflow.com/help/how-to-ask) o [responder](https://stackoverflow.com/help/how-to-answer) la pregunta de otra persona.