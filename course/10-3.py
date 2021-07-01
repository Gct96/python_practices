filename='guest.txt'
name=input('pls input your name: ')
with open(filename,'w') as file_object :
	file_object.write(name)