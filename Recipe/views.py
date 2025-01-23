from django.shortcuts import render, get_object_or_404
from .models import Recipe, Directions,Ingredient,Recipe_Images

def index(request):
    name = 'nathon'
    context = {'name': name}
    return render(request, 'Recipe/index.html', context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes,}
    return render(request, 'Recipe/list.html', context)

def recipe_detail(request, year,month,day,recipe):
    recipe = get_object_or_404(
        Recipe,
        status=Recipe.Status.PUBLISHED,
        slug=recipe,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    ingredients = Ingredient.objects.filter(recipe=recipe.id)
    directions = Directions.objects.filter(recipe=recipe.id)
    images = Recipe_Images.objects.filter(recipe=recipe.id)
    context = {'recipe': recipe,'ingredients': ingredients, 'directions': directions, 'images': images,}
    return render(request, 'Recipe/detail.html', context)