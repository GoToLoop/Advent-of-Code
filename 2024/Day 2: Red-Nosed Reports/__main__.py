#!/usr/bin/env python

from collections.abc import Sequence
from array import array

def read_file_as_2d_int_tuple(filename='input.txt'):
	"""
	Reads a file and converts its lines into a 2D tuple of integers.

	Arg:
		filename (str): Name of the file to read from. Defaults to 'input.txt'.

	Returns:
		tuple[array[int], ...]: A tuple where each of its inner uint8 array
		contains 5 to 8 integers.
	"""

	with open(filename) as f: return *(
		array('B', map(int, line.split()) ) for line in f.readlines()
	),


def solution_1():
	"""
	Calculates and prints the total number of safe level reports.

	A safe level report is one where the sequence of integers is either
	strictly ascending within a specified maximum difference or strictly
	descending within the same limit.

	Additionally, consecutive levels must not repeat.

	The function reads level reports, checks each report for safety based on
	the defined criteria, and counts the number of safe reports.
	"""

	total_safe_level_reports = 0

	for levels in level_reports:
		if (ascending := is_ascending(levels)) is not None:
			if ascending:
				if is_always_ascending(levels): total_safe_level_reports += 1
			elif is_always_descending(levels): total_safe_level_reports += 1

	# Print the number of reports that contain safe sequence levels:
	print(f'{total_safe_level_reports = }')


def is_ascending(ints: Sequence[int]):
	"""
	Determines if a sequence is initially ascending.

	Arg:
		ints (Sequence[int]): A sequence of integers to check.

	Returns:
		Optional[bool]: None if the sequence has fewer than 2 elements or the
		first two elements are equal. True if the first two elements are in
		ascending order. False otherwise.
	"""

	return None if len(ints) < 2 or ints[0] == ints[1] else ints[0] < ints[1]


def is_always_ascending(ints: Sequence[int], max_diff=3):
	"""
	Checks if the sequence of positive integers is strictly ascending with
	differences	within a specified maximum difference.

	Args:
		ints (Sequence[int]): A sequence of positive integers to check.

		max_diff (int): Maximum allowed difference between consecutive integers.

    Returns:
		bool: True if the sequence is strictly ascending and each difference is
		within max_diff. False if any two adjacent elements are equal,
		descending, or exceed max_diff.
	"""

	for i in range(len(ints) - 1):
		diff = ints[i + 1] - ints[i]
		if diff <= 0 or diff > max_diff: return False
	return True


def is_always_descending(ints: Sequence[int], max_diff=3):
	"""
	Checks if the sequence of positive integers is strictly descending with
	differences	within a specified maximum difference.

	Args:
		ints (Sequence[int]): A sequence of positive integers to check.

		max_diff (int): Maximum allowed difference between consecutive integers.

    Returns:
		bool: True if the sequence is strictly descending and each difference is
		within max_diff. False if any two adjacent elements are equal,
		ascending, or exceed max_diff.
	"""

	for i in range(len(ints) - 1):
		diff = ints[i] - ints[i + 1]
		if diff <= 0 or diff > max_diff: return False
	return True


def solution_2():
	"""

	"""

	total_safe_level_reports = 0

	# Print the number of reports that contain safe sequence levels:
	print(f'{total_safe_level_reports = }')


def is_always_going_same_direction(ints: Sequence[int], tolerances=1, diff=3):
	"""

	"""




# Read the input file and convert it to a tuple of uint8 arrays:
level_reports = read_file_as_2d_int_tuple()

solution_1() # total_safe_level_reports = 663
solution_2() # total_safe_level_reports = 
