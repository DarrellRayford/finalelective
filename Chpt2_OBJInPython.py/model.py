from django.utils import datetime


class Review:
    def __init__(self, text, user, movie, watch_again):
        self.text = text
        self.date = datetime.datetime.now()
        self.user = user
        self.movie = movie
        self.watch_again = watch_again

    def __str__(self):
        return self.text

    def get_review_details(self):
        return f"Review: {self.text}\nDate: {self.date}\nUser: {self.user}\nMovie: {self.movie.title}\nWatch Again: {self.watch_again}"