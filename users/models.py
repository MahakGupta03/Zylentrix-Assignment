from django.db import models

class User(models.Model):
    """
    Model representing a user with name, email, and age.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name