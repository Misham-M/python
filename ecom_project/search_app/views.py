from django.shortcuts import render
from shop.models import Product
from django.db.models import Q #for query purpose

# Create your views here.
def SearchResult(request):
    products=None
    query=None

    if 'q' in request.GET:
        query = request.GET.get('q')
        # q is name of search text box
        products = Product.objects.all().filter(Q(name__contains = query) | Q(description__contains = query))
        # syntax(field name__contain)
        return render(request,'search.html',{'query':query,'products':products})