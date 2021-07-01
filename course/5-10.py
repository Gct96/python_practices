current_users=['admin','mike','John','Joden','SuSan']
new_users=['Admin','Lisa','john','Jojo','Susan']
current_users2=[]
for current_user in current_users :
	current_users2.append(current_user.lower())
for new_user in new_users :
	if new_user.lower() in current_users2 :
		print(f'The name {new_user} has been used.pls input other names!')
	else :
		print(f'the name {new_user} has not been used.')

