from django.shortcuts import render, redirect, get_object_or_404
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

        return HttpResponse("Error")

    return render(request, 'index.html')


# NEW: Redirect view
def redirect_url(request, short_url):
    obj = get_object_or_404(Url, short_url=short_url)
    return redirect(obj.full_url)