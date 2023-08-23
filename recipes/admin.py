from django.contrib import admin
from recipes.models import recipe

class recipe_admin(admin.ModelAdmin):
    list_display=('image', 'cat', 'name', 'ing', 'des')

admin.site.register(recipe, recipe_admin)

# Register your models here.
