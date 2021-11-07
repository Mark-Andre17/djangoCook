from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}
    return render(request, template_name='cookbook/home.html', context=context)


def recipe_view(request, recipe_name):
    if recipe_name in DATA:
        recipe = DATA[recipe_name]
        servings = request.GET.get('servings', None)
        if servings:
            result = dict()
            for key, value in recipe.items():
                new_value = value * int(servings)
                result[key] = new_value
            context = {
                'recipe_name': recipe_name,
                'recipe': result
            }
        else:
            context = {
                'recipe_name': recipe_name,
                'recipe': recipe
            }
    else:
        context = None
    return render(request, template_name='cookbook/index.html', context=context)
