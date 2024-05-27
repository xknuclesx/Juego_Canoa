# Vikingo y el Cruce del Río

Este es un juego de lógica en Python donde debes ayudar al vikingo a cruzar el río junto con un lobo, Caperucita y unas uvas, evitando que el lobo se coma a Caperucita o que Caperucita se coma las uvas.

## Instrucciones del Juego

1. **Objetivo**: Llevar al vikingo, el lobo, Caperucita y las uvas al otro lado del río sin que ocurran incidentes.
2. **Restricciones**:
    - El vikingo debe estar presente para cualquier cruce.
    - Si el lobo y Caperucita se quedan solos en una orilla, el lobo se comerá a Caperucita.
    - Si Caperucita y las uvas se quedan solas en una orilla, Caperucita se comerá las uvas.

## Requisitos

- Python 3.12.3

## Instalación

1. Clona este repositorio o descarga los archivos `vikingo_game.py` y `test_vikingo_game.py`.
2. Asegúrate de tener Python 3.12.3 instalado en tu sistema. Puedes verificarlo con:
    ```sh
    python --version
    ```

## Ejecución del Juego

1. Navega al directorio donde descargaste los archivos.
2. Ejecuta el juego con el siguiente comando:
    ```sh
    python vikingo_game.py
    ```
3. Sigue las instrucciones en pantalla para mover los objetos de una orilla a la otra.

## Ejecución de las Pruebas Unitarias

1. Navega al directorio donde descargaste los archivos.
2. Ejecuta las pruebas unitarias con el siguiente comando:
    ```sh
    python test_vikingo_game.py
    ```
3. Verifica los resultados en la terminal. Las pruebas verificarán que las funciones del juego se comporten correctamente en diferentes escenarios.

## Estructura del Código

### `vikingo_game.py`

Contiene las funciones principales del juego:
- `es_estado_valido(orilla)`: Verifica si una orilla es segura.
- `cruzar_rio(orilla_izquierda, orilla_derecha, objeto, direccion)`: Realiza el cruce del río con el objeto seleccionado.
- `imprimir_estado(orilla_izquierda, orilla_derecha)`: Imprime el estado actual del juego.
- `animar_cruce(objeto, direccion)`: Muestra una animación básica del cruce.
- `limpiar_pantalla()`: Limpia la pantalla de la terminal.
- `juego()`: Controla el flujo principal del juego.

### `test_vikingo_game.py`

Contiene las pruebas unitarias para verificar las funciones del juego:
- `test_es_estado_valido()`: Prueba la función `es_estado_valido`.
- `test_cruzar_rio_derecha()`: Prueba el cruce hacia la derecha.
- `test_cruzar_rio_izquierda()`: Prueba el cruce hacia la izquierda.
- `test_cruzar_rio_objeto_no_en_orilla()`: Verifica el manejo de objetos que no están en la orilla actual.
- `test_estado_no_valido_despues_de_cruzar()`: Prueba estados no válidos después de un cruce.

## Autor

Desarrollado por Grupo 4
Integrantes:
- Adrian Paguay
- Mateo Pilco
- 
-

