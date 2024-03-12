from django.contrib import admin
from .models import ServiceMessage, VebinarMessage, Case, Paragraph, Image, Ip

#qsl
admin.site.register(ServiceMessage)
admin.site.register(VebinarMessage)
admin.site.register(Case)
admin.site.register(Paragraph)
admin.site.register(Image)
admin.site.register(Ip)
