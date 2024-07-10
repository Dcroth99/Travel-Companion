from django.contrib import admin
from .models import Destination, Itinerary, Accommodation, Activity, DiningOption, Budget

admin.site.register(Destination)
admin.site.register(Itinerary)
admin.site.register(Activity)
admin.site.register(Accommodation)
admin.site.register(DiningOption)
admin.site.register(Budget)