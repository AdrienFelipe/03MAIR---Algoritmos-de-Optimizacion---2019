# Actividades Tema 1

---
author: Adrien Felipe
date: 10/2019
---

### Versión
El código de este proyecto es únicamente compatible con Python 3

## Ejercicios
Los ejercicios están localizados dentro de `src\activity\` y agrupados por pregunta.  
Se puede ejecutar cada pregunta con uno de los comandos siguientes, desde la carpeta raíz del proyecto:  
```shell script
PYTHONPATH=src python src/activity/Activity1.py
PYTHONPATH=src python src/activity/Activity2.py
PYTHONPATH=src python src/activity/Activity3.py
PYTHONPATH=src python src/activity/Activity4.py
```

### Extras
He añadido dos programas más con ejercicios extras presentando la multiplicación
por la matriz identidad, y las etapas para calcular la matriz inversa:
```shell script
PYTHONPATH=src python src/activity/Activity5.py
PYTHONPATH=src python src/activity/Activity6.py
``` 

#### Nota 1
Todos los ejercicios están pensados para que se pueda alterar los valores de entrada
y que los outputs se adapten, reflejado con el comentario `# Inputs:`.  
Ej:
```python
# Inputs:
x = Vector((4, 5, 1))
scalar = 4

```

#### Nota 2
El código del **ejercicio 4.c** está parametrizado para generar una matriz A de dimensión 100x100 y elevarla a potencia 10.
De esta forma tarda 10 segundos, ya que 500x500 ** 10000 no es capaz de acabar los cálculos en un tiempo aceptable.
Pero se puede cambiar perfectamente el script para ejecutar los valores requeridos:
 ```python
# src/activity/Activity4.py:
# 4.c ----------------------------

# Inputs:
dimension = 500
power = 10000
```

### Funciones requeridas
Las funciones requeridas por los ejercicios están dentro de `src/requirements`, cada una en su fichero correspondiente,
pero estas usan internamente las classes definidas en el resto del proyecto:
- Vector
- Matrix  

Y cada una de estas clases llama a sub-clases organizadas por ficheros dentro de su carpeta `src/*/tools`  

### Tests
Los ejercicios están bajo test, asi como las funciones necesarias para cumplir con los ejercicios.
Los tests son compatibles con unittest y deberían funcionar con una instalación basica de python 3.
Para ejecutar los tests desde la linea de comando, desde la carpeta raiz del proyecto:
```shell script
PYTHONPATH=src python -m unittest -v
```

## Nota
Estoy descubriendo Python por primera vez, y aún descontrolo la gestión correcta de namespaces y sus importaciones.  
La configuración actual funciona con los paquetes por defecto de Python 3, tanto con ejecución desde linea de comando
(ubuntu) como desde el IDE (PyCharm). Aún así es muy probable que no sea la forma óptima de preparar un projecto Python 
y estoy impaciente de recibir tus recomendaciones, pero insisto en poder usar clases y tests.
