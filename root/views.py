from django.shortcuts import render
from django.http import HttpResponse
from root.models import Url

def index(request):
    if request.method == "POST":
        full_url = request.POST.get('full_url')
        if full_url:
            obj = Url.create(full_url)
            if obj:
                return render(request, 'index.html', {
                    'full_url': obj.full_url,
                    'short_url': obj.short_url
                })
            else:
                return HttpResponse("Error creating URL")
        else:
            return HttpResponse("No URL provided")
    return render(request, 'index.html')