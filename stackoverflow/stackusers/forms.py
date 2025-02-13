from django import forms  # Import Django's forms module
from django.contrib.auth.models import User  # Import the User model from Django's authentication system
from django.contrib.auth.forms import UserCreationForm  # Import the UserCreationForm for creating new users

# Define a new form class that inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Add an email field to the form, making it a required field
    email = forms.EmailField(required=True)

    # Define metadata for the form
    class Meta:
        # Specify that this form is associated with the User model
        model = User
        # Specify the fields to include in the form
        fields = ["username", "email", "password1", "password2"]
