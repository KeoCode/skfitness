from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Package, Category
from .forms import PackageForm

# Create your views here.

def all_packages(request):
    """ A view to show all packages, including sorting and search queries """

    packages = Package.objects.all()
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


def package_detail(request, package_id):
    """ A view to show individual Packages details """

    packages = get_object_or_404(Package, pk=package_id)

    context = {
        'packages': packages,
    }

    return render(request, 'packages/package_detail.html', context)

@login_required
def add_package(request):
        """ Add a package to the store """
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect(reverse('home'))

        if request.method == 'POST':
            form = PackageForm(request.POST, request.FILES)
            if form.is_valid():
                package = form.save()
                messages.success(request, 'Successfully added package!')
                return redirect(reverse('package_detail', args=[package.id]))
            else:
                messages.error(request,
                            ('Failed to add package. '
                                'Please ensure the form is valid.'))
        else:
            form = PackageForm()

        template = 'packages/add_package.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


@login_required
def edit_package(request, package_id):
    """ Edit a package in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated package!')
            return redirect(reverse('package_detail', args=[package.id]))
        else:
            messages.error(request,
                           ('Failed to update package. '
                            'Please ensure the form is valid.'))
    else:
        form = PackageForm(instance=package)
        messages.info(request, f'You are editing {package.name}')

    template = 'packages/edit_package.html'
    context = {
        'form': form,
        'package': package,
    }

    return render(request, template, context)


@login_required
def delete_package(request, package_id):
    """ Delete a package from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    package = get_object_or_404(Package, pk=package_id)
    package.delete()
    messages.success(request, 'Package deleted!')
    return redirect(reverse('packages'))