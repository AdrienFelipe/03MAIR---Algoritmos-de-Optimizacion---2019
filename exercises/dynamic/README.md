# Programación dinámica: Problema del viaje por el rio

## Enunciado
En un río hay n embarcaderos y debemos desplazarnos río abajo (no hay posibilidad de
remontar) desde un embarcadero a otro. Cada embarcadero tiene precios diferentes para ir
de un embarcadero a otro situado más abajo. Para ir del embarcadero i al j, puede ocurrir que
sea más barato hacer un trasbordo por un embarcadero intermedio k. El problema consiste
en determinar la **combinación más barata**.

## Solución
La clase [ShortestPath](src/ShortestPath.py) propone una solución al problema aplicando un algoritmo
de programación dinámica.

### Ejemplo
El test [test_ShortestPath](tests/test_ShortestPath.py) ejecuta un ejemplo aplicado al enunciado con 3
casos en cuales encontrar el camino más barato:
- Desdel primer hasta último nodo
- Desde un nodo que no sea el primero hasta el último nodo
- Desde el primer nodo a un nodo que no sea el último