# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from device.models import * 

# Create your views here.


def index(request):
    return render_to_response("index.html")


def device_list(request):
    # device_router = DeviceRouterForm()
    device_router =  DeviceRouter.objects.all()
    # paginator = Paginator(device_list, 5) # Show 5 articles per page
    # page = request.GET.get('page')
    # try:
    #     device_router = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     device_router = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     device_router = paginator.page(paginator.num_pages)
        
    print device_router
    return render_to_response('device_list.html', 
        {"device_router":device_router}
        )


# http://127.0.0.1/device/update/?mac=00:00:c1:88:1a:2e&device_id=1@3    
def create_device(request):
    device_id = request.GET.get('device_id')
    mac = request.GET.get('mac') #"00:00:c0:88:0a:2e"
    state_info = 'new device'
    extro_info = 'no record'
    pub_date = timezone.now()
    try:
        new_device = DeviceRouter(device_id=device_id, mac=mac, state_info=state_info, extro_info=extro_info, pub_date=pub_date)
        new_device.save()
        return HttpResponse("create ok")
    except:
        return HttpResponse("we are sorry, this mac addres exited!")


# http://127.0.0.1/device/update/?mac=00:00:c1:88:1a:2e&device_id=1@3
def update_device(request):
    device_id = request.GET.get('device_id')
    mac = request.GET.get('mac') #"00:00:c0:88:0a:2e"
    state_info = request.GET.get('state_info', "I'm down")
    pub_date = timezone.now()
    try:
        target_device = get_object_or_404(DeviceRouter, mac=mac)
        DeviceRouter.objects.filter(mac=mac).update(device_id=device_id, state_info=state_info, pub_date=pub_date)
        return HttpResponse("update ok")
    except:
        return HttpResponse("such device not found!")


