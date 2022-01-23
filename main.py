nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:
	"""задагние 1 итератор"""

	def __init__(self, nested_list):
		self.nested_list = nested_list
		self.list_len = len(self.nested_list)
		self.cursor_1 = -1

	def __iter__(self):
		self.cursor_1 += 1
		self.cursor_2 = 0
		return self

	def __next__(self):
		if self.cursor_2 == len(self.nested_list[self.cursor_1]):
				iter(self)
		if self.list_len == self.cursor_1:
			raise StopIteration
		self.cursor_2 += 1
		list_ = self.nested_list[self.cursor_1][self.cursor_2 - 1]
		return list_

for item in FlatIterator(nested_list):
	print(item)

# flat_list = [item for item in FlatIterator(nested_list)]
# print(flat_list)

# flat_list = [item for nested in nested_list for  item in nested]
# print(flat_list)

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(nested_list_1):
	"""Задание 2 генератор"""

	for item in nested_list_1:
		for i in item:
			yield i


for item in flat_generator(nested_list_1):
	print(item)

