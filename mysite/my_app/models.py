from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Member(User):
    roll_no=models.IntegerField()
    college=models.CharField(max_length=300)
    phone_number=models.IntegerField()

class CreateForm(UserCreationForm):
    class Meta:
        model=Member
        fields=('username','password','email','phone_number','roll_no','college',)
