from django.db import models
from django.core.validators import RegexValidator

alphanumeric=RegexValidator(r'^[0-9a-zA-z]*$','Only alphanumeric characters are allowed')
# Create your models here.
class details(models.Model):
    username=models.CharField(max_length=20,null=False, validators=[alphanumeric])
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    email=models.EmailField(max_length=100,null=False,validators=[alphanumeric])
    password=models.CharField(max_length=50,null=False,validators=[alphanumeric])
    
    