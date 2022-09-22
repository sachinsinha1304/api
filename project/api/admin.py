from django.contrib import admin

from .models import item,userDetails,Biddings,SoldItems

# Register your models here.
admin.site.register(item)
admin.site.register(userDetails)
admin.site.register(Biddings)
admin.site.register(SoldItems)

