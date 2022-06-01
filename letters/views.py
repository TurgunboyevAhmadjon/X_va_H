from django.shortcuts import render
from .models import *
def asosiy(request):
    qidiruv_sozi = request.GET.get('qidirish')
    t_soz = Togri.objects.filter(soz=qidiruv_sozi)
    if len(t_soz) > 0:
        n_sozlar = Notogri.objects.filter(togri=t_soz[0])
    else:
        n_sozlar = Notogri.objects.filter(soz=qidiruv_sozi)
        if len(n_sozlar) > 0:
            t_soz =[n_sozlar[0].togri]
            n_sozlar = Notogri.objects.filter(togri=t_soz[0])
        else:
            t_soz=["Bunaqa so'z yoq!"]
            n_sozlar=[]
    data = {
        'togrisi': t_soz[0],
        'notogrilar': n_sozlar,
    }

    return render(request, 'result.html', data)
