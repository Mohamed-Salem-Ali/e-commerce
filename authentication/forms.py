from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Order
from .models import Customer


# Form for user registration, extending Django's built-in UserCreationForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields to be included in the form


# Form for handling Customer model data
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__' # Include all fields from Customer model
		exclude = ['user'] # Exclude the 'user' field 
            

# Form for handling Order model data
class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__' # Include all fields from Order model