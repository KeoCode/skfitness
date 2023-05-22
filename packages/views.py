from django.shortcuts import render
from .models import Packages

# Create your views here.

def all_packages(request):
    """ A view to show all packages, including sorting and search queries """

    packages = Packages.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)