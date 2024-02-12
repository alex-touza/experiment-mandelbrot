from os import fsync

from PIL import Image, ImageDraw



class Canvas:
	def __init__(self, w: int, h: int):
		self.w = w
		self.h = h
		self._img = Image.new("RGB", (w, h), 'White')
		self._dib = ImageDraw.Draw(self._img)

	def row(self, y: int, color: list[str]):
		for x in range(self.w):
			self._dib.point([(x, y)], color[x])

	def save(self):
		self._img.save("output.png")
