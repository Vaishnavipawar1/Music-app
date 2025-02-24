from django.contrib import admin
from database.models import Addressbook, Contact
# Register your models here.

admin.site.register(Contact)
admin.site.register(Addressbook)