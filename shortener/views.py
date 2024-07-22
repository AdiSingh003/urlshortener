from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'shortener/index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = url, uid = uid)
        new_url.save()
        return HttpResponse(uid)
    
def redirectTo(request,pk):
    url_details = Url.objects.get(uid=pk)
    if (url_details.link.find('https://') == -1):
        return redirect('https://'+ url_details.link)
    else:
        return redirect(url_details.link)
        

