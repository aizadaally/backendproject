from django.contrib import admin
from django.utils.translation import gettext_lazy as _ 
from .models import *

admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Record)