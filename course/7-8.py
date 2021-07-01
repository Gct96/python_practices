sanwich_orders=['tuna','pastrami','fruit','pastrami','pastrami']
finished_sandwiches=[]

print('pastrami has been sold out!')
while 'pastrami' in sanwich_orders:
	sanwich_orders.remove('pastrami')
	
while sanwich_orders:
	current_order=sanwich_orders.pop()
	print(f'I made your {current_order} sandwich')
	finished_sandwiches.append(current_order)

print('\nAll the sanwichs have been finished:')
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche)	
