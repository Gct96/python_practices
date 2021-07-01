text_messages=['I love China','She is my moonlight','It is my pet dog']
sent_messages=[]
def send_messages(text_messages,sent_messages):
	while text_messages:
		current_message=text_messages.pop()
		print(f'Printing message:{current_message}')
		sent_messages.append(current_message)

#定义一个函数遍历sent_messages列表
def show_messages(sent_messages):
	print('\nThe following messages have been printed:')
	for sent_message in sent_messages :
		print(sent_message)
	
send_messages(text_messages[:],sent_messages)
show_messages(sent_messages)

print(text_messages)
print(sent_messages)