"""
Main typo generation class designed for easy user usage.
Should implement:
- Letter inversion
- Wrong key
- Double letter
- Letter omission
"""

import random
from typing import Union, List
from typo_maker.helpers import KeyboardEnum, ModeEnum, punct, num


class TypoMaker:
	"""Typo Maker"""
	def __init__(self, key, seed = 42):
		self.key: KeyboardEnum = key
		self.seed: int = seed
		random.seed(set_seed)
		self.mode: ModeEnum = ModeEnum.full

	def do_typo(self, txt: Union[str, List[str]], proportion: float = .2):
		"""
		Main typo maker method. Assumes that either a word or a list of words is being processed.
		:param txt: Either a single word or a list of words

		:return: New word(s) and offset shift from original (e.g. "hello"->"helo", shift = -1)
		"""
		shift = 0
		if isinstance(txt, list):
			assert 0 <= proportion <= 1, f"`proportion` parameter must be in range (0;1), {proportion} found."
			# Processing words one by one
			for i, elem in enumerate(txt):
				assert isinstance(elem, str), f"List items must be `str`, `{type(elem)}` found."
				# We don't want to interact with 1-letter words
				if len(elem) == 1:
					continue
				if random.random() < proportion:
					# Replace word by modified word
					txt[i], new_shift = _do_typo(elem)

		elif isinstance(txt, str):
			if len(txt) == 1 or len(txt) == 0:
				print("0-char and 1-char words are not modifiable.")
				return txt, shift
			return _do_typo(txt)
		else:
			raise TypeError(f"Wrong text input type, `{type(txt)}` found.")


	def set_mode(self, mode):
		if mode not in ModeEnum:
			raise ValueError(f"mode `{mode}` is not available.")
		self.mode = mode


	def _do_typo(self, word):
		"""Make typo depending on TypoMaker's mode"""
		if self.mode == "invert":
			return self._invert(word)
		elif self.mode == "wrong":
			return self._wrong_key(word)
		elif self.mode == "duplicate":
			return self._duplicate(word)
		elif self.mode == "miss":
			return self._omission(word)
		else:
			#TODO: pick a mode randombly and perform it 
			pass
		return word

	def _invert(self, word):
		#TODO:
		# handle 2 char words DONE
		# handle 2+ char words
		if len(word) == 2:
			return word[1] + word[0], 0
		pass

	def _wrong_key(self, word):
		#TODO:
		# key mapping
		# handle uppercased letters to not alter case
		pass

	def _duplicate(self, word):
		pass

	def _omission(self, word):
		pass



#=========================================================

#maker = TypoMaker("be")

#maker.do_typo(["Clément", "a", "un", "micropéni"], .5) # -> ["Clémznt", "a", "un", "miropéni"]

#maker.set_mode("invert")
#maker.do_typo(["Clément", "a", "un", "micropéni"], .2) # -> ["Clément", "a", "un", "mircopéni"]
#maker.do_typo(["Clément", "a", "un", "micropéni"], 1.0) # -> ["Clémnet", "a", "nu", "micrpoéni"]

#maker.set_mode("wrong")
#maker.do_typo(["Clément", "a", "un", "micropéni"], .99) # -> ["Clépent", "a", "in", "mivropéni"]
