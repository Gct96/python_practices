prompt='\npls input the peiliao of the pizza:'
prompt+='\nEnter quit to end the program. '
while True :
	peiliao=input(prompt)
	if peiliao=='quit':
		break
	else:
		print(f'We will add the {peiliao}')