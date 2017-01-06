from django.db import models
# Create your models here.


class AccountHolder(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    profile_photo = models.ImageField(null=True, blank=True, height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    dob = models.DateField()
    about = models.TextField()

    def __str__(self):
        return self.username
