from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q

# Create your views here.
def index(request):
    student = Student.objects.all()

    paginator = Paginator(student,4)
    page = request.GET.get('page')

    ###### FOR IP ADRESS #############
    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED_FOR')

        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    print('request 1: '+str(request))
    print('ip 1: '+str(ip))
    #print(ip)
    u = User(user=ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result)== 1: pass
        #print("user exist")
    elif len(result) > 1:pass
        #print("user exist more ...")
    else:
        u.save()
        #print("user is unique")

    count = User.objects.all().count()
    users = User.objects.all()
    #print("total user is: ",count)




    try:
        student = paginator.page(page)
    except PageNotAnInteger:
        student = paginator.page(1)
    except EmptyPage:
        student = paginator.page(paginator.num_pages)

    context = {
        'student':student,
        'page':page,
        'count':count,
        'users':users,
    }
    return render(request,'base.html',context)