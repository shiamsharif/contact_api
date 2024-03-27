from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128, null=False)
    phone_number = PhoneNumberField()
    email = models.EmailField()


#  pipenv install django-phonenumber-field[phonenumberslite] {it's not worked}

# step:1   
#   pip install "django-phonenumber-field[phonenumbers]"

# step:2      
#   set-up:
#   INSTALLED_APPS = [
#         # Other apps…
#       "phonenumber_field",
#   ]
    
# step:3
#     from django.db import models
#     from phonenumber_field.modelfields import PhoneNumberField


#     class Customer(models.Model):
#         name = models.TextField()
#         # An optional phone number.
#         phone_number = PhoneNumberField(blank=True)