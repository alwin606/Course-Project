from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Park, Restaurants, Attractions, Place
from django.db.models import Q, Sum

# Create your views here.
# request -> response
# request handler
# action
def index_page(request):
    return render(request, 'index.html')

def park_page(request):
    park = Park.objects.all().order_by('date')
    data = []
    for p in park:
        total_sales = Restaurants.objects.filter(date=p.date).aggregate(total_sales=Sum('total_sales'))['total_sales']
        if total_sales is None:
            total_sales = 'N/A'
        data.append({'date': p.date, 'num_workers': p.num_workers, 'attendance': p.attendance, 'weather': p.weather,
                     'capacity': p.capacity, 'total_sales': total_sales})
    context = {'data': data}
    return render(request, 'park.html', context)
def submit_form_park(request):
    if request.method == 'POST':
        date = request.POST['date']
        num_workers = request.POST['num_workers']
        attendance = request.POST['attendance']
        weather = request.POST['weather']
        capacity = request.POST['capacity']
        park = Park(date=date, num_workers=num_workers, attendance=attendance, weather=weather, capacity=capacity)
        park.save()
        return HttpResponseRedirect('/adventurezone/park/')
    else:
        return render(request, 'park.html')

def restaurants_page(request):
    restaurants = Restaurants.objects.all()
    sort_by = request.GET.get('sort_by', None)
    if sort_by:
        if sort_by == 'open':
            restaurants = restaurants.filter(Q(open=True))
        elif sort_by == 'closed':
            restaurants = restaurants.filter(Q(open=False))
        elif sort_by == 'sales':
            restaurants = restaurants.order_by('-total_sales')
        elif sort_by == 'type':
            restaurants = restaurants.order_by('type')
        elif sort_by == 'capacity':
            restaurants = restaurants.order_by('-capacity')
    context = {'restaurants': restaurants}
    return render(request, "restaurants.html", context)


def attractions_page(request):
    include_restaurants = False
    open_attractions = False
    sort_by = ''
    attractions = Attractions.objects.all()

    if request.method == 'POST':
        include_restaurants = request.POST.get('include_restaurants', False)
        open_attractions = request.POST.get('open_attractions', False)
        sort_by = request.POST.get('sort_by', '')

        if include_restaurants:
            attractions = attractions.prefetch_related('restaurants')

        if open_attractions:
            attractions = attractions.filter(Q(open=True))
        if sort_by == 'queue':
            attractions = attractions.order_by('-queue')
        elif sort_by == 'capacity':
            attractions = attractions.order_by('-capacity')
        elif sort_by == 'wait_time':
            attractions = attractions.order_by('-wait_time')
        elif sort_by == 'maintenance':
            attractions = attractions.order_by('maintenance')

    context = {
        'attractions': attractions,
        'include_restaurants': include_restaurants,
        'open_attractions': open_attractions,
        'sort_by': sort_by
    }
    return render(request, 'attractions.html', context)

def places_page(request):
    places = Place.objects.filter(Q(attraction__isnull=False) | Q(restaurant__isnull=False)).order_by('name')
    sort_by = request.GET.get('sort_by', None)
    if sort_by:
        if sort_by == 'open':
            places = places.filter(Q(open=True))
        elif sort_by == 'closed':
            places = places.filter(Q(open=False))
        elif sort_by == 'type':
            places = places.order_by('type')
        elif sort_by == 'capacity':
            places = places.order_by('-capacity')
    context = {'places': places}
    return render(request, 'places.html', context)


