from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Package


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Package, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Package, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings.SPEND_OFFER_THRESHOLD:
        offer = total * Decimal(settings.SPEND_OFFER_PERCENTAGE / 100)
        spend_offer_delta = total - settings.SPEND_OFFER_THRESHOLD 
    else:
        offer = 0
        spend_offer_delta = 0

    grand_total = total - offer

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'offer': offer,
        'spend_offer_delta': spend_offer_delta,
        'spend_offer_threshold': settings.SPEND_OFFER_THRESHOLD,
        'grand_total': grand_total,
    }

    return context