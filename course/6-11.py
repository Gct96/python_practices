cities={
	'nanjing':{'country':'china','population':'50W','fact':'capatial of six dynasties'},
	'paris':{'country':'france','population':'40W','fact':'capatial of romantic'},
	'sydney':{'country':'australia','population':'30W','fact':'capatial of singers'},
}

# for  city,info in cities.items():
# 	print(f'\ncityname:{city}')
# 	country_name=f"{info['country']}"
# 	population_index=f"{info['population']}"
# 	fact_info=f"{info['fact']}"

# 	print(f'\tCountry:{country_name.title()}')
# 	print(f'\tpopulation:{population_index}')
# 	print(f'\tfact:{fact_info}')

for  city,infos in cities.items():
	print(f'\ncityname:{city}')
	for  key,value in infos.items() :
		if key=='country':
			print(f'\t{key}:{value.title()}')
		else:
			print(f'\t{key}:{value}')
		
		