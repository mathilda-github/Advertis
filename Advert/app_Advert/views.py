from django.shortcuts import render, redirect, reverse
from .models import Advertisement
from .forms import AdvertisementForm

#def fun(request):
#    return HttpResponse('Урррррраааааа!')

# Create your views here.
def index (request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers (request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            return redirect(reverse('main_page'))
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)