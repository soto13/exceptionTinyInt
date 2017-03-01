class TinyIntError(Exception):
	def __init__(self):
		self.message = 'el numero no cuenta con las caracteristicas de un numero tiny int'

	def __str__(self):
		return self.message







