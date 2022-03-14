from django.shortcuts import render
from main.models import Logo
from .models import AboutPage, AboutTab, AboutAccordian, TeamMember

# Create your views here.
def about(request):
    ctx = {
        'logo': Logo.objects.last(),
        'page_obj': AboutPage.objects.last(),
        'about_sections': AboutTab.objects.all().order_by('order_num'),
        'accordion_entries': AboutAccordian.objects.all().order_by('order_num'),
        'team_members': TeamMember.objects.all()
    }
    return render(request, 'about/index.html', context=ctx)
