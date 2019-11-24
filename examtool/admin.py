from django.contrib import admin
from examtool.models import Category, Question
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    list_display_links = ('category_id', 'category_name')


admin.site.register(Category, CategoryAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'question', 'answer1', 'answer2', 'answer3', 'answer4', 'seikai')
    list_display_links = ('category_id', 'question', 'answer1', 'answer2', 'answer3', 'answer4', 'seikai')


admin.site.register(Question, QuestionAdmin)
