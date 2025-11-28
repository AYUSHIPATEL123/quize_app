from django.db import models

# Create your models here.

class Quize(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    CHOICES = (
        ('mcq', 'Multiple Choice Question'),
        ('T/F', 'True/False'),
    )    
    quize = models.ForeignKey(Quize,on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=3, choices=CHOICES, default='mcq')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.text    

class UserSubmission(models.Model):
    quize = models.ForeignKey(Quize,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user_name} - {self.quize.title} - {self.score}"

class UserAnswer(models.Model):
    submission = models.ForeignKey(UserSubmission,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to {self.question.text} in submission {self.submission.id}"
