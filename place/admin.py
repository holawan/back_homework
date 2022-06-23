from django.contrib import admin

# Register your models here.

from .models import Place,ReviewImage,Review
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'place_tagline')


admin.site.register(Place, PlaceAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'content')


admin.site.register(Review, ReviewAdmin)


class ReviewImageAdmin(admin.ModelAdmin) :
    list_display = ('review',)

admin.site.register(ReviewImage,ReviewImageAdmin)