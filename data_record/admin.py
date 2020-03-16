from django.contrib import admin
from .models import History,Project,Users
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=("release_date",)
    search_field=("release_date",)
    date_hierarchy="release_date"
    fields=("project_name","person","release_date")
    #raw_id_fields=("project_name",)
class HistoryAdmin(admin.ModelAdmin):
    raw_id_fields=("project_name",)
admin.site.register(History,HistoryAdmin)
#admin.site.register(Project)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Users)
