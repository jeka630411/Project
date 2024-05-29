from django.contrib import admin
from .models import User, CalculationResult, Rating

admin.site.register(User)
admin.site.register(CalculationResult)
admin.site.register(Rating)
