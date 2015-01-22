from django.contrib import admin
from gigafig.models import Paper, Figure, Table, Workflow
from gigafig.models import UserProfile


class PaperAdmin(admin.ModelAdmin):
    list_display = ('doi_suffix', 'short_name', 'title', 'article_type', 'year')

admin.site.register(Paper, PaperAdmin)
admin.site.register(Figure)
admin.site.register(Table)
admin.site.register(Workflow)
admin.site.register(UserProfile)
