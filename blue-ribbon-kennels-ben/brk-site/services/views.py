from django.shortcuts import render
from services.models import Service
from main.models import Logo

# Create your views here.
def service(request, service):
    ctx = {
        'logo': Logo.objects.last(),
        # 'service': Service.objects.get(title=service)
    }
    if Service.objects.exists():
        ctx['service'] = Service.objects.get(title=service)
    return render(request, 'services/service.html', context=ctx)