from typing import Iterable

def interlace(it: Iterable):
	for i in range(2):
		j = 0
		for item in it:
			if j % 2 == i:
				yield item

			j += 1
