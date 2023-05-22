from django.shortcuts import render, get_object_or_404
from .models import Packages

# Create your views here.

def all_packages(request):
    """ A view to show all packages, including sorting and search queries """

    packages = Packages.objects.all()
    query = None
    categories = None

    if request.GET:
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