from canvas import Canvas
from interlace import interlace
from mandelbrot import Mandelbrot

WIDTH = 5000
HEIGHT = 5000
ITERATIONS = 100

canvas = Canvas(WIDTH, HEIGHT)
mandelbrot = Mandelbrot(2, ITERATIONS)
zoom = 2000

palette = [
	"Green",
	"Blue",
	"Red",
	"Pink",
	"Orange",
	"Purple",
	"Turquoise",
]

a = 3 + 8j


def get_point(x: int, y: int):
	global zoom, WIDTH, HEIGHT
	return (x - WIDTH / 2) / zoom, (y - HEIGHT / 2) / zoom


for yi, y in enumerate(interlace(range(HEIGHT))):
	colors: list[str] = []

	for x in range(WIDTH):
		_x, _y = get_point(x, y)

		m = mandelbrot(complex(_x, _y))

		c = 'Black' if m == 0 else palette[(m-1) % len(palette)]

		colors.append(c)

	canvas.row(y, colors)

	print(f"Drawing row {y}")

canvas.save()
