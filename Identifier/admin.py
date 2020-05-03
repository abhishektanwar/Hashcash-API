from django.contrib import admin
from .models import ContentHash,HashIdentifier
# Register your models here.
admin.site.register(ContentHash)
admin.site.register(HashIdentifier)