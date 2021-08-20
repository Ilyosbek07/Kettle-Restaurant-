from random import randrange

array = [34, 65, 23, 23, 12, 53, 54, 34, 23, 1, 4, 3, 53]


def qsort():
	if len(array) < 2:
		return array
	else:
		pivot = array.pop(randrange(len(array)))
		kichik = [i for i in array if i <= pivot]
		katta = [i for i in array if i >= pivot]
		return qsort(kichik) + [pivot] + qsort(katta)

array = [34, 65, 23,  12, 53, 54, 34, 23, 1, 4, 3, 53]

print(array)
print(qsort(array))
