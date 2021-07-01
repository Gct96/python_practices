Pizzas=['KFC','GoldenDoor','pepperoni']
for pizza in Pizzas :
	print(f'I like {pizza} pizza.')
print('I really love pizza!')

friend_pizzas=Pizzas[:]
Pizzas.append('Mcdonla')
friend_pizzas.append('hualaishi')

print('My favourite pizzas are:')
print(Pizzas)
print("My friend's favourite pizzas are:")
print(friend_pizzas)
