from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .choices import prize_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)# list, number of elements per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')
    #Keywords
    if 'keywords' in request.GET:#name of the field keywords
        keywords = request.GET['keywords']
        if keywords:#not empty string
            queryset_list = queryset_list.filter(description__icontains=keywords)#fieldtosearch__(double underscore)icontains

    #City
    if 'city' in request.GET:#name of the field city
        city = request.GET['city']
        if city:#not empty string
            queryset_list = queryset_list.filter(city__iexact=city)#fieldtosearch__(double underscore)iexact

    #State
    if 'state' in request.GET:#name of the field state
        state = request.GET['state']
        if state:#not empty string
            queryset_list = queryset_list.filter(state__iexact=state)#fieldtosearch__(double underscore)iexact
    
    #Bedrooms
    if 'bedrooms' in request.GET:#name of the field bedrooms
        bedrooms = request.GET['bedrooms']
        if bedrooms:#not empty string
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)#fieldtosearch__(double underscore)iexact

    #Price
    if 'price' in request.GET:#name of the field price
        price = request.GET['price']
        if price:#not empty string
            queryset_list = queryset_list.filter(price__lte=price)#fieldtosearch__(double underscore)iexact


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'prize_choices': prize_choices,
        'listings': queryset_list
    }

    return render(request, 'listings/search.html', context)