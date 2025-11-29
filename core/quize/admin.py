from django.contrib import admin
from .models import Quize, Question, Answer, UserSubmission, UserAnswer
# Register your models here.

class QuizeAdmin(admin.ModelAdmin):  # Customizing the admin interface for the Quize model
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Quize, QuizeAdmin) # Registering the Quize model with the customized admin interface

class QuestionAdmin(admin.ModelAdmin):  # Customizing the admin interface for the Question model
    list_display = ('text', 'quize', 'question_type', 'created_at')
    search_fields = ('text',)
    list_filter = ('question_type', 'created_at')

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):  # Customizing the admin interface for the Answer model
    list_display = ('text', 'question', 'is_correct')
    search_fields = ('text',)
    list_filter = ('is_correct',)

admin.site.register(Answer, AnswerAdmin)

class UserSubmissionAdmin(admin.ModelAdmin):  # Customizing the admin interface for the UserSubmission model
    list_display = ('user_name', 'quize', 'score', 'submitted_at')
    search_fields = ('user_name',)
    list_filter = ('submitted_at',)

admin.site.register(UserSubmission, UserSubmissionAdmin)

class UserAnswerAdmin(admin.ModelAdmin):  # Customizing the admin interface for the UserAnswer model
    list_display = ('submission', 'question', 'answer', 'is_correct')
    list_filter = ('is_correct',)

admin.site.register(UserAnswer, UserAnswerAdmin)

