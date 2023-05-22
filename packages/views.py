from django.shortcuts import render, get_object_or_404
from .models import Packages

# Create your views here.

def all_packages(request):
    """ A view to show all packages, including sorting and search queries """

    packages = Packages.objects.all()
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                packages = packages.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
                
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            packages = packages.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            packages = packages.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('packages'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            packages = packages.filter(queries)


    context = {
        'packages': packages,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'packages/packages.html', context)


def Packages_detail(request, packages_id):
    """ A view to show individual Packages details """

    packages = get_object_or_404(Packages, pk=packages_id)

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages_detail.html', context)