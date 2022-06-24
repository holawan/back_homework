from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User,PointLog

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username',)

admin.site.register(User, UserAdmin)


class PointLogAdmin(admin.ModelAdmin) :
    list_display = ('user','place','action','calculation','point',)

admin.site.register(PointLog,PointLogAdmin)

# class PointAdmin(admin.ModelAdmin) :
#     list_display = ('pk','point_now',)

# admin.site.register(Point,PointAdmin)