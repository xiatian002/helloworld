from django.contrib import admin

# Register your models here.
from .models import Column,Article #two tables 

class ColumnAdmin(admin.ModelAdmin):
  list_display = ('name','slug','intro','nav_display','home_display')


class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title','slug','news_author','pub_date','update_time')


admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)
