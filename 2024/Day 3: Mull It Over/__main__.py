#!/usr/bin/env python

from collections.abc import Sequence
from array import array

def read_file_as_2d_int_tuple(filename='input.txt'):
	"""
	Reads a file and converts its lines into a 2D tuple of integers.

	Arg:
		filename (str): Name of the file to read from. Defaults to 'input.txt'.

	Returns:
		tuple[array[int], ...]: A tuple where each of its inner uint8 arrays
		contains 5 to 8 integers.
	"""

	with open(filename) as f: return *(
		array('B', map(int, line.split()) ) for line in f.readlines()
	),


def day_2_part_1_solution():
	"""
	Calculates and prints the total number of safe level reports.

	A safe level report is one where the sequence of integers is either
	strictly ascending within a specified maximum difference or strictly
	descending within the same limit.

	Additionally, consecutive levels must not repeat.

	The function reads level reports, checks each report for safety based on
	the defined criteria, and counts the number of safe reports.
	"""

	safe_level_reports = 0

	for levels in level_reports:
		if (ascending := is_ascending(levels)) is not None:
			if ascending:
				if is_always_ascending(levels): safe_level_reports += 1
			elif is_always_descending(levels): safe_level_reports += 1

	# Print the number of reports that contain safe sequence levels:
	print(f'{safe_level_reports = }')


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


def is_always_ascending(ints: Sequence[int], max_dif=3):
	"""
	Checks if the sequence of positive integers is strictly ascending with
	differences	within a specified maximum difference.

	Args:
		ints (Sequence[int]): A sequence of positive integers to check.

		max_dif (int): Maximum allowed difference between consecutive integers.

    Returns:
		bool: True if the sequence is strictly ascending and each difference is
		within `max_dif`. False if any two adjacent elements are equal,
		descending, or exceed `max_dif`.
	"""

	for i in range(len(ints) - 1):
		diff = ints[i + 1] - ints[i]
		if diff <= 0 or diff > max_dif: return False
	return True


def is_always_descending(ints: Sequence[int], max_dif=3):
	"""
	Checks if the sequence of positive integers is strictly descending with
	differences	within a specified maximum difference.

	Args:
		ints (Sequence[int]): A sequence of positive integers to check.

		max_dif (int): Maximum allowed difference between consecutive integers.

    Returns:
		bool: True if the sequence is strictly descending and each difference is
		within `max_dif`. False if any two adjacent elements are equal,
		ascending, or exceed `max_dif`.
	"""

	for i in range(len(ints) - 1):
		diff = ints[i] - ints[i + 1]
		if diff <= 0 or diff > max_dif: return False
	return True


def day_2_part_2_solution():
	"""

	"""

	safe_level_reports = sum(map(is_always_going_same_direction, level_reports))

	# Print the number of reports that contain safe sequence levels:
	print(f'{safe_level_reports = }')


def is_really_ascending(ints: Sequence[int], max_fails=1):
	"""
	Determines if a sequence is initially ascending.

	Arg:
		ints (Sequence[int]): A sequence of integers to check.

	Returns:
		Optional[bool]: None if the sequence has fewer than 2 elements or the
		first two elements are equal. True if the first two elements are in
		ascending order. False otherwise.
	"""

	if (size := len(ints)) < 2: return None

	for i in range(size - 1):
		if ints[i] == ints[i + 1]:
			if (max_fails := max_fails - 1) < 0: return print(f"\nFAIL!!!\n{ints = }\n")

		else: return ints[i] < ints[i + 1]


def is_always_going_same_direction(ints: Sequence[int], max_fails=1, max_dif=3):
	"""

	"""

	if (up := is_really_ascending(ints, max_fails)) is None: return False

	print(f'Initial direction: {"ascending" if up else "descending"}')

	i = int(0)
	tail = len(clone := [*ints]) - 1

	while i < tail:
		diff = clone[i + 1] - clone[i] if up else clone[i] - clone[i + 1]

		print(f'Checking {clone}, idx: {i}, diff: {diff}, max_fails: {max_fails}')

		if diff <= 0 or diff > max_dif:
			if (max_fails := max_fails - 1) < 0: return print(False) or False

			if i == (tail := tail - 1): break

			if i == 0:
				del clone[i]
				continue

			# Decide whether to remove the left or the right value based on future differences:
			if abs(clone[i + 2] - clone[i]) <= max_dif:
				del clone[i + 1]
			else:
				del clone[i]
				i -= 1

			continue

		i += 1

	return print(True) or True


# Read the input file and convert it to a tuple of uint8 arrays:
level_reports = read_file_as_2d_int_tuple()

day_2_part_1_solution() # safe_level_reports = 663
day_2_part_2_solution() # safe_level_reports = 687
