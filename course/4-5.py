numbers=list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print('The first three items in the list are:')
for number in numbers[0:3]:
	print(number)

print('Three items from the middle of the list are:')
for number in numbers[499998:500001]:
	print(number)

print('The last three items in  the list are:')
for number in numbers[-3:]:
	print(number)