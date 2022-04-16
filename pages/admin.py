from turtle import title
from django.contrib import admin
from .models import Page
# Register your models here.


admin.site.register(Page)
#configuracion del panel 
title="Panel de gestión"
subtitle='Blog con Django'
admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle
