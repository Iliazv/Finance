from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ServiceMessage, VebinarMessage, Case, Ip

def main(request):
    cases = Case.objects.all()
    content = {'cases': cases}
    template = loader.get_template('outsource/main.html')
    return HttpResponse(template.render(content, request))

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

def case_page(request, arg):
    case = Case.objects.get(id=arg)

    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        case.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        case.views.add(Ip.objects.get(ip=ip))  

    paragraphs = case.paragraphs.all()
    content = {'case': case, 'paragraphs': paragraphs}
    template = loader.get_template('outsource/case_page.html')
    return HttpResponse(template.render(content, request))

def all_cases(request):
    cases = Case.objects.all()
    content = {'cases': cases}
    template = loader.get_template('outsource/all_cases.html')
    return HttpResponse(template.render(content, request))

def politics(request):
    content = {}
    template = loader.get_template('outsource/politics.html')
    return HttpResponse(template.render(content, request))

def form_service(request):
    FIO = request.POST.get('FIO')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    message = ServiceMessage.objects.create(FIO=FIO, phone=phone, address=address)
    content = {}
    template = loader.get_template('outsource/main.html')
    return HttpResponse(template.render(content, request))

def form_vebinar(request):
    FIO = request.POST.get('FIO_2')
    phone = request.POST.get('phone_2')
    address = request.POST.get('address_2')
    message = VebinarMessage.objects.create(FIO=FIO, phone=phone, address=address)
    content = {}
    template = loader.get_template('outsource/main.html')
    return HttpResponse(template.render(content, request))