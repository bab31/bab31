from django.db import models
# Model nameed Post


class Post(models.Model):
    Male = 'M'
    Female = "F"
    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, "Female"),

    )

    # Define a user name field with bound max length it can have
    username = models.CharField(max_length=20, blank=False, null=False)
    # This is used to write a post
    text = models.TextField(blank=False, null=False)
    # values for gender are resticted by giving choices
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, default=Male)
    time = models.DateTimeField(auto_now_add=True)
