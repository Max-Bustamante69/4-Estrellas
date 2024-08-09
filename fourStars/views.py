
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Avg
from .models import Professor

#create your views here
def home(request):
    # return HttpResponse("<h1>Four Stars Project</h1>")
    return render(request, 'home.html', {'name': 'Valeria'})

def about(request):
    return HttpResponse("<h1>About Four Stars </h1>")

from django.db.models import Avg

def professor_list(request):
    search_query = request.GET.get('q', '')
    order_by = request.GET.get('order_by', 'last_name')
    sort_direction = request.GET.get('sort_direction', 'asc')

    # Annotate with average rating
    professors = Professor.objects.annotate(
        average_rating=Avg('ratings__rating')
    )
    
    if search_query:
        professors = professors.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(courses__name__icontains=search_query)
        ).distinct()

    # Determine sort direction
    if sort_direction == 'desc':
        professors = professors.order_by(f'-{order_by}')
    else:
        professors = professors.order_by(order_by)

    return render(request, 'professor_list.html', {
        'professors': professors,
        'order_by': order_by,
        'sort_direction': sort_direction,
        'search_query': search_query
    })
