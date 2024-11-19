from .models import EventCategory

def categories_processor(request):
    return {
        'categories': EventCategory.objects.all()[:5]
    }
