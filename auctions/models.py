from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.category}"


class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    imageurl = models.URLField(max_length=200, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, related_name="listings", null=True)

    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    value = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.bidder} bid on {self.listing}"


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}: {self.bidder} comment on {self.listing}"


class Watching(models.Model):
    watcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watching")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchers")
    value = models.BooleanField()



# TODO: IMPLEMENT INHERITED CLASSES (ACTION?)