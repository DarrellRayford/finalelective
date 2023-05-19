from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images')
    url = models.URLField(blank=True)


# Single inheritance a class inherits from a single base class
# ActionMovie inherits from the 'Movie' class. 
# The ActionMovie class inherits all the properties and methods from the Movie class.
# A new method called play_action_scene() specific to action movies.
class ActionMovie(Movie):
    def play_action_scene(self):
        print("Playing an action scene!")


class Review(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()


# Multiple inheritance allows a class to inherit from multiple base classes.
# UserReview class inherits properties and methods from both the Review and User classes. 
# It adds a new method called get_user_name() to retrieve the name of the user who wrote the review.
class UserReview(Review, User):
    def get_user_name(self):
        return self.user.name

    def __str__(self):
        return self.text


# Hierarchical Inheritance:
# In hierarchical inheritance, multiple classes inherit from a single base class. 
# PositiveReview and NegativeReview, both inherit from the Review class:
# Both the PositiveReview and NegativeReview classes inherit the properties and methods from the Review class. 
# They introduce their own methods specific to positive or negative reviews.
class PositiveReview(Review):
    def is_positive(self):
        return True


class NegativeReview(Review):
    def is_negative(self):
        return True
