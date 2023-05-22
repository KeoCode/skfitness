from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from packages.models import Package


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified packages to the shopping bag """

    packages = get_object_or_404(Package, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    messages.success(request, f'Added {packages.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified packages to the specified amount"""

    packages = get_object_or_404(packages, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'packages_size' in request.POST:
        size = request.POST['packages_size']
    bag = request.session.get('bag', {})

    

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        packages = get_object_or_404(packages, pk=item_id)
        

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)