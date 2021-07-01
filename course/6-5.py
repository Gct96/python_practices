rivers_country={'nile':'egypt','huanghe':'china','meigonghe':'laowo'}
for river,country in rivers_country.items() :
	print(f'The {river.title()} runs through {country.title()}')
for river in rivers_country.keys() :
	print(river)
for country in rivers_country.values() :
	print(country)