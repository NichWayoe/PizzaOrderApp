from django.contrib import admin
from .models import Subs, Toppings, Pasta, Salads, DinnerPlatters, RegularPizza

# Register your models here.
admin.site.register(Subs)
admin.site.register(Toppings)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(RegularPizza)
