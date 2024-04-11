from django.contrib import admin

from portfolio.models import Social,Email,Phone,Address,Global, Skills, About, Experences, Client

# Register your models here.
admin.site.register(Social)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Global)
admin.site.register(Skills)
admin.site.register(About)
admin.site.register(Experences)
admin.site.register(Client)