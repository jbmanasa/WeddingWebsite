from django.db import models
from random_word import RandomWords


INVITED_BY_LIST = [
    ("Kishan", "Kishan"),
    ("Manasa", "Manasa")]

def random_code():
    word_generator = RandomWords()
    return word_generator.get_random_word(minLength=4, maxLength=8).upper()


class Family(models.Model):
    family = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    invited_by = models.CharField(max_length=20, choices=INVITED_BY_LIST, default="Manasa")
    code = models.CharField(max_length=12, default=random_code, editable=False, unique=True)

    invited_haldi = models.BooleanField(default=False)
    invited_mehendi = models.BooleanField(default=False)
    invited_pre_wedding_party = models.BooleanField(default=False)
    invited_wedding = models.BooleanField(default=False)

    comments = models.CharField(max_length=512, blank=True)
    rsvp_date = models.DateTimeField('rsvp_date', auto_now=True)

    def __str__(self):
        return self.family


class Guest(models.Model):
    name = models.CharField(max_length=200, blank=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    attending_haldi = models.BooleanField(default=False)
    attending_mehendi = models.BooleanField(default=False)
    attending_pre_wedding_party = models.BooleanField(default=False)
    attending_wedding = models.BooleanField(default=False)
