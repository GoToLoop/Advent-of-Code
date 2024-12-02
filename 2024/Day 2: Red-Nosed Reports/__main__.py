#!/usr/bin/env python

from collections import Counter
from collections.abc import Iterable, Sequence
from typing import cast

def read_file_as_2d_int_tuple(filename='input.txt'):
	"""
	Reads a file and converts its lines into a 2D tuple of integers.

	Arg:
		filename (str): Name of the file to read from. Defaults to 'input.txt'.

	Returns:
		tuple[tuple[int, int], ...]: A 2D tuple where each inner tuple contains
		two integers.
	"""

	with open(filename) as f: return cast(
		tuple[tuple[int, int], ...],
		tuple( tuple(map(int, line.split())) for line in f.readlines() )
	)


def split_and_sort_container_as_two_lists(lines: Iterable[Iterable[int]]):
	"""
	Splits the input lines into two lists and sorts them.

	Arg:
		lines (Iterable[Iterable[int]]): A 2D iterable containing int values.

	Returns:
		tuple[tuple[int, ...], tuple[int, ...]]: A 2D tuple containing two
		sorted lists of integers.
	"""

	# `pair` is a zip containing the input lines split as 2 containers:
	pair: zip[Iterable[int]] = zip(*lines, strict=True)

	# Sort `pair` as `lefts` & `rights` int lists:
	lefts, rights = map(sorted, pair)

	# Return both sorted lists as a 2D tuple of integers:
	return tuple(lefts), tuple(rights)


def solution1():
	"""
	Calculates and prints the total distance between corresponding
	elements of the sorted pairs of values.
	"""

	# Calculate the total distance:
	total_dist = total_distance(lefts, rights)

	# Print the total_distance()'s result:
	print(f'{total_dist = }') # 1651298


def total_distance(lefts: Sequence[int], rights: Sequence[int]):
	"""
	Calculates the total distance as the sum of the absolute differences
	between corresponding elements of the sorted pairs of values.

	Args:
		lefts (Sequence[int]): A sequence containing the left integers.
		rights (Sequence[int]): A sequence containing the right integers.

	Returns:
		int: The total sum of the absolute differences between corresponding
		elements of the `lefts` and `rights` sequences. This value represents 
		the total distance between the sorted pairs of values.
	"""

	# Calculate the total sum of the absolute differences for each pair:
	return sum( abs(rights[idx] - lefts[idx]) for idx in range(len(lefts)) )


def solution2():
	"""
	Calculates and prints the total similarity between the left
	integers and the count of the right integers.
	"""

	# Calculate the total similarity:
	total_similar = total_similarity(lefts, Counter(rights))

	# Print the total_similarity()'s result:
	print(f'{total_similar = }')


def total_similarity(ints: Iterable[int], counter: dict[int, int]):
	"""
	Calculates the total similarity as the sum of the products of integers and
	their counts.

	Args:
		ints (Iterable[int]): An iterable containing integer values.
		counter (dict[int, int]): A counter dict containing the counts of 
		id integer values.

	Returns:
		int: The total sum of the products of integers and their counts. This
		value represents the total similarity.
	"""

	# Calculate the total sum of the products for each integer and its count:
	return sum( id * counter[id] for id in ints )


# Read the input file and convert it to a 2D tuple of integers:
lines = read_file_as_2d_int_tuple()

# Split and sort the input lines into `lefts` and `rights` lists:
lefts, rights = split_and_sort_container_as_two_lists(lines)

solution1() # total_dist = 1651298
solution2() # total_similar = 21306195
