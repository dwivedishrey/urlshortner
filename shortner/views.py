from django.shortcuts import render,redirect
import uuid
from django.http import HttpResponse
from .models import url
def index(request):
    return render(request,'index.html')
def create(request):
    if request.method == 'POST':
        link=request.POST['link']
        uid= str(uuid.uuid4())[:5]
        new_url=url(link=link,uvid=uid)
        new_url.save()
        return HttpResponse(uid)
def go(request, pk):
    url_details=url.objects.get(uvid=pk)
    return redirect(url_details.link)
        
# Create your views here.
