from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    CATEGORY_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids')
    )

    LIKE_CHOICES = (
        ('sports', 'Sports'),
        ('music', 'Music'),
        ('reading', 'Reading'),
        ('game', 'Games'),
        ('technology', 'Technology'),
        ('movies', 'Movies'),
        ('languages', 'Languages'),
        ('fashion', 'Fashion'),
    )

    GRADE_CHOICES = (
        ('2nd', 'Second Grade'),
        ('3nd', 'Third Grade'),
        ('4nd', 'Fourth Grade'),
        ('5nd', 'Fifth Grade'),
        ('6nd', 'Sixth Grade'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    what_do_you_like = MultiSelectField( choices=LIKE_CHOICES, max_choices=4)

    school_grade = models.CharField(max_length=10, choices=GRADE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'