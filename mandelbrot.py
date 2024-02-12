from typing import Callable
from cmath import sqrt


class Mandelbrot:
	def __init__(self, magnitude: int, max_iterations: int):
		self.magnitude = magnitude
		self.max_iterations = max_iterations

	def __call__(self, c: complex, z: complex = 0, count=0) -> int:
		count += 1

		m = z ** 2 + c

		if abs(m) > self.magnitude:
			return count
		elif count < self.max_iterations:
			return self(c, m, count)
		else:
			return 0
