# Snake--Game-Python


## Controls

- Uses the arrow keys (Up, Down, Left, Right) to control the snake's movement.
- The game starts as soon as a direction key is pressed.

## Game Rules

- The snake cannot reverse its direction directly (e.g., from left to right without first going up or down).
- The game ends if the snake collides with the walls or its own body.

## How the Game Works

### Board and Dimensions

#### Grid Settings:
- **Rows**: 25
- **Columns**: 25
- **Tile Size**: 25 pixels

#### Window Dimensions:
- Dynamically set to `rows * tile_size` for both width and height.
- The window is centered on the screen using system resolution.

```python
rows, cols, tile_size = 25, 25, 25
wwidth, hheight = tile_size * rows, tile_size * cols
```