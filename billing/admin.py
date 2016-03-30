from django.contrib import admin

# Register your models here.
from billing.models import  Membership, Transaction, UserMerchantId, PlanData

admin.site.register(Membership)
admin.site.register(Transaction)
admin.site.register(UserMerchantId)
admin.site.register(PlanData)