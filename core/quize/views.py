from django.shortcuts import redirect, render
from .models import Quize, Question, Answer, UserSubmission, UserAnswer 
# Create your views here.

def quize_list(request):
    quizes = Quize.objects.all()
    return render(request, 'quize_list.html', {'quizes': quizes})

def quize_detail(request, quize_id):
    quize = Quize.objects.get(id=quize_id)
    questions = Question.objects.filter(quize=quize)
    answers = Answer.objects.filter(question__in=questions)
    if request.method == 'POST':
        user_submission = UserSubmission.objects.create(
            quize=quize,
            user_name=request.POST.get('user_name', 'Anonymous'),
            score=0
        )
        for question in questions:
            sel_ans_id = request.POST.get('question_' + str(question.id))
            if sel_ans_id:
                answer = Answer.objects.get(id=sel_ans_id)
                user_answer = UserAnswer.objects.create(
                    submission=user_submission,
                    question=question,
                    answer=answer,
                    is_correct=answer.is_correct
                )
                user_answer.save()
                if answer.is_correct:
                    user_submission.score += 1
        user_submission.save()
        return redirect('quize_result', submission_id = user_submission.id)
    return render(request, 'quize.html', {'quize': quize, 'questions': questions, 'answers': answers})       

def quize_result(request, submission_id):
    submission = UserSubmission.objects.get(id=submission_id)
    return render(request, 'quize_result.html', {'submission': submission})
