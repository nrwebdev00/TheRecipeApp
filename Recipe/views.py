from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from .models import Recipe, Directions,Ingredient,Recipe_Images

def index(request):
    name = 'nathon'
    context = {'name': name}
    return render(request, 'Recipe/index.html', context)


def recipe_list(request):
    recipes_list = Recipe.objects.all()
    # Pagination
    paginator = Paginator(recipes_list, 4)
    object_count = paginator.count
    per_page = paginator.per_page
    page_number = request.GET.get('page', 1)



    # Error Handling on Pagination -
    try:
        recipes = paginator.page(page_number)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    context = {'recipes': recipes,'object_count':object_count, 'per_page':per_page,}
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