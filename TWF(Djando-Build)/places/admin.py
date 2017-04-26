from django.contrib import admin
from places.models import Location, Zone, GeoTag

# Register your models here.

admin.site.register(Location)
admin.site.register(Zone)
admin.site.register(GeoTag)
