from django.contrib import admin
from .models import User, Categories, Listing, Bid, Comment, Watching


# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watching)