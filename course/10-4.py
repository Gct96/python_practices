while True:
	name=input('pls input your name: ')
	if name=='quit':
		break
	else:
		print(f'Hello,{name}')
		with open('guest_book.txt','a') as file_object:
			file_object.write(f'Guest {name} visited!\n')