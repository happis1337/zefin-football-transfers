from .models import *

def base_context(request):
    countries = Country.objects.all()[:11]
    context= {
        'countries': countries,
    }
    return context