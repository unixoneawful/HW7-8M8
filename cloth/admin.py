from django.contrib import admin
from .models import CustomerCL, TagCL, ProductCl, OrderCL

admin.site.register(CustomerCL)
admin.site.register(TagCL)
admin.site.register(ProductCl)
admin.site.register(OrderCL)

