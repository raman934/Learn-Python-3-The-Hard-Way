i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)

	i += 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")
	print(end='\n\n')

print("The numbers: ")

for num in numbers:
	print(num, end=' ')
print()