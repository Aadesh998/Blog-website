from django.contrib import admin
from coders.models import Postblog
from coders.models import comments

# Register your models here.
admin.site.register(Postblog)
admin.site.register(comments)
