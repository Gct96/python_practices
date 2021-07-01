class Restaurant:
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def read_number(self):
		print(f'{self.number_served} people have come to this restaurant!')

	def open_restaurant(self):
		print(f'{self.restaurant_name} is now opening!')

	def set_number_served(self,number):
		self.number_served=number

	def increament_number_served(self,number):
		self.number_served+=number

my_restaurant=Restaurant('KFC','Western')

my_restaurant.describe_restaurant()
my_restaurant.set_number_served(200)
my_restaurant.read_number()
my_restaurant.open_restaurant()
my_restaurant.increament_number_served(100)
my_restaurant.read_number()

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['sweet','sour']
	def describe_icecream(self):
		print(self.flavors)

icecreamstand=IceCreamStand('DQ','Western')
icecreamstand.describe_icecream()

		