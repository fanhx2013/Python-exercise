class Restaurant(object):
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The restaurant's name is: " + self.restaurant_name)
		print("The cuisine type is: " + self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is opening.")

	def set_number_served(self, num):
		self.number_served = num
		print(self.number_served)

	def increment_number_served(self,num):
		self.number_served += num

my_restaurant = Restaurant('Hotpot','Chinese food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant = Restaurant('BBQ', 'meat')
print(restaurant.number_served)
restaurant.number_served = 20
print(my_restaurant.number_served)

restaurant.set_number_served(25)

restaurant.increment_number_served(5)
print(restaurant.number_served)