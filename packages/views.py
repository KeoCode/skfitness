from django.shortcuts import render, get_object_or_404
from .models import Packages

# Create your views here.

def all_packages(request):
    """ A view to show all packages, including sorting and search queries """

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)


def Packages_detail(request, packages_id):
    """ A view to show individual Packages details """

    packages = get_object_or_404(Packages, pk=packages_id)

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages_detail.html', context)