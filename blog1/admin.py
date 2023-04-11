from django.contrib import admin
from .models import short_descriptions
from .models import types
from .models import  template
from .models import  profile

# Register your models here.
admin.site.register(short_descriptions)
admin.site.register(types)
admin.site.register(template)
admin.site.register(profile)



