from django.shortcuts import render

from my_app.models import Meca, Segundo

def meca(request):
    meca = Meca.objects.all()

    context_dict = {"meca": meca}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/meca_list.html",
    )

def segundo(request):
    meca = Segundo.objects.all()

    context_dict = {"segundo": segundo}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/segundo_list.html",
    )

# Create your views here.
