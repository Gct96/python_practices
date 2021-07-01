# age=''
# while age!='quit' :
# 	age=input('What is your age? ')
# 	if age!='quit':
# 		age=int(age)
# 		if age<3 :
# 			print('free')
# 		elif age<12 :
# 			print('10 dollars')
# 		elif age>12:
# 			print('15 dollars')
# print('exit')

#法2：
# flag=True
# while flag:
# 	age=input('What is your age? ')
# 	if age=='quit':
# 		flag=False
# 		print('exit')
# 	else:
# 		age=int(age)
# 		if age<3 :
# 			print('free')
# 		elif age<12 :
# 			print('10 dollars')
# 		elif age>12:
# 			print('15 dollars')

#法三:
while True:
	age=input('What is your age? ')
	if age=='quit':
		print('exit')
		break
	else :
		age=int(age)
		if age<3 :
			print('free')
		elif age<12 :
			print('10 dollars')
		elif age>12:
			print('15 dollars')