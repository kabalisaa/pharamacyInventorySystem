from django.contrib import admin
from pharmacy.models import *


# # Register your models here.
admin.site.register(Pharmacist)
admin.site.register(Supplier)
admin.site.register(MedecineType)
admin.site.register(MedecineCategory)
admin.site.register(Medecine)
admin.site.register(PharmacyRequest)
admin.site.register(ReceivedMedecine)
admin.site.register(StockOut)