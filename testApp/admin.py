
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Section_1, Section_2, Section_3, Section_4, Section_5, Section_6, Section_7, Section_8

class MyModelAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
   pass



admin.site.register(Section_1, MyModelAdmin)
admin.site.register(Section_2, MyModelAdmin)
admin.site.register(Section_3, MyModelAdmin)
admin.site.register(Section_4, MyModelAdmin)
admin.site.register(Section_5, MyModelAdmin)
admin.site.register(Section_6, MyModelAdmin)
admin.site.register(Section_7, MyModelAdmin)
admin.site.register(Section_8, MyModelAdmin)