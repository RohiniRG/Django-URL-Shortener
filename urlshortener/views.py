from django.shortcuts import render, HttpResponse, redirect
import uuid
from .models import Url

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        context = {
            'link' : request.build_absolute_uri('') + uid 
        }

    return render(request, 'index.html', context)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk) 
    return redirect(url_details.link)
