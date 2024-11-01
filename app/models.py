from django.db import models
from django.utils.translation import gettext_lazy as _

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

    @property
    def staff_count(self):
        return Staffs.objects.filter(category=self.id).count()


class Staffs(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        category, on_delete=models.SET_NULL, related_name='staff_category', null=True)
    experience = models.FloatField()
    about = models.CharField(max_length=30)


class Tickets(models.Model):
    PENDING = "Pending"
    IN_PROGRESS = "In_progress"
    COMPLETED = "Completed"
    STATUS_CHOICES = [
        (PENDING, _("Pending")),
        (IN_PROGRESS, _("In_progress")),
        (COMPLETED, _("Completed"))
    ]
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='ticket_user')
    staff = models.ForeignKey(
        Staffs, on_delete=models.SET_NULL, related_name='ticket_staff', null=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default=PENDING, max_length=20)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} raised issue."


class Feedback(models.Model):
    ticket = models.ForeignKey(
        Tickets, on_delete=models.CASCADE, related_name='feedback_ticket')
    rating = models.CharField(max_length=10)
    comment = models.TextField()

    def __str__(self):
        return f"{self.ticket.user.username} feedback with rating {self.rating}"


class Emergency_support(models.Model):
    PENDING = "Pending"
    IN_PROGRESS = "In_progress"
    SORTED = "Sorted"
    STATUS_CHOICES = [
        (PENDING, _("Pending")),
        (IN_PROGRESS, _("In_progress")),
        (SORTED, _("Sorted"))
    ]
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='support_user')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,
                              default=PENDING, max_length=20)

    def __str__(self):
        return f"{self.user.username} need emergency support."
