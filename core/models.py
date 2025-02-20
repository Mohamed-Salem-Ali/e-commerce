from django.db import models
from django.contrib.auth.models import User
from authentication.models import Customer

# Product model representing items available for purchase
class Product(models.Model):
	name = models.CharField(max_length=50)
	price = models.FloatField()
	description  = models.CharField(max_length=300)
	image = models.ImageField(null=True, blank= True)  # Optional product image

	@property
	def imageURL(self):
		"""
		Returns the URL of the product image or a placeholder if no image is uploaded.
		"""
		try:
			url = self.image.url
		except:
			url = 'images/placeholder.png' # Default placeholder image
		return url
	def __str__(self):
		return self.name

# Order model representing a user's shopping cart or completed order
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)  # Status flag (whether order is completed)
	transaction_id = models.CharField(max_length=100, null=True)

	@property
	def get_cart_total(self):
		"""
		Calculates and returns the total cost of all items in the cart.
		
		"""
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		"""
		Returns the total number of items in the cart.
		
		"""
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 


	def __str__(self):
		return str(self.id)


# OrderItem model representing individual items in an order
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		"""
		Calculates and returns the total price for this order item.
		
		"""
		total = self.product.price * self.quantity
		return total

# ShippingAddress model representing the shipping details for an order
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address