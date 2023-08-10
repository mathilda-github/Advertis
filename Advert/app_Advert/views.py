from django.shortcuts import render


#def fun(request):
#    return HttpResponse('Урррррраааааа!')

# Create your views here.
def index (request):
#    advertisements = Advertisement.object.all()
#    context = {'adverisements': advertisements}
    return render(request, 'index.html')

def top_sellers (request):
    return render(request, 'top-sellers.html')