# Proyecto Final: Tic-Tac-Toe (Fundamentos de Python 1 - PE1)

Programa en consola que simula una partida de *tic-tac-toe* entre el usuario y la maquina.

## Reglas

- La maquina juega con `X`; el usuario juega con `O`.
- El primer movimiento es de la maquina: siempre coloca una `X` en el centro (cuadro 5).
- Los cuadros se numeran del `1` al `9`, de izquierda a derecha y de arriba abajo.
- El usuario ingresa el numero del cuadro elegido; debe ser un entero de 1 a 9 y no estar ocupado.
- Tras cada movimiento se verifica el estado: el juego continua, hay empate, gana el usuario o gana la maquina.
- No hay inteligencia artificial: la maquina elige un cuadro libre al azar (`randrange()`).

## Estructura del codigo (`tic_tac_toe.py`)

| Funcion | Descripcion |
|---|---|
| `display_board(board)` | Dibuja el tablero en la consola. |
| `enter_move(board)` | Pide y valida el movimiento del usuario y lo registra como `O`. |
| `make_list_of_free_fields(board)` | Devuelve la lista de cuadros libres como tuplas `(fila, columna)`. |
| `victory_for(board, sgn)` | Revisa filas, columnas y diagonales; devuelve `'you'`, `'me'` o `None`. |
| `draw_move(board)` | La maquina coloca una `X` en un cuadro libre al azar. |
| `main()` | Ciclo principal del juego. |

El tablero es una lista de tres listas de tres elementos, accesible como `board[fila][columna]`.

## Requisitos

- Python 3.8 o superior ([python.org/downloads](https://www.python.org/downloads/)). No requiere librerias externas.

## Ejecucion en IDLE

1. Abre **IDLE** (menu Inicio > "IDLE (Python 3.x)").
2. Menu **File > Open...** y selecciona `tic_tac_toe.py`.
3. En la ventana del archivo, pulsa **F5** (o **Run > Run Module**).
4. El juego aparece en la ventana *Shell*. Escribe un numero del 1 al 9 en `Ingresa tu movimiento:` y pulsa Enter.

## Ejecucion en Visual Studio Code

1. Instala [VS Code](https://code.visualstudio.com/) y la extension **Python** (de Microsoft) desde el panel Extensions (`Ctrl+Shift+X`).
2. **File > Open Folder...** y abre la carpeta con `tic_tac_toe.py`.
3. Elige el interprete: `Ctrl+Shift+P` > **Python: Select Interpreter** > una version de Python 3.
4. Ejecuta el archivo con el boton **Run Python File** (triangulo arriba a la derecha) o desde la terminal integrada (`Ctrl+\``):

   ```bash
   python tic_tac_toe.py      # en Windows
   python3 tic_tac_toe.py     # en macOS / Linux
   ```

5. Escribe tus movimientos en la terminal integrada.

## Ejemplo de salida

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
```
