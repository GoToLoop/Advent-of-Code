#!/usr/bin/env python

from collections.abc import Iterable
import re

# Regex pattern to match "mul(xxx,yyy)", "do()", and "don't()":
MULTIPLICATION_PATTERN = re.compile(r'''
	mul\(
		(\d{1,3})	# (1) captured multiplicand integer (1 to 3 digits)
		,			# non-captured comma character
		(\d{1,3}) 	# (2) captured multiplier integer (1 to 3 digits)
	\)
    |
    	do\(\) 		# match the literal string "do()"
    |
    	don't\(\) 	# match the literal string "don't()"
''', re.VERBOSE)

def read_whole_file(filename='input.txt'):
	"""Reads the file and returns its entire content as a string.

	Arg:
		filename (str): Name of the file to read from. Defaults to 'input.txt'.

	Returns:
		str: the full content of the file as a string.
	"""

	with open(filename) as f: return f.read()


def mul(groups: Iterable[str]):
	"""Converts captured groups to integers, multiplies them, and returns their
	product.

	Arg:
		groups (Iterable[str]): Captured groups from the regex match.

	Returns:
		int: The product of the converted integer groups.
	"""

	factor_pair = map(int, groups) # convert captured groups to integers
	product = multiplier(factor_pair) # and multiply the factors

	return product # and then return their product


def multiplier(factor_pair: Iterable[int]):
	"""Multiplies two integers from the given iterable.

	Arg:
		factor_pair (Iterable[int]): A pair of integers to multiply.

	Returns:
		int: The product of the two integers.
	"""

	multiplicand, multiplier = factor_pair
	product = multiplicand * multiplier

	return product


def day_3_part_1_solution():
	"""Calculates the sum of all products found in the multiplication script."""

	sum_of_products = int(0) # sum collector for each found product

	# Iterate over all matches found by the regex in the multiplication script:
	for match in MULTIPLICATION_PATTERN.finditer(multiplication_script):
		if all(groups := match.groups()): # ensure we've got captured groups
			product = mul(groups) # multiply the captured groups
			sum_of_products += product # then add their product to the sum

	# Print the total sum of all multiplied found pairs:
	print(f'{sum_of_products = }')


def day_3_part_2_solution():
	"""Calculates the sum of all products found in the multiplication script
	with conditional enablement."""

	sum_of_products = int(0) # sum collector for each found & enabled product
	enabled = True # "do()" enables "mul()" and "don't()" disables it

	# Iterate over all matches found by the regex in the multiplication script:
	for match in MULTIPLICATION_PATTERN.finditer(multiplication_script):
		if (group := match.group()) == "do()": enabled = True
		elif group == "don't()": enabled = False

		elif enabled: # only multiply if last instruction was "do()"
			groups = match.groups() # grab the 2 captured factors 
			product = mul(groups) # then multiply them
			sum_of_products += product # collect their product result as a sum

	# Print the total sum of all multiplied found & enabled pairs:
	print(f'{sum_of_products = }')


multiplication_script = read_whole_file()

day_3_part_1_solution() # sum_of_products = 182619815
day_3_part_2_solution() # sum_of_products = 80747545
