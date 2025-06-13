from django.contrib import admin
from .models import MarketModel
# Register your models here.

@admin.register(MarketModel)
class MarketModelAdmin(admin.ModelAdmin):
    search_fields=['name','location']