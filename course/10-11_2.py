import json
with open('favourite_number.json') as f:
	number=json.load(f)
print(f'I know your favourite number!It is {number}')