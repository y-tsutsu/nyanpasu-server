from django.contrib import admin

from app.models import Nyanpasu


class NyanpasuAdmin(admin.ModelAdmin):
    pass


admin.site.register(Nyanpasu, NyanpasuAdmin)
