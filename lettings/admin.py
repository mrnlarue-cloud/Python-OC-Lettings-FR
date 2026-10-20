"""Administration des locations et de leurs adresses."""

from django.contrib import admin

from .models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)
