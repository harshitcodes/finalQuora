from django.db import models
from django.contrib.auth.models import User, AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class MyUser(AbstractUser):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', blank = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    dob = models.DateField(blank=True, null=True)
    #phone = PhoneNumberField(unique = True, null=True, blank=True, help_text=('Only Indian'))
    street_address = models.CharField(max_length = 100, null=True, blank=True)
#    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    pincode = models.CharField(max_length=8, default="0000000")
    following = models.ManyToManyField("self", symmetrical = False, related_name = "follower")
   
	
class Profile(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30, blank = True)
	Profile_Pic = models.ImageField(upload_to = 'User_ProfilePics/', blank = True)
	followers = models.ManyToManyField(MyUser, related_name = 'following_me')
	
	def __str__(self):
	  return self.first_name