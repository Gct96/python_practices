dinner_guest=['Swk','Zbj','Shs']
# print(f'{dinner_guest[0]},please come to have dinner with me!')
# print(dinner_guest[1]+',please come to have dinner with me!')
# print('%s,please come to have dinner with me!'%dinner_guest[2])

# print(f'{dinner_guest[2]} can not come.')
dinner_guest[2]='Tang'
# print(f'{dinner_guest[0]},please come to have dinner with me!')
# print(dinner_guest[1]+',please come to have dinner with me!')
# print('%s,please come to have dinner with me!'%dinner_guest[2])

print('I find a larger table')
dinner_guest.insert(0,'Bailong')
dinner_guest.insert(2,'Rulai')
dinner_guest.append('GuanY')
print(f'{dinner_guest[0]},please come to have dinner with me!')
print(dinner_guest[1]+',please come to have dinner with me!')
print('%s,please come to have dinner with me!'%dinner_guest[2])
print(f'{dinner_guest[3]},please come to have dinner with me!')
print(f'{dinner_guest[4]},please come to have dinner with me!')
print(f'{dinner_guest[5]},please come to have dinner with me!')

print('I can only invite two guests!')
popped_1=dinner_guest.pop()
print(f'{popped_1},I am very sorry that I cant invite you!')
popped_2=dinner_guest.pop()
print(f'{popped_2},I am very sorry that I cant invite you!')
popped_3=dinner_guest.pop()
print(f'{popped_3},I am very sorry that I cant invite you!')
popped_4=dinner_guest.pop()
print(f'{popped_4},I am very sorry that I cant invite you!')
print(f'{dinner_guest[0]},you still in the list!')
print(f'{dinner_guest[1]},you still in the list!')

del dinner_guest[0:2]
print(dinner_guest)