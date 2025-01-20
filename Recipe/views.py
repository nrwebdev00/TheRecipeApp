from django.shortcuts import render

def index(request):
    name = 'nathon'
    context = {'name': name}
    return render(request, 'Recipe/index.html', context)
