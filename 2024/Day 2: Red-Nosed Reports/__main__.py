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
		array('B', map( int, line.split() )) for line in f.readlines()
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
	Determines & prints the number of reports that contain safe sequence levels.
	"""

	safe_level_reports = sum(map(is_safe_level_sequence, level_reports))

	# Print the number of reports that contain safe sequence levels:
	print(f'{safe_level_reports = }')


def is_really_ascending(ints: Sequence[int], max_fails=1):
	"""
	Determines if a sequence is initially ascending.

	Args:
		ints (Sequence[int]): A sequence of integer levels to check.

		max_fails (int): Maximum tolerance for bad level readings.

	Returns:
		Optional[bool]: None if the sequence has fewer than 2 elements or the
		first two elements are equal. True if the first two elements are in
		ascending order. False otherwise.
	"""

	if (size := len(ints)) < 2: return None

	for i in range(size - 1):
		if ints[i] == ints[i + 1]:
			if (max_fails := max_fails - 1) < 0: return None

		else: return ints[i] < ints[i + 1]


def is_safe_level_sequence(ints: Sequence[int], max_fails=1, max_dif=3):
	"""
	Checks if a reactor report of sequence levels are within safety limits.
	Levels should always be increasing or decreasing, never staying the same.
	Also, the level change readings should never be higher than `max_dif`.
	However, the reactor has a fail tolerance of up to `max_fails`.

	Args:
		ints (Sequence[int]): A sequence of positive integer levels to check.

		max_fails (int): Maximum tolerance for bad level readings.

		max_dif (int): Maximum allowed difference between consecutive levels.

	Returns:
		bool: True if the level sequence is safe. False if it's unsafe.
	"""

	# Make sure params are positive:
	max_fails = abs(max_fails); max_dif = abs(max_dif)

	# "Unsafe" if no direction was found after more than `max_fails` attempts.
	# Otherwise, store the initial direction of the sequence in `up0`:
	if (up0 := is_really_ascending(ints, max_fails)) is None: return False

	up = up0; i = int(0) # current direction & loop iterator variable
	tail = len(clone := [ *ints ]) - 1 # last index & clone of ints as a list

	while i < tail: # loop ends at penultimate level value

		# Range subtraction order based on initial ascend or descend:
		dif = clone[i+1] - clone[i] if up else clone[i] - clone[i+1]

		# Update current direction `up` based on `dif` comparison & initial
		# direction `up0`:
		up = dif > 0 if up0 else dif < 0

		# Skip to next iteration if no fail on `dif` level pair comparison:
		if 0 < dif <= max_dif: i += 1; continue

		# Fails if `dif` is more than `max_dif` or there was no change or `dif`
		# was negative; meaning an unexpected direction change occurred

		# Decrease attempts and return "unsafe" if no attemps are left:
		if (max_fails := max_fails - 1) < 0: return False

		# Decrease sequence size b/c a `del` has to happen after a fail.
		# Already at the end; nothing more to compare; so levels are "safe":
		if i == (tail := tail - 1): break

		# If we're checking the head level, lookahead to 3rd level value:
		if i == 0:

			# Find range `dif` between 1st & 3rd level values:
			dif = clone[i+2] - clone[i] if up else clone[i] - clone[i+2]

			# If it fails, `del` head level & 2nd level becomes the new head
			# having next loop iteration visiting it:
			if dif <= 0 or dif > max_dif: del clone[i]

			# Otherwise `del` 2nd level. Current level will still be the head
			# level value next loop iteration:
			else: del clone[i+1]

			continue # next iteration will be same index

		# Decide whether to remove the left or the right side of the level pair
		# by looking behind 1st; that is, previous & right side level:
		dif = clone[i+1] - clone[i-1] if up else clone[i-1] - clone[i+1]

		# Check if the lookbehind succeeds. If so `del` current left level.
		# The right side level will be current left level on next iteration:
		if 0 < dif <= max_dif: del clone[i]

		else:
			# Calculate range `dif` between current level & next level after
			# the right side level (lookahead):
			dif = clone[i+2] - clone[i] if up else clone[i] - clone[i+2]

			# Check if the lookahead succeeds. if so `del` right side level.
			# And advance the while loop variable so next iteration will be the
			# level after the deleted right side level:
			if 0 < dif <= max_dif: del clone[i+1]; i += 1

			# Otherwise, arbitrarily `del` the current left side level.
			# Next iteration will be the right side level:
			else: del clone[i]

	return True # level sequence is safe if loop fully completed


# Read the input file and convert it to a tuple of uint8 arrays:
level_reports = read_file_as_2d_int_tuple()

day_2_part_1_solution() # safe_level_reports = 663
day_2_part_2_solution() # safe_level_reports = 692
