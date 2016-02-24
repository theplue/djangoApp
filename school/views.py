from django.shortcuts import render
from django.http import Http404

from school.models import Student


def index(request):
	items = Item.objects.get()
	return render(request, 'inventory/index.html', {
		'items': items,
	})

def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/item_detail.html', {
		'item': item,
	})