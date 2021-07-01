import json
number=input('pls input your favourite number: ')
with open('favourite_number.json','w') as f:
	json.dump(number,f)
	print('I will remember the num!')
