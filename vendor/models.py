from django.db import models
from accounts.models import User, UserProfile

# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)  # Unique related_name
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)  # Unique related_name
    vendor_name = models.CharField(max_length=50)
    vendor_license = models.ImageField(upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # Corrected method name
        return self.vendor_name
