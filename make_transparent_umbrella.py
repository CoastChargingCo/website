"""Remove solid beige background from red-umbrella.png."""
from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'assets' / 'red-umbrella.png'
BG = (234, 219, 183)
TOLERANCE = 22


def color_close(a: tuple[int, int, int], b: tuple[int, int, int], tol: int) -> bool:
    return all(abs(a[i] - b[i]) <= tol for i in range(3))


def remove_background(path: Path) -> None:
    image = Image.open(path).convert('RGBA')
    width, height = image.size
    pixels = image.load()
    visited = [[False] * width for _ in range(height)]
    queue: deque[tuple[int, int]] = deque()

    def try_seed(x: int, y: int) -> None:
        if visited[y][x]:
            return
        r, g, b, _ = pixels[x, y]
        if color_close((r, g, b), BG, TOLERANCE):
            visited[y][x] = True
            queue.append((x, y))

    for x in range(width):
        try_seed(x, 0)
        try_seed(x, height - 1)
    for y in range(height):
        try_seed(0, y)
        try_seed(width - 1, y)

    while queue:
        x, y = queue.popleft()
        pixels[x, y] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], 0)
        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= nx < width and 0 <= ny < height and not visited[ny][nx]:
                r, g, b, _ = pixels[nx, ny]
                if color_close((r, g, b), BG, TOLERANCE):
                    visited[ny][nx] = True
                    queue.append((nx, ny))

    image.save(path, format='PNG')
    print(f'Wrote transparent {path.name} ({width}x{height})')


if __name__ == '__main__':
    remove_background(SRC)
