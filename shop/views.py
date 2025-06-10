from django.shortcuts import render
#def first_view(request):
    #return render(request, 'first.html')

#def second_view(request):
    #return render(request, 'second.html')
def main_page(request):
    return render(request, 'main_page.html')

def catalog_page(request):
    return render(request, 'catalog.html')

def conatcts_page(request):
    return render(request, 'contacts.html')

def cart(request):
    return render(request, 'cart.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    return render(request, 'categories.html')

def cabinet(request):
    return render(request, 'cab.html')

def category_detail(request, id):
    category_name = f"Категория номер {id}" 
    data = {
        'category_name': category_name,
        'category_id': id,
    }
    return render(request, 'category_detail.html', data)
