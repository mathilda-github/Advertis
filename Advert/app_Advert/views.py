from django.shortcuts import render, redirect, reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

#def fun(request):
#    return HttpResponse('Урррррраааааа!')

# Create your views here.
def index (request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisement/index.html', context)

def top_sellers (request):
    return render(request, 'app_advertisement/top-sellers.html')


@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_advertisement/advertisement-post.html', context)