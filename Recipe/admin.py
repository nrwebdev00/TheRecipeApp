from django.contrib import admin
from .models import Recipe,Recipe_Images,Ingredient,Directions


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title','status','admin_status','author')
    list_filter = ('status','admin_status')
    search_fields = ('title','status')
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status','admin_status','author')
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe','name','group_number')
    ordering = ('recipe','group_number',)
    list_filter = ('recipe','group_number')

@admin.register(Directions)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('title','group_number')
    ordering = ('group_number','number')
    list_filter = ('recipe',)

@admin.register(Recipe_Images)
class Recipe_ImagesAdmin(admin.ModelAdmin):
    list_display = ('recipe','title','Image')
    ordering = ('recipe','title',)
    list_filter = ('recipe',)
