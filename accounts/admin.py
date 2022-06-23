from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User,Point

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username',)

admin.site.register(User, UserAdmin)


class PointAdmin(admin.ModelAdmin) :
    list_display = ('user','place','action','calculation','point','point_now')

admin.site.register(Point,PointAdmin)