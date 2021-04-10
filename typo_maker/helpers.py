"""
Helper functions for typo generation
"""

from aenum import Enum


class KeyboardEnum(str, Enum):
	"""Available keyboards"""
	be = "be"


class ModeEnum(str, Enum):
	full = "full"
	invert = "invert"
	wrong = "wrong"
	duplicate = "duplicate"
	miss = "miss"