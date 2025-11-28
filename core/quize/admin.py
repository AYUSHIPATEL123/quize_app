from django.contrib import admin
from .models import Quize, Question, Answer, UserSubmission, UserAnswer
# Register your models here.

class QuizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Quize, QuizeAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quize', 'question_type', 'created_at')
    search_fields = ('text',)
    list_filter = ('question_type', 'created_at')

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    search_fields = ('text',)
    list_filter = ('is_correct',)

admin.site.register(Answer, AnswerAdmin)

class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'quize', 'score', 'submitted_at')
    search_fields = ('user_name',)
    list_filter = ('submitted_at',)

admin.site.register(UserSubmission, UserSubmissionAdmin)

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('submission', 'question', 'answer', 'is_correct')
    list_filter = ('is_correct',)

admin.site.register(UserAnswer, UserAnswerAdmin)

