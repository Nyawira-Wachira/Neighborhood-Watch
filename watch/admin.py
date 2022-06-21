from django.contrib import admin
from.models import Profile,Post,Neighborhood,Business,HealthCentre,PoliceAuthority

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(HealthCentre)
admin.site.register(PoliceAuthority)