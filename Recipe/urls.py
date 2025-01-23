from django.urls import path
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='recipe_index'),
    path('list/', views.recipe_list, name='recipe_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:recipe>', views.recipe_detail, name='recipe_detail'),
]