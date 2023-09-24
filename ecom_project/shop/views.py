from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

# before paginator
# def allProdCat(request,c_slug=None):
#     c_page = None
#     products = None
#     # print(c_slug)
#     if c_slug != None:#if slug is present
#         c_page=get_object_or_404(Category,slug=c_slug)#load single object category slag
#         #get_object_or_404 is a convenient shortcut function provided by Django, which is used for getting an object from a database
#         products_list=Product.objects.all().filter(category=c_page,available=True)#load selected all products under particular slug
#         print(c_page)
#         print(products_list)
#     else:
#         products_list=Product.objects.all().filter(available=True)#load all products in index page
#         print(products_list)
# return render(request,"category.html",{'category':c_page,'products':products_list})


# after paginator
def allProdCat(request,c_slug=None):
    c_page = None
    products_list= None
    # print(c_slug)
    if c_slug != None:#if slug is present
        c_page=get_object_or_404(Category,slug=c_slug)#load single object category slag
        #get_object_or_404 is a convenient shortcut function provided by Django, which is used for getting an object from a database
        products_list=Product.objects.all().filter(category=c_page,available=True)#load selected all products under particular slug
        # print(c_page)
        # print(products_list)
    else:
        products_list=Product.objects.all().filter(available=True)#load all products in index page
        # print(products_list)
    # ==================== pageination code==============================================
    paginator=Paginator(products_list,6)
    print("paginator:")
    print(paginator)
    # passing product_list in paginator .show only 6 content in a page
    try:
        page=int(request.GET.get('page','1'))
        print("page :")
        print(page)
    #     page in bracket?
    except:
        page=1#default page is 1

    try:
        products=paginator.page(page)
        print("products:")
        print(products)
        # Paginator.page(number)¶
        # Returns a Page object with the given 1-based index.
        # paginator.page(variable name)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)


    return render(request,"category.html",{'category':c_page,'products':products})
def proDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
        # in product variable it contain one object from product table
        # product=product object(2)=>name of the class to which object belongs
        # print(product) Product object (2)

        # a={'product': product}
        # print(a) {'product': <Product: Product object (2)>}


        print("prodetails")
        print(product)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})