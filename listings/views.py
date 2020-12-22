from django.shortcuts import render, get_object_or_404

from .models import Listings
from listings.choices import price_choices, region_choices, bedroom_choices


def index(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings

    }
    return render(request, 'listings/listings.html', context=context)


def listing(request, listing_id):
    listing_single = get_object_or_404(Listings, pk=listing_id)
    context = {'listing': listing_single}
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listings.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'region_choices': region_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context=context)
