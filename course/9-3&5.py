class User:
	def __init__(self,first_name,last_name,location,phone):
		self.first_name=first_name
		self.last_name=last_name
		self.location=location
		self.phone=phone
		self.login_attempts=0

	def describe_user(self):
		print(f'fullname:{self.first_name}{self.last_name}')
		print(f'location:{self.location}')
		print(f'phone:{self.phone}')

	def greet_user(self):
		print(f'Hello,{self.first_name}{self.last_name}')

	def increament_login_attempts(self):
		self.login_attempts+=1

	def reset_login_attempts(self):
		self.login_attempts=0

user1=User('jefer','Mike','Newyork',846541)
user1.describe_user()
user1.greet_user()
user1.increament_login_attempts()
user1.increament_login_attempts()
user1.increament_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

# class Admin(User):
# 	def __init__(self,first_name,last_name,location,phone):
# 		super().__init__(first_name,last_name,location,phone)
# 		self.privileges=['can add post','can delete post','can ban users']
# 	def show_privileges(self):
# 		print(self.privileges)

# admin=Admin('jack','Daosen','London','5201314')
# admin.describe_user()
# admin.show_privileges()

class Admin(User):
	def __init__(self,first_name,last_name,location,phone):
		super().__init__(first_name,last_name,location,phone)
		self.privileges=Privileges()


class Privileges:
	def __init__(self,privileges=['can add post','can delete post','can ban users']):
		self.privileges=privileges
	def show_privileges(self):
		print(self.privileges)

admin=Admin('jack','Daosen','London','5201314')
admin.describe_user()
admin.privileges.show_privileges()