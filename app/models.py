from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Staffs(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        category, on_delete=models.SET_NULL, related_name='staff_category', null=True)
    experience = models.FloatField()
    about = models.CharField(max_length=30)


class Tickets(models.Model):
    pass
