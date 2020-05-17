from django.contrib import admin
from shop.models import User,Contact,Order
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    pass