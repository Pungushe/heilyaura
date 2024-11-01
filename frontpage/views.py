from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from cart.forms import CartAddProductForm
from .models import Category, Product

def popular_list(request):
     products=Product.objects.filter(available=True)[:3]
     return render(request, 'frontpage/main/frontpage.html', {'products':products})

def product_detail(request, slug):
     product=get_object_or_404(Product, slug=slug, available=True)
     cart_product_form = CartAddProductForm()
     
     context = {
          'product':product,
          'cart_product_form': cart_product_form
     }
     
     return render(request, 'frontpage/detail/detail.html', context)

def product_list(request, category_slug=None):
     category = None
     categories = Category.objects.all() 
     products = Product.objects.filter(available=True)
     page=request.GET.get('page', 1)
     paginator = Paginator(products, 2)
     current_page = paginator.page(int(page))
     
     if category_slug:
          category = get_object_or_404(Category, slug=category_slug)
          paginator = Paginator(products.filter(category=category), 1)
          current_page = paginator.page(int(page))
          
     context = {
          'category': category,
          'categories': categories,
          'products': current_page,
          'slug_url': category_slug
     }
     
     return render(request, 'frontpage/product/list.html', context)
     