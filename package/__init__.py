from .validates import validate_val, validate_tiny_int
from .error import TinyIntError

def tiny_int(val, call_back = None):
	try:
		if validate_val(val) and validate_tiny_int(val):
			return True
		else:
			raise TinyIntError()
	except TinyIntError as err:
		if call_back is not None:
			print(err)
		else:
			print(err)







