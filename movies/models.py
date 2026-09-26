from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):

    STATUS_CHOICES = [
        ("want", "Baxmaq istəyirəm"),
        ("watching", "Baxıram"),
        ("watched", "Baxmışam"),
    ]

    title = models.CharField(max_length=200)

    genre = models.CharField(max_length=100)

    release_year = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="want"
    )
    
    rating = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    def __str__(self):
        return self.title