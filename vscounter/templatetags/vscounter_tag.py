
from django import template
from vscounter.models import Vscounter
from django.db.models import Q
register = template.Library()


@register.simple_tag
def get_ip(request):
    adress = request.META.get('HTTP_X_FORWARDED_FOR')
    if adress:
        ip = adress.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@register.simple_tag
def vscounter(request):
    ip = get_ip(request)
    u = Vscounter(user=ip)
    result = Vscounter.objects.filter(Q(user__icontains=ip))
    if len(result) > 0:
        pass
    else:
        u.save()
    count = Vscounter.objects.all().count()
    return count
