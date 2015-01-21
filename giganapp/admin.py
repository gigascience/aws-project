from django.contrib import admin
from giganapp.models import Paper, Figure, Table


class PaperAdmin(admin.ModelAdmin):
    list_display = ('doi_suffix', 'short_name', 'title', 'article_type', 'year')

admin.site.register(Paper, PaperAdmin)
admin.site.register(Figure)
admin.site.register(Table)
