favourite_places={
	'jen':['nanjin','suzhou'],
	'sarah':['hangzhou','wenzhou'],
	'edward':['london','weinisi'],
	'phil':['newyork','california'],
}
for name,places in favourite_places.items() :
	print(f"\n{name.title()}'s favourite places are:")
	for place in places :
		print(f'\t{place.title()}')